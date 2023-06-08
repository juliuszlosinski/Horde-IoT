#! /bin/sh

echo "1. Composing/ creating Flask-InfluxDB container..."
docker-compose build --no-cache
echo "1. Flask-InfluxDB container is created!"

echo "2. Starting up container..."
docker-compose up
echo "2. Container finished working!"