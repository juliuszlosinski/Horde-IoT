import json
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from flask import Flask, jsonify, request

class InfluxDB_handler:

    """
    Initialzing InfluxDB connection.
    """
    def __init__(self) -> None:
        f = open("influxdb_config.json")
        config_json = json.load(f)

        self.token = config_json["token"]
        self.org = config_json["org"]
        self.url = config_json["url"]
        self.bucket = config_json["bucket"]
        self.client = influxdb_client.InfluxDBClient(
            url=self.url, token=self.token, org=self.org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS) 
        self.query_api = self.client.query_api()
    """
    Writting device measurement.
    """
    def write_device_measurement(self, device_id:str, temperature:float, humidity:float)->None:
        point = (
            Point("device-measurement")
            .tag("device-id", device_id)
            .field("temperature", temperature)
            .field("humidity", humidity)
        )
        self.write_api.write(
            bucket=self.bucket, org="horde-org", record=point)
        
    """
    Printing all device measurements.
    """
    def print_all_device_measurement(self)->str:
        query = """from(bucket: "horde-bucket")
        |> range(start: -10m)"""
        tables = self.query_api.query(query, org="horde-org")
        results = ""
        for table in tables:
            for record in table.records:
                results += str(record)+"\n"
            results+="\n"
        return results

influxdb_handler = InfluxDB_handler()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def default_page():
    return "Flask-InfluxDB Backend is working!"

@app.route("/device-measurement", methods=["GET"])
def print_measurment():
    result = "Use POST method to add measurement!\n\n"
    result = influxdb_handler.print_all_device_measurement()
    return result

@app.route("/device-measurement", methods=["POST"])
def add_measurement():
    data = request.get_json()
    print(data)
    device_id = str(data["device-id"])
    temperature = float(data["temperature"])
    humidity = float(data["humidity"])

    influxdb_handler.write_device_measurement(
        device_id=device_id,
        temperature=temperature,
        humidity=humidity
    )
    return '', 204

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=7007)