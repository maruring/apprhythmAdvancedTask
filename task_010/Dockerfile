FROM ubuntu:20.04
RUN apt-get update
RUN apt-get update && apt-get install -y --no-install-recommends wget build-essential libreadline-dev \
libncursesw5-dev libssl-dev libsqlite3-dev libgdbm-dev libbz2-dev liblzma-dev zlib1g-dev uuid-dev libffi-dev libdb-dev

#任意バージョンのpython install
RUN wget --no-check-certificate https://www.python.org/ftp/python/3.7.11/Python-3.7.11.tgz \
&& tar -xf Python-3.7.11.tgz \
&& cd Python-3.7.11 \
&& ./configure --enable-optimizations\
&& make \
&& make install

#サイズ削減のため不要なものは削除
RUN apt-get autoremove -y

#必要なpythonパッケージをpipでインストール
RUN pip3 install --upgrade pip

RUN mkdir -p /root/src
COPY app.py /root/src
COPY pred.py /root/src
COPY original_model.py /root/src
RUN mkdir -p /root/src/models
COPY models/ /root/src/models
WORKDIR /root/src

RUN pip install torch torchvision torchaudio pillow streamlit