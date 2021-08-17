FROM python:3.7

WORKDIR /app
ENV TZ 'Europe/Moscow'

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/app_python
ENTRYPOINT [ "bash", "/app/etc/entrypoint.sh" ]
