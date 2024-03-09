#!/bin/bash
##Install Docker
sudo apt update -y
sudo apt-get install docker.io -y
sudo usermod -aG docker ubuntu
sudo usermod -aG docker jenkins
sudo systemctl daemon-reload
sudo systemctl restart docker
sudo docker info