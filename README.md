# Telegram Message Bridge

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Aiogram](https://img.shields.io/badge/Aiogram-3.x-0088cc?style=flat&logo=telegram&logoColor=white)
![License](https://img.shields.io/github/license/Melfex/telegram-msg-bridge?style=flat)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow?style=flat)

**Telegram Message Bridge** is a personal Telegram bot that serves as a secure and configurable messaging gateway between users and the bot owner.

Users can send messages to the owner in two modes:

- **Direct mode** — Sender's identity (username, display name, and/or user ID) is visible to the owner
- **Anonymous mode** — Sender's identity is completely hidden, providing full privacy

This bot acts as a personal communication bridge, enabling controlled, private, and convenient interaction with followers, friends, contacts, or anyone who wishes to reach out.

## Table of Contents

- 🚧 [Project Status](#project-status)
- 📋 [Planned Features](#planned-features)
- 📂 [Project Structure](#project-structure)
- 🛠  [Prerequisites](#prerequisites)
- ⚙️ [Installation & Local Development Setup](#installation--local-development-setup)
- 🤝 [Contributing](#contributing)
- 📄 [License](#license)
- 📧 [Contact](#contact)

## Project Status

🚧 **Actively under development** 🚧

The project is in its early stages. The modular architecture and foundational structure are complete, while the core messaging logic, mode selection, owner interface, and additional features are currently being implemented.

## Planned Features

- [ ] Receiving various message types from users (text, photos, voice, videos, documents, etc.)
- [ ] Two distinct message submission modes:
  - **Direct** — Full sender identity revealed to the owner
  - **Anonymous** — Sender identity fully concealed
- [ ] Owner dashboard: view incoming messages, reply to users, block/unblock, manage settings
- [ ] Multilingual support using lexicon-based internationalization
- [ ] Advanced message filtering (spam protection, banned words/phrases, rate limiting)
- [ ] Comprehensive logging and security-oriented middleware
- [ ] Asynchronous database layer (PostgreSQL recommended; SQLite for local development)
- [ ] Easy deployment using Docker + docker-compose

## Project Structure

Clean, modular, and layered architecture optimized for maintainability and scalability:

```text
telegram-msg-bridge/
├── config/          # Configuration (Pydantic models, loaders)
├── database/        # ORM models, async sessions, Alembic migrations
├── filter/          # Custom aiogram filters
├── handler/         # Routers, message/callback/command handlers
├── keyboard/        # Inline & reply keyboards
├── lexicon/         # Localized strings and i18n support
├── middleware/      # Throttling, logging, authentication, etc.
├── state/           # FSM states
├── tests/           # pytest-based unit & integration tests
├── util/            # Helpers, validators, logging setup
├── .env.example
├── instance.py      # Bot & Dispatcher factory / instantiation
├── main.py          # Application entry point
└── pyproject.toml   # Dependency & build management with Poetry
```


## Prerequisites

- **Python** ≥ 3.10 (recommended: 3.11 or 3.12 for better asyncio performance and compatibility with aiogram 3.25+)
- **[Poetry](https://python-poetry.org/)** ≥ 1.5 – for dependency management and virtual environments
- **Git** – required to clone the repository
- **Telegram Bot Token** – obtain from [@BotFather](https://t.me/botfather)
- **Optional (for advanced development or future features)**:
  - PostgreSQL ≥ 13 – if planning to use async database support (e.g., SQLAlchemy + asyncpg)
  - Docker & docker-compose – for containerized deployment (planned in future updates)

All core dependencies (aiogram ≥3.25, structlog, rich, pydantic-settings, python-dotenv, etc.) are automatically installed via `poetry install`.

## Installation & Local Development Setup

1. Clone the repository

   ```bash
   git clone https://github.com/Melfex/telegram-msg-bridge.git
   cd telegram-msg-bridge
    ```
2. Install dependencies

   ```bash
   poetry install
   ```
3. Copy and configure environment variables

   ```bash
   cp .env.example .env
   ```
   Edit .env and add at least:
   ```
   BOT_TOKEN=your_bot_token_from_BotFather
   # OWNER_ID=your_telegram_user_id_here   # Recommended for owner-only access
   ```
4. Run the bot

   ```bash
   poetry run python main.py
   ```

## Contributing

This is an open-source project under active development.

Contributions are welcome in the following forms:

- Suggesting features or improvements (open an Issue)
- Reporting bugs
- Submitting pull requests

For significant changes, please open an issue first to discuss the proposed direction.

## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

## Contact

- Maintainer: [@Melfex](https://t.me/Melfex) (Telegram)

Bot username and live link will be shared once a stable version is released.

---

Built with [aiogram 3](https://docs.aiogram.dev/en/latest/) • Modern Python practices
Contributions and stars are very welcome! ⭐

