#! /bin/bash

mkdir flask_docker
pip install Flask
pip install influxdb-client
pip freeze > requirements.txt
pip install -r requirements.txt
docker image build -t flask_docker .
docker run -p 5000:5000 -d flask_docker