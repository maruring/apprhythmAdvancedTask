FROM python:3.8-slim

RUN apt-get update
RUN apt-get install -y

RUN mkdir -p /root/src

COPY code.ipynb /root/src
COPY citrus.csv /root/src
COPY healthcare-dataset-stroke-data.csv /root/src
WORKDIR /root/src

RUN python -m pip install --upgrade pip
RUN python -m pip install jupyterlab
RUN python -m pip install autogluon
RUN python -m pip install ipywidgets