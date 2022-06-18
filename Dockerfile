FROM python:3.10

WORKDIR /home/test

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY server.py .
COPY config.py .
COPY app.db .
COPY boot.sh ./
RUN chmod +x boot.sh

ENV APPLICATION_PORT=5000

EXPOSE ${APPLICATION_PORT}
ENTRYPOINT ["./boot.sh"]
#set FLASK_APP=server.py
#flask run