from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from tbot_random_book.book import Book
import logging


START_MESSAGE = 'Нажмите кнопку или отправьте любой текст в чат, ' \
                'чтобы получить случайную книгу'
BUTTON = 'Случайная книга'


def start_bot(token: str, url: str):
    logging.basicConfig(
        level=logging.INFO,
        filename="bot_log.log",
        format="%(asctime)s %(levelname)s %(message)s"
    )

    bot = TeleBot(token)
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button = KeyboardButton(BUTTON)
    markup.add(button)

    @bot.message_handler(commands=['start', 'help'])
    def send_start_message(message):
        bot.send_message(
            chat_id=message.chat.id, text=START_MESSAGE, reply_markup=markup
        )

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        book = Book(url)

        log_mess = f'chat_id = {message.chat.id}, ' \
                   f'book = \n{book.description}\n'
        logging.info(log_mess)

        bot.send_photo(
            chat_id=message.chat.id,
            photo=book.image_link,
            caption=book.description,
            reply_markup=markup
        )

    bot.infinity_polling()
