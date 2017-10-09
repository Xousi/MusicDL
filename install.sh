#!/bin/bash

sudo apt-get install python-pip python-dev build-essential libav-tools;
sudo pip install --upgrade pip;
sudo pip install --upgrade virtualenv;

pip install youtube-dl BeautifulSoup4

cd musicdl/
python3 setup.py
