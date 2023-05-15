#! /bin/bash

echo "1. Building Flask-InfluxDB Image..."
docker build -t flask-influxdb-app .
echo "1. Flask-InfluxDB image is created!"

echo "2. Starting Flask-InfluxDB backend container..."
docker run -it -p 4000:4000 -d --name python_backend flask-influxdb-app
echo "2. Flask-InfluxDB backend container started!"