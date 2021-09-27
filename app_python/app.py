import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pathlib import Path

from flask import Flask

from .utils.get_content import get_content

LOG_FILE_NAME = "/tmp/app_python.log"
logging.basicConfig(filename=LOG_FILE_NAME, level=logging.DEBUG)
logger = logging.getLogger()

# rotate our logging file
logger.addHandler(RotatingFileHandler(filename=LOG_FILE_NAME, maxBytes=1000, backupCount=5))

app = Flask(__name__)


DATA_PATH = Path("/opt/data/visits.json")


@app.route("/")
def hello_world():
    logging.debug("hello world!")
    if not DATA_PATH.parent.exists():
        DATA_PATH.parent.mkdir()

    DATA_PATH.touch(exist_ok=True)
    DATA_PATH.write_text("{old}\nVisited at {now}".format(old=DATA_PATH.read_text(), now=datetime.now()))
    return get_content()


@app.route("/visits/")
def visits():
    val = "No visits!"
    if DATA_PATH.exists():
        val = DATA_PATH.read_text()
    boilerplate = """
    <html>
        <body>
        you are at /visits

        <h3> content </h3>
        <pre>{val}</pre>
        </body>
    </html>"""
    return boilerplate.format(val=val)
