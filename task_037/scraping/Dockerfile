FROM python:3.8-slim

RUN apt-get update
RUN apt-get install -y

WORKDIR /root/src

RUN python -m pip install --upgrade pip
RUN python -m pip install jupyterlab
RUN python -m pip install numpy
RUN python -m pip install pandas
RUN python -m pip install requests
RUN python -m pip install beautifulsoup4
RUN python -m pip install tqdm
RUN python -m pip install lxml