#!/bin/bash

# Define the name of the image
IMAGE_NAME="proxy-server"

echo "Building Docker image named $IMAGE_NAME"

# Build the image
docker build -t $IMAGE_NAME .

echo "Docker image $IMAGE_NAME built successfully"
