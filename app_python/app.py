import logging
from logging.handlers import RotatingFileHandler

from flask import Flask

from .utils.get_content import get_content

LOG_FILE_NAME = "/tmp/app_python.log"
logging.basicConfig(filename=LOG_FILE_NAME, level=logging.DEBUG)
logger = logging.getLogger()

# rotate our logging file
logger.addHandler(RotatingFileHandler(filename=LOG_FILE_NAME, maxBytes=1000, backupCount=5))

app = Flask(__name__)


@app.route("/")
def hello_world():
    logging.debug("hello world!")
    return get_content()
