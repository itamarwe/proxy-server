!/bin/bash

# Define the name of the image
IMAGE_NAME="your-image-name"

# Define the port number
HOST_PORT=8080
CONTAINER_PORT=8080

echo "Running Docker container from image $IMAGE_NAME"

# Run the container
docker run -p $HOST_PORT:$CONTAINER_PORT $IMAGE_NAME

echo "Docker container is running on port $HOST_PORT"
