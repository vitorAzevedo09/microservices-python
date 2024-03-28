#!/bin/bash

# Check if Docker is installed
if ! command -v docker &> /dev/null
then
    echo "Docker is not installed. Please install Docker to proceed."
    exit 1
fi

# Check if script is run with sudo
if [ "$(id -u)" -ne 0 ]; then
    echo "Please run this script with sudo."
    exit 1
fi

# Build the Docker image
sudo docker buildx build . -t microservice/auth
