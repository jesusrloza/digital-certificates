#!/usr/bin/sh
sudo apt update -y && sudo apt upgrade -y

# CLI programs
sudo apt-get install openssl qrencode poppler-utils git neovim ranger curl tree -y
sudo apt-get install python3 python3-pip -y
sudo apt-get remove nano -y

# Pip config for Data Analysis
pip3 install -U pip psutil openpyxl
pip3 install -U numpy pandas scikit-learn matplotlib seaborn nltk beautifulsoup4
