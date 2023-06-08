import json
import influxdb_client
import socket
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from flask_swagger import swagger
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
        self.hostname = str(socket.gethostname(config_json["hostname"]))
        self.port = config_json["port"]
        self.url = f"{self.hostname}:{self.port}"
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
            .tag("device-id", device_id)            # tag
            .field("temperature", temperature)      # key-value     
            .field("humidity", humidity)            # key-value
        )
        self.write_api.write(
            bucket=self.bucket, org=self.org, record=point)
        
    """
    Printing all device measurements.
    """
    def print_all_device_measurement(self)->str:
        query = 'from(bucket:"horde-bucket")\
                |> range(start: -60m)\
                |> filter(fn:(r) => r._measurement == "device-measurement")'    # Name of table/ measurement.
        result = self.query_api.query(query=query, org=self.org)
        results = []
        for table in result:
            for record in table.records:
                json_data = {
                        "Type of measurement": record.get_field(),
                        "Value" : record.get_value(),
                        "Device-id": record.values["device-id"],
                        "Time": record.get_time()
                    }
                results.append(json_data)
        print(results)
        return results

influxdb_handler = InfluxDB_handler()

app = Flask(__name__)

"""
Getting default response.
"""
@app.route("/", methods=["GET"])
@app.route("/api", methods=["GET"])
def default_page():
    return "Flask-InfluxDB Backend is working!", 204

"""
Getting all measurements.
"""
@app.route("/api/device-measurement", methods=["GET"])
def print_measurement():
    result = influxdb_handler.print_all_device_measurement()
    return result


"""
Adding measurement.
"""
@app.route("/api/device-measurement", methods=["POST"])
def add_measurement():
    data = request.get_json()
    print(data)
    try:
        device_id = str(data["device-id"])
        temperature = float(data["temperature"])
        humidity = float(data["humidity"])
    except:
        return 'Wrong data!', 206
    
    influxdb_handler.write_device_measurement(
        device_id=device_id,
        temperature=temperature,
        humidity=humidity
    )
    return '', 204

# Starting the Flask REST API application.
if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=7007)