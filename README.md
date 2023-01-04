# Случайная книга

Простой телеграм бот, который присылает случайную книгу по запросу.

Книги беру здесь: https://www.livelib.ru/book/random

Использую [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI), 
[BeautifulSoup](https://pypi.org/project/beautifulsoup4/) и 
[requests](https://pypi.org/project/requests/). 

Протестировать можно [здесь](https://t.me/RandomBookBot).

## Запуск

Для сборки используется poetry ver. 1.2.1

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