# check docker version
docker --version

# pull the latest version of the docker image of mysql
docker pull mysql

# show the list of docker images
docker images

# pull mongo with version 4.4.6
docker pull mongo:4.4.6

# show the list of running containers
docker ps

# stop the running container
docker stop 48cf46e6a1b0
# start the container
docker start 48cf46e6a1b0

# run in detached mode (mysql)
docker run -d mysql

# docker remove container
docker rm 48cf46e6a1b0

# docker remove image
docker rmi mysql

# docker run with port binding
docker run -d -p 3306:3306 mysql

# docker run with the name 
docker run -d --name mysql -p 3306:3306 mysql

# show logs of the container based on the name
docker logs mysql

docker run -d  shashkist/docker-hello-test:1.1  # run the container in detached mode

docker attach 8371a64268af # attach to the container