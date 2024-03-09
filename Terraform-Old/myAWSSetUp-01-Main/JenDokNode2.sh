#!/bin/bash
##Install Docker and Java-for-JenkinsNode
sudo hostnamectl set-hostname JenDokNode2
sudo apt update -y
sudo apt install default-jdk -y
sudo apt update -y
sudo apt-get install docker.io -y
sudo usermod -aG docker ubuntu
sudo usermod -aG docker jenkins
sudo systemctl daemon-reload
sudo systemctl restart docker
#sudo docker info