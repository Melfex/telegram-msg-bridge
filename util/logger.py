from __future__ import annotations

import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional, Union, TYPE_CHECKING

import structlog
from structlog.stdlib import BoundLogger

from enums import LogLevel

if TYPE_CHECKING:
    from structlog.types import Processor


def setup_logging(
        *,
        log_level: Union[LogLevel, str] = LogLevel.INFO,
        json_format: bool = False,
        log_file: Optional[Union[str, Path]] = None,
        rotate: bool = True,
        max_bytes: int = 10_485_760,  # 10 MiB
        backup_count: int = 5,
        service_name: Optional[str] = None,
        environment: Optional[str] = None,
) -> BoundLogger:
    """
    configure structlog and standard logging with console and optional file output.

    Args:
        log_level: minimum logging level
        json_format: if True, output JSON logs
        log_file: path to log file
        rotate: whether to rotate log files
        max_bytes: max size of a log file before rotation
        backup_count: number of backup files to keep
        service_name: optional service name added to every log record
        environment: optional environment name added to every log record

    Returns:
        a configured structlog bound logger instance
    """
    # Convert log level to numeric value
    level_str = (
        log_level.value if isinstance(log_level, LogLevel) else log_level.upper()
    )
    level_value = getattr(logging, level_str, logging.INFO)

    logging.basicConfig(format="%(message)s", stream=sys.stdout, level=level_value)
    root_logger = logging.getLogger()
    root_logger.setLevel(level_value)

    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level_value)
    console_handler.setFormatter(logging.Formatter("%(message)s"))
    root_logger.addHandler(console_handler)

    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        if rotate:
            file_handler = RotatingFileHandler(
                str(log_path), maxBytes=max_bytes, backupCount=backup_count
            )
        else:
            file_handler = logging.FileHandler(str(log_path))
        file_handler.setLevel(level_value)
        file_handler.setFormatter(logging.Formatter("%(message)s"))
        root_logger.addHandler(file_handler)

    logging.getLogger("aiogram").setLevel(logging.WARNING)
    logging.getLogger("aiogram.dispatcher").setLevel(logging.WARNING)
    logging.getLogger("aiogram.event").setLevel(logging.WARNING)
    logging.getLogger("asyncio").setLevel(logging.WARNING)

    shared_processors: list[Processor] = [
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso", key="timestamp"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
    ]

    if service_name or environment:

        def add_static_context(
                _logger: logging.Logger, method_name: str, event_dict: dict
        ) -> dict:
            if service_name:
                event_dict["service"] = service_name
            if environment:
                event_dict["env"] = environment
            return event_dict

        shared_processors.insert(0, add_static_context)

    if json_format:
        processors = shared_processors + [structlog.processors.JSONRenderer()]
    else:
        processors = shared_processors + [structlog.dev.ConsoleRenderer(colors=True)]

    structlog.configure(
        processors=processors,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=BoundLogger,
        cache_logger_on_first_use=True,
    )

    return structlog.get_logger()
