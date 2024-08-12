FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /djangoProject

COPY requirements.txt /djangoProject/
RUN pip install -r requirements.txt
COPY . /djangoProject/

EXPOSE 8000
