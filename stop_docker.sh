#!/bin/bash

# Define the name of the image
IMAGE_NAME="proxy-server"

# Stop the Docker container
echo "Stopping the Docker container: $IMAGE_NAME"
docker stop $IMAGE_NAME

# Remove the Docker container
echo "Removing the Docker container: $IMAGE_NAME"
docker rm $IMAGE_NAME
