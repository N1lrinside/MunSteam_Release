FROM python:3.12

WORKDIR /djangoProject

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY . .
