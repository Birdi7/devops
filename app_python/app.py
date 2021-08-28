from flask import Flask

from app_python.get_content import get_content

app = Flask(__name__)


@app.route("/")
def hello_world():
    return get_content()
