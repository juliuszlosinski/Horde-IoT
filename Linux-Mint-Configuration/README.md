## You need to change the permission of the shell/file script (chmod 777 file_name) before executing!

### 1. Docker on LinuX Mint installation.

```sh
chmod 777 DockerEngine-Installer/docker-installer-mint-2.sh
DockerEngine-Installer/docker-installer-mint-2.sh
```

### 2. InfluxDB container creation.

```sh
cd InfluxDB-Container
chmod 777 influxdb-container-creator.sh
./influxdb-container-creator.sh
cd ..
```

### 3. Python Flask Backend creation.

```sh
cd Python-Backend-Container
chmod 777 flask-influxdb-backend-container-creator.sh
./flask-influxdb-backend-container-creator.sh
cd ..
```

### 4. InfluxDB-Backend Docker Network creation.

```sh
chmod 777 DockerNetwork-Creator/influxdb-backend-network-creator.sh
DockerNetwork-Creator/influxdb-backend-network-creator.sh
```

File "influxdb_config.json" inside of Python-Backend-Container:

```json
{
	"token": "WFP9nF-1oO7rYnq2vV-_pC3bKWNEZZd9XRN_tpYlBZzxgx35f3hNRLIb8C_6DmTB0Weq9HpCViqOu0FGqYxMvg==",
	"org": "horde-org",
	"url": "http://CURRENT_IP_ADDRESS_OF_INFLUXD_CONTAINER:8086",
	"bucket": "horde-bucket"
}
```
### * Available simulation of ESP8266 x 4 in "ESP8266-Simulation" folder:

File "ESP8266_0X_simulation.py" inside of Python-Backend-Container/ESP8266-Simulation:

```py
import json
import requests
import random
import time

f = open("flask_config.json")
influxdb_config = json.load(f)
url = influxdb_config["url"]

while(True):
    device_id = "ESP8266-01"
    temperature = random.randint(0, 100)
    humidity = random.randint(0, 100)
    print(f"Device-id: {device_id}, Temperature: {temperature}, Humidity: {humidity}")
    response = requests.post(f"{url}/device-measurement", json=
                  {"device-id":device_id, 
                   "temperature":temperature, 
                   "humidity":humidity}
                   )
    print(response)
    time.sleep(1)
```
File  "flask_config.json" inside Python-Backend-Container/ESP8266-Simulation:

```json
{
	"url": "CURRENT_IP_ADDRESS_OF_INFLUXD_CONTAINER:7007"
}
```

![Screenshot](Flask-InfluxDB-Docker-Working.png)
![Screenshot](InfluxDB-Charts.png)
![Screenshot](ESP8266-Simulation.png)