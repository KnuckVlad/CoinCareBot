# Import flask and template operators
from flask import Flask, render_template, request
import logging
import telegram
from pymongo import MongoClient
import config

# Define the WSGI application object
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

global bot
bot = telegram.Bot(token=config.TOKEN)
botName = "Bot Name"  # Without @

# Define MongoDB entities
client = MongoClient(config.DATABASE_URI, config.DATABASE_PORT)
# Define database
db = client['your_database']
# music = db[collection_name]