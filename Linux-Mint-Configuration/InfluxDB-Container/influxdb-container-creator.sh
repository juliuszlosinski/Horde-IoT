#! /bin/bash

echo "Updating..."
apt-get update -y
echo "Finished updating!"

echo "Install docker compose..."
apt-get install docker.io -y && apt-get install docker-compose -y
echo "Finished installing docker compose!"

echo "Creating Horde-influxdb container..."
docker-compose up
echo "Horde-Influxdb container created!"
