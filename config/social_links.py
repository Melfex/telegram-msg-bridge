from __future__ import annotations

import json
from pathlib import Path

from pydantic import BaseModel, HttpUrl, Field


_CONFIG_PATH = Path(__file__).parent / "social_links.json"
_EXAMPLE_PATH = Path(__file__).parent / "social_links.example.json"


class SocialLink(BaseModel):
    """A single social profile entry with a display label and a validated URL"""

    label: str = Field(min_length=1, max_length=64)
    url: HttpUrl


class SocialLinksConfig(BaseModel):
    """Container for all owner social profile links"""

    links: list[SocialLink] = Field(min_length=1)


def _load(path: Path = _CONFIG_PATH) -> SocialLinksConfig:
    """Load and validate the social links config file"""
    if not path.exists():
        raise FileNotFoundError(
            f"Social links config not found: '{path}'.\n"
            f"Copy the example file and fill in your links:\n"
            f"  cp {_EXAMPLE_PATH.relative_to(Path.cwd())} "
            f"{path.relative_to(Path.cwd())}"
        )
    data = json.loads(path.read_text(encoding="utf-8"))
    return SocialLinksConfig.model_validate(data)


social_links: SocialLinksConfig = _load()
