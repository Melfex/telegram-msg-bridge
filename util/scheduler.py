from __future__ import annotations

import asyncio
import contextlib
import heapq
import time
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Iterable, Protocol, runtime_checkable

from structlog import get_logger

if TYPE_CHECKING:
    from aiogram import Bot

logger = get_logger(__name__)

# Telegram's deleteMessages accepts at most 100 message ids per call
_BATCH_LIMIT: int = 100


@runtime_checkable
class DeleteAfter(Protocol):
    """
    Callable injected into handlers and middlewares for delayed message cleanup::

        delete_after(chat_id, message_id, delay=30)
        delete_after(chat_id, [msg1, msg2], delay=60)
    """

    def __call__(
        self,
        chat_id: int,
        message_ids: int | Iterable[int],
        delay: float,
    ) -> None: ...


@dataclass(order=True, slots=True)
class _Job:
    """A single pending deletion, ordered by due time then insertion order"""

    due: float
    seq: int
    chat_id: int = field(compare=False)
    message_id: int = field(compare=False)


class MessageJanitor:
    """Heap-backed, single-worker scheduler for delayed Telegram message deletion"""
    def __init__(self) -> None:
        self._heap: list[_Job] = []
        self._seq: int = 0
        self._wakeup: asyncio.Event = asyncio.Event()
        self._worker: asyncio.Task[None] | None = None
        self._bot: Bot | None = None

    def start(self, bot: Bot) -> None:
        """Bind the bot and launch the background worker"""
        if self._worker is not None:
            return
        self._bot = bot
        self._worker = asyncio.create_task(self._run(), name="message-janitor")
        logger.info("message janitor started")

    async def stop(self) -> None:
        """Cancel the worker"""
        if self._worker is None:
            return
        self._worker.cancel()
        with contextlib.suppress(asyncio.CancelledError):
            await self._worker
        self._worker = None
        self._heap.clear()
        logger.info("message janitor stopped")

    def schedule(
        self,
        chat_id: int,
        message_ids: int | Iterable[int],
        delay: float,
    ) -> None:
        """
        Queue one or more messages in ``chat_id`` for deletion after ``delay`` seconds
        """
        due = time.monotonic() + max(delay, 0.0)
        ids = (message_ids,) if isinstance(message_ids, int) else tuple(message_ids)

        for message_id in ids:
            heapq.heappush(
                self._heap,
                _Job(due=due, seq=self._seq, chat_id=chat_id, message_id=message_id),
            )
            self._seq += 1

        self._wakeup.set()

    async def _run(self) -> None:
        """Drain due jobs forever, sleeping exactly until the next deadline"""
        while True:
            self._wakeup.clear()

            if not self._heap:
                await self._wakeup.wait()
                continue

            delay = self._heap[0].due - time.monotonic()
            if delay <= 0:
                await self._flush_due()
                continue

            try:
                await asyncio.wait_for(self._wakeup.wait(), timeout=delay)
            except asyncio.TimeoutError:
                await self._flush_due()

    async def _flush_due(self) -> None:
        """Pop every job whose deadline has passed and delete them per chat"""
        now = time.monotonic()
        due_by_chat: dict[int, list[int]] = {}

        while self._heap and self._heap[0].due <= now:
            job = heapq.heappop(self._heap)
            due_by_chat.setdefault(job.chat_id, []).append(job.message_id)

        for chat_id, message_ids in due_by_chat.items():
            await self._delete(chat_id, message_ids)

    async def _delete(self, chat_id: int, message_ids: list[int]) -> None:
        """Delete messages in batches"""
        if self._bot is None:
            return

        for start in range(0, len(message_ids), _BATCH_LIMIT):
            chunk = message_ids[start : start + _BATCH_LIMIT]
            try:
                await self._bot.delete_messages(chat_id=chat_id, message_ids=chunk)
            except Exception as error:  # noqa: BLE001 - best-effort cleanup
                logger.warning(
                    "janitor failed to delete messages",
                    chat_id=chat_id,
                    message_ids=chunk,
                    error=str(error),
                )


__all__ = [
    "MessageJanitor",
    "DeleteAfter",
]
