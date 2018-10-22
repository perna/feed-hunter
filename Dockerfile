FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  curl wget vim \
  debconf-utils 

RUN apt-get install -y --no-install-recommends \
    software-properties-common \
    build-essential libssl-dev libffi-dev

RUN apt-get install python -y

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py

RUN apt-get install python-dev -y

RUN pip install requests

RUN pip install scrapy