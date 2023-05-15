import json
import requests
import random
import time

f = open("flask_config.json")
influxdb_config = json.load(f)
url = influxdb_config["url"]

while(True):
    device_id = "ESP8266-04"
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