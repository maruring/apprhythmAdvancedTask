
FROM python:3.8-slim

RUN apt-get update
RUN apt-get install -y

RUN mkdir -p /root/src

COPY ./codes/ /root/src/codes/
COPY ./model/ /root/src/model/
WORKDIR /root/src

RUN python -m pip install --upgrade pip
RUN python -m pip install numpy torch torchvision torchaudio pillow streamlit