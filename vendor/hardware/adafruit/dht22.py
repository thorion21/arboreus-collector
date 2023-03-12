# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_dht as dht
# from utils import DATE_FORMAT
from datetime import datetime


DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class DHT22:
    def __init__(self, data_pin=board.D4, read_interval=3.0):
        self.device = dht.DHT22(data_pin)
        self.read_interval = read_interval
        
        self._reading_thread = Thread(target=self._loop)
        self._reading_thread.start()

        self._temperature = None
        self._humidity = None

    def get_temperature(self):

        while not self._temperature:
            time.sleep(1)

        return self._temperature
    
    def get_humidity(self):

        while not self._humidity:
            time.sleep(1)

        return self._humidity

    def _loop(self):
        while True:
            try:
                self._temperature = self.device.temperature
                self._humidity = self.device.humidity
            except Exception:
                pass

            time.sleep(self.read_interval)

from threading import Thread
sensor = DHT22()


counter = 0

while counter < 100:
    print(f"Temperature: {sensor.get_temperature()} C\tHumidity: {sensor.get_humidity()}%")

    time.sleep(5)
    counter += 1

print('end counter')