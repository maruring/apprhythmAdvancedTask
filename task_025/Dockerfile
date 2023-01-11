
FROM python:3.8-slim

RUN apt-get update
RUN apt-get install -y

RUN mkdir -p /root/src

COPY ./codes/ /root/src/codes/
WORKDIR /root/src

RUN python -m pip install --upgrade pip
RUN python -m pip install jupyterlab ipywidgets numpy pandas scikit-learn