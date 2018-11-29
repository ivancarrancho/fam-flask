FROM python:3.6
RUN apt-get update
RUN easy_install -U pip
RUN pip install --upgrade pip
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
ADD ./app/requirements.txt /app/requirements.txt
RUN pip install grpcio
RUN pip install https://github.com/paulharter/fam/archive/2.0.5.tar.gz
RUN pip install -r requirements.txt
ADD ./app /app/