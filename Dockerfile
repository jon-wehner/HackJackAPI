# syntax=docker/dockerfile:1

FROM python:3.8

ENV FLASK_APP=app
ENV FLASK_ENVIRONMENT=production

EXPOSE 8080

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn app:app