face_app docker image based on jjanzic/docker-python3-opencv:opencv-4.1.0 with added matplotlib dependencies.
Added trained classifier and program to detect faces from images


## Docker Images

### Docker Image for project

mhelkeyappfolio/hackfolio2021-face-app:alpha-0.1.0

## Test Face_App for yourself!
#### Install docker
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
