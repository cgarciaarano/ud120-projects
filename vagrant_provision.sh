#!/bin/bash
sudo apt-get update
sudo apt-get install -y python-pip python-dev build-essential libblas-dev libblas3gf liblapack-dev liblapack3gf gfortran gfortran-4.6 pkg-config
sudo pip install -r requirements.txt
cd /vagrant/tools && python startup.py
