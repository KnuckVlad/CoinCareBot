from . import Flask, dispatcher, updater
from config import TOKEN
from .bot import start, echo
from telegram.ext import CommandHandler, MessageHandler, Filters

flask_app = Flask(__name__)

@flask_app.route('/')
def hello():
    return 'Hello World!'


@flask_app.route('/activate', methods=['POST', 'GET'])
def activate():
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)
    dispatcher.add_handler(start_handler)
    print('add Echo!')
    updater.start_polling()
    return 'OK'


