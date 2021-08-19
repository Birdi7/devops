FROM python:3.7

LABEL name "devops-1"
LABEL version "1"


WORKDIR /app
ENV TZ 'Europe/Moscow'

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT [ "bash", "/app/etc/entrypoint.sh" ]
CMD ["flask", "RUN"]
