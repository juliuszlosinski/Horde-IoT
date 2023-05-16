#! /bin/sh

echo "1. Creating InfluxDB-Backend Network..."
docker network create influxdb-backend-network
echo "1. InfluxDB-Backend Network is created!"

echo "2. Connecting InfluxDB to docker network..."
docker network connect influxdb-backend-network horde-influxdb
echo "2. InfluxDB is connected to InfluxDB-Backend Network!"

echo "3. Connecting Falsk Backend to docker network..."
docker network connect influxdb-backend-network horde-backend
echo "3. Flask Backend is connected to InfluxDB-Backend Network!"