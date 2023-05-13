#! /bin/bash

echo "1. Updating..."
apt-get update -y
echo "1. Finished updating!"

echo "2. Installing docker compose..."
apt-get install docker.io -y && apt-get install docker-compose -y
echo "2. Finished installing docker compose!"

echo "3. Creating Horde-influxdb container..."
docker-compose up
echo "3. Horde-Influxdb container created!"
