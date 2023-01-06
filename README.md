[![lint and tests](https://github.com/vadim-gusak/tbot_random_book/actions/workflows/main.yml/badge.svg)](https://github.com/vadim-gusak/tbot_random_book/actions/workflows/main.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/5eb3dcf63f3aa3761342/maintainability)](https://codeclimate.com/github/vadim-gusak/tbot_random_book/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/5eb3dcf63f3aa3761342/test_coverage)](https://codeclimate.com/github/vadim-gusak/tbot_random_book/test_coverage)

# Случайная книга

Простой телеграм бот, который присылает случайную книгу по запросу.

Книги беру здесь: https://www.livelib.ru/book/random

Использую [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI), 
[BeautifulSoup](https://pypi.org/project/beautifulsoup4/) и 
[requests](https://pypi.org/project/requests/). 

Протестировать можно [здесь](https://t.me/RandomBookBot).

## Запуск

Для сборки используется poetry ver. 1.3.1

Подготовлен Makefile с командами для запуска.
Установка зависимостей:
```commandline
make install
```
Или так:
```commandline
poetry install
```

Для запуска необходимо установить переменные окружения:
- TOKEN с вашим токеном
- URL: https://www.livelib.ru/book/random

Я использую [dotenv](https://pypi.org/project/python-dotenv/). 
Эти переменные можно указать в .env файле в корне проекта. 
Скрипт сам их найдет.

Непосредственно запуск:
```commandline
make bot
```
Или:
```commandline
poetry run bot
```
### Docker
Подготовлен Dockerfile и docker-compose.yml для запуска бота в контейнере. 
В Dockerfile необходимо вписать в переменную окружения TOKEN ваш токен бота.

Далее достаточно собрать образ и запустить его командой:
```commandline
docker compose up -d
```