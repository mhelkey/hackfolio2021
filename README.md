- [Overview](#overview)
- [Demo-Screenshots](#demo)
- [Tech-Stack](#tech-stack)
- [Docker-Info](#docker)
- [Building-and-Testing](#building-and-testing)


#
# Overview
#### This is my project for the 2021 Appfolio Hackathon, and it is a Python web app to detect faces in an image, and draw a hat with the Appfolio name on the heads of detected faces.
####
#### It uses a trained OpenCV Haar Cascade face classifier to identify where faces are in a photo, and uses OpenCV's rectangle and text tools to draw a rudimentary hat on top of the faces.
####  
#### The project is locally hosted on a Flask webserver inside of a Docker container, which also contains the OpenCV libraries for face detection, and matplotlib libraries for image display and matrix manipulation

#
# Demo
### Home page
![Home PAge](/images/home.png)
### Choose a photo to upload
![People](/images/people.jpg)
### Upload photo of people
![Choose File](/images/choose_file.png)
### Submit the photo to webserver, and enjoy the (very rudimentary) hats and facial detection!!!
![GitHub Logo](/images/submit_file.png)
## 
# 
# Tech Stack
#### OpenCV and Python docker image taken from jjanzic/docker-python3-opencv:opencv-4.1.0.
#### Added Flask and MatPlotLib libraries to image, creating a new Docker image
#### Added trained classifier from OpenCV
#### Wrote program to detect faces from images, and draw hats on heads
#### Packaged everything into a webserver

#
# Docker 
## Docker Project Repo
https://hub.docker.com/repository/docker/mhelkeyappfolio/hackfolio2021-face-app/
## Most Recent Docker Image for project
mhelkeyappfolio/hackfolio2021-face-app:alpha-0.1.0


#
# Building and Testing
## Test Face_App for yourself!
#### Install docker (No need to clone this repo at all through the magic of docker!!)
https://docs.docker.com/get-docker/
#### Boot up project docker container
```shellscript
docker run --name opencv -p 42069:42069 -td mhelkeyappfolio/hackfolio2021-face-app:alpha-0.1.0
```
#### Run a bash instance inside the docker container
```
docker exec -it opencv bash
```
#### Inside the bash instance in the docker container, leave this command running
```
python main.py
```
#### Now go to your browser, and go to http://localhost:42069/ and upload a photo and test this project out for yourself!
