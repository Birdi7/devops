from datetime import datetime

from flask import Flask
from pytz import timezone

app = Flask(__name__)


def moscow_now() -> datetime:
    moscow_tz = timezone("Europe/Moscow")
    return datetime.now(moscow_tz)


@app.route("/")
def hello_world():
    boilerplate = """
<html>
    <body>
    {content}
    </body>
</html>
"""
    info = moscow_now().strftime("%Y-%m-%d %H:%M:%S %Z%z")
    result = boilerplate.format(content=info)
    return result
