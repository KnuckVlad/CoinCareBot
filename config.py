# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# Working with mongoDB
DATABASE_URI = 'localhost'
DATABASE_PORT = 27015
DATABASE_COLLECTION_NAME = 'temp'
DATABASE_CONNECT_OPTIONS = {}

#Define telegram bot configs
TOKEN = '556841640:AAGbmKHZEe2henJOZ71IfYPfcJLiCRjLHJA'

