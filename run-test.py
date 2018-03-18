# this module use polling technique for testing application
# Run a test server.
import app.bot
from app.flask import flask_app
import flask
from config import HOST_PORT, HOST_URI
# using app.bot.setWebhook() if we have external web server
# on localhost using polling()
print(flask_app.logger_name)
flask_app.run(
        host=HOST_URI,
        port=HOST_PORT,
        ssl_context='adhoc',
        debug=True
        )
