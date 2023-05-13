FROM python:3.8-slim

RUN apt-get update
RUN apt-get install -y

WORKDIR /root/src

RUN python -m pip install --upgrade pip
RUN python -m pip install keras numpy pandas Pillow streamlit tensorflow