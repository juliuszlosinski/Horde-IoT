#! /bin/bash

echo "1. Building Flask-InfluxDB Image..."
docker build -t flask-influxdb-app .
echo "1. Flask-InfluxDB image is created!"

echo "2. Starting Flask-InfluxDB backend container..."
docker run -it -p 4500:4500 -d --name python_backend flask-influxdb-app
echo "2. Flask-InfluxDB backend container started!"

echo "3. Starting Flask-InfluxDB python backend..."
docker exec -it python_backend flask --app flask_influxdb_backend run -p 4500
echo "4. Flask-InfluxDB python backend finished working!"