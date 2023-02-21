FROM python:3.8-slim

RUN apt-get update
RUN apt-get install -y

RUN mkdir -p /root/src

WORKDIR /root/src

RUN python -m pip install --upgrade pip
RUN python -m pip install autogluon autokeras FLAML jupyterlab ipywidgets numpy pandas