# Import flask and template operators
from flask import Flask, render_template, request
import logging
import telegram
from pymongo import MongoClient
import config
import logging
from telegram.ext import Updater

#Define logging section
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Define the WSGI application object
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Creating bot
bot = telegram.Bot(token=config.TOKEN)
botName = "Bot Name"  # Without @
## updater instance
updater = Updater(token=config.TOKEN)
##dispatcher instance
dispatcher = updater.dispatcher


# Define MongoDB entities
client = MongoClient(config.HOST_URI, config.HOST_PORT)
# Define database
db = client['your_database']
# music = db[collection_name]

