FROM python:latest

#RUN apt upgrade
#RUN apt update

#RUN apt install -y python3

WORKDIR /app

#RUN python -m venv venv
#RUN source venv/bin/activate.sh
RUN python -m pip install sqlmodel
RUN python -m pip install fastapi

CMD ["python", "main.py"]
