import sys
import time

sys.path.append("..")
from lib.bmp180 import BMP180

class BMP:
    def __init__(self, i2c):
        self.bmp_sensor = BMP180(i2c)

    def poll(self):
        datapoints = []

        datapoints.append(
            {
                "quantity": "temperature",
                "value": self.bmp_sensor.temperature,
                "time": 0
            },
        )
        datapoints.append(
            {
                "quantity": "pressure",
                "value": self.bmp_sensor.pressure,
                "time": 0
            }
        )

        return datapoints

