from datetime import datetime

from pytz import timezone


def moscow_now() -> datetime:
    moscow_tz = timezone("Europe/Moscow")
    return datetime.now(moscow_tz)


def get_content() -> str:
    boilerplate = """
    <html>
        <body>
        {content} in moscow now!
        </body>
    </html>
    """
    info = moscow_now().strftime("%Y-%m-%d %H:%M:%S %Z%z")
    result = boilerplate.format(content=info)
    return result
