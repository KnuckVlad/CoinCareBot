from . import Flask, dispatcher, updater
from config import TOKEN
from .bot import start
from telegram.ext import CommandHandler

flask_app = Flask(__name__)

@flask_app.route('/')
def hello():
    return 'Hello World!'


@flask_app.route('/activate', methods=['POST', 'GET'])
def activate():
    print('START!')
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()
    return 'OK'


