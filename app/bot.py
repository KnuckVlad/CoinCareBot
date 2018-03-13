from config import TOKEN, HOST_PORT, HOST_URI
from . import bot


def echo(update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!"
                                                          "Why You cut your hair?"
                                                          "Dyed it back!")


def set_webhook():
    bot.setWebhook(webhook_url='https://%s:%s/%s' % (HOST_URI, HOST_PORT, TOKEN),)
                  # certificate=open(CERT, 'rb'))
