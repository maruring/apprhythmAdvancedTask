
FROM python:3.8-slim

RUN apt-get update
RUN apt-get install -y

RUN mkdir -p /root/src
RUN mkdir -p /root/src/imgs
RUN mkdir -p /root/src/TEST

COPY ./codes/ /root/src/codes
WORKDIR /root/src

RUN python -m pip install --upgrade pip
RUN python -m pip install jupyterlab
RUN python -m pip install ipywidgets
RUN python -m pip install icrawler
RUN python -m pip install numpy
RUN python -m pip install pandas
RUN python -m pip install python-ulid