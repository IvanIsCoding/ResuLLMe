# light weight python streamlit app into a docker container 
# https://hub.docker.com/r/continuumio/miniconda3

# base image
FROM ubuntu:22.04

# set working directory
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt packages.txt /app/

RUN apt update -y
RUN apt install -y python3-pip python-dev-is-python3 build-essential

# install dependencies
RUN pip install -r requirements.txt && \
    DEBIAN_FRONTEND=noninteractive xargs apt install -y < packages.txt

# copy the content of the local src directory to the working directory
COPY src .

# command to run on container start
CMD [ "streamlit", "run", "Main.py" ]

# # build the image
# docker build -t streamlit-app .

# # run the container
# docker run -p 8501:8501 streamlit-app

# # open the app in the browser
# http://localhost:8501