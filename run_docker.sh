#!/bin/bash

# Define the name of the image
IMAGE_NAME="proxy-server"

# Define the port number
HOST_PORT=${HOST_PORT:-8080}
CONTAINER_PORT=8080


DESTINATION_URL=$(printenv DESTINATION_URL)

echo "Running Docker container from image $IMAGE_NAME"
echo "Docker container is running on port $HOST_PORT"

# Run the container
docker run -p $HOST_PORT:$CONTAINER_PORT -e DESTINATION_URL=$DESTINATION_URL $IMAGE_NAME
