FROM python:latest

WORKDIR /app

RUN python -m pip install sqlmodel
RUN python -m pip install fastapi[standard]
