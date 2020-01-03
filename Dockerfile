FROM python:3.7-slim as base
WORKDIR /api
ENV PYTHONUNBUFFERED True
COPY ./src .
COPY requirements.txt .
RUN pip install -r requirements.txt

