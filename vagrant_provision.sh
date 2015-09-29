#!/bin/bash
sudo apt-get update
sudo apt-get install -y python-pip python-dev build-essential
sudo pip install scikit-learn nltk scipy numpy
cd /vagrant/tools
