############################################################
# Dockerfile to build DEV environment.
# Project should be mounted on /opt/app
#
# Based on Ubuntu Python 2.7
############################################################

# Set the base image to Ubuntu
FROM python:2.7

MAINTAINER cgarciaarano@gmail.com

# Update the repository sources list
RUN apt-get update -y && apt-get install -y libblas3gf liblapack3gf gfortran pkg-config

# Add requirements
COPY requirements.txt /opt/app/

WORKDIR /opt/app

# Install Python packages and system build dependencies
RUN apt-get install -y build-essential libblas-dev liblapack-dev && \
	pip install -r requirements.txt && \
	apt-get remove --purge -y build-essential libblas-dev liblapack-dev && \
	rm -rf /var/cache/apt/*

COPY . /opt/app
