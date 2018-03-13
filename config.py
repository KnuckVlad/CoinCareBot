# Statement for enabling the development environment
DEBUG = True

#web-server configs
HOST_URI = 'localhost'
HOST_PORT = 8443

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# Working with mongoDB
DATABASE_NAME = 'NONE'
DATABASE_COLLECTION_NAME = 'temp'
DATABASE_CONNECT_OPTIONS = {}

#GET THE TOKEN
import private_config
TOKEN = private_config.TOKEN


