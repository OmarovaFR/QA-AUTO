# QA Autotests Portfolio

Учебный проект для демонстрации навыков начинающего Automation QA.

## Что внутри

- Python 3.11
- pytest
- Flask test client
- fixtures
- parametrization
- positive and negative API tests
- HTTP status code assertions
- JSON response validation
- GitHub Actions CI

## Структура

```text
qa-autotests/
├── .github/
│   └── workflows/
│       └── tests.yml
├── tests/
│   ├── conftest.py
│   ├── test_health.py
│   └── test_users.py
├── app.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Запуск

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Установка зависимостей:

```bash
pip install -r requirements.txt
```

Запуск тестов:

```bash
pytest -v
```

## Что проверяют тесты

1. Доступность health-check endpoint.
2. Получение существующего пользователя.
3. Обработку несуществующего пользователя с `404`.
4. Валидацию обязательного поля `name`.
5. Создание пользователя с кодом `201`.
6. Структуру JSON-ответа.

## CI

При каждом `push` и `pull request` GitHub Actions устанавливает Python 3.11, зависимости и запускает `pytest -v`.

## Что я практикую

Проект демонстрирует базовые навыки автоматизации: написание тестов, фикстуры, параметризацию, проверки API-ответов и интеграцию тестов в CI.

> Проект учебный и создан для портфолио, а не для имитации коммерческого опыта.
