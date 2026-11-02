![Tests](https://github.com/w-osipov/aqa-juice-shop/actions/workflows/run_tests.yml/badge.svg)

# aqa_juice_shop

Учебный пет-проект по автоматизации тестирования интернет-магазина
[OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) — популярного
полигона для практики в тестировании и не только.

## Что внутри

- **UI-тесты на Playwright + pytest** — регистрация и валидация форм
  (позитивный и негативный сценарии, проверка блокировки кнопки).
- **CI на GitHub Actions** — прогон тестов на каждый push, с кэшированием
  браузеров Playwright (`playwright-cache`).
- **Docker Compose** — приложение поднимается одной командой перед прогоном.
- **docs/test-plan.md** — тест-план проекта.
- **uv** — управление зависимостями и фиксированной версией Python.

## Структура

tests/ — тесты и фикстуры (conftest.py)
src/ — вспомогательный код
docs/ — тест-план
.github/workflows/ — пайплайн CI

## Как запустить локально

```bash
# 1. Поднять приложение
docker compose up -d

# 2. Установить зависимости и браузеры
uv sync
uv run playwright install chromium

# 3. Прогнать тесты
uv run pytest tests/ -v