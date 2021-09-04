from flask import Flask

from .utils.get_content import get_content

app = Flask(__name__)


@app.route("/")
def hello_world():
    return get_content()
