#!/bin/bash
sudo apt-get update
sudo apt-get install -y python-pip python-dev build-essential libblas-dev libblas3gf liblapack-dev liblapack3gf gfortran gfortran-4.6 pkg-config libpng12-dev libfreetype6-dev
sudo pip install --upgrade pip distribute
sudo pip install -r requirements.txt
cd /vagrant/tools && python startup.py