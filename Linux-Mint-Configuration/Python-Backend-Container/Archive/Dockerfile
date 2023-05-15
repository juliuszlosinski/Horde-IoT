FROM python:3-alpine

# 1. Creating app directory.
WORKDIR /app

# 2. Installing Flask package.
RUN pip install flask

# 3. Installing Influxdb-Client package.
RUN pip install influxdb-client

# 4. Copying all files to docker image.
COPY . .

# 5. Exposing backend port.
EXPOSE 4500