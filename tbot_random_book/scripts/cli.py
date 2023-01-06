#!/usr/bin/env python3
from tbot_random_book.bot import start_bot
from dotenv import find_dotenv, load_dotenv
from os import getenv


def main():
    print('Start...')
    load_dotenv(find_dotenv())
    token = getenv('TOKEN')
    url = getenv('URL')
    start_bot(token, url)


if __name__ == '__main__':
    main()
