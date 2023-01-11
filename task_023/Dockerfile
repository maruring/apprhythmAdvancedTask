
FROM python:3.8-slim

RUN apt-get update
RUN apt-get install -y

RUN mkdir -p /root/src
RUN mkdir -p /root/src/models

COPY ./codes/ /root/src/codes/
COPY ./TRAIN/ /root/src/TRAIN/
COPY ./TEST/ /root/src/TEST/
WORKDIR /root/src

RUN python -m pip install --upgrade pip
RUN python -m pip install jupyterlab ipywidgets numpy pandas torch torchvision torchaudio pillow scikit-learn