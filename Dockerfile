FROM python:3.10.9-alpine3.17

ENV TOKEN=''\
    URL="https://www.livelib.ru/book/random"\
    POETRY_VERSION=1.3.1

RUN pip install "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.create false

WORKDIR /app

COPY . .

RUN poetry install --no-dev --no-interaction --no-ansi

CMD [ "poetry", "run", "bot" ]
