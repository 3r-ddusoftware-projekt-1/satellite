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
                "temperature": self.bmp_sensor.temperature,
                "timestamp": 0
            },
        )

        return datapoints

