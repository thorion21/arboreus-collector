import time
import board
import adafruit_dht as dht
from datetime import datetime, timedelta

from threading import Lock
from core.routine import Routine


class DHT22(Routine):
    def __init__(self, read_interval_secs=2, timeout=10):
        self.device = dht.DHT22(board.D4)
        self.read_interval_secs = read_interval_secs
        self.timeout = timeout

        self.lock = Lock()
        self.temperature = None
        self.humidity = None

    def loop(self):
        while True:
            try:
                with self.lock:
                    self.temperature = self.device.temperature
                    self.humidity = self.device.humidity
            except Exception:
                pass

            time.sleep(self.read_interval_secs)

    def collect(self):
        end = datetime.now() + timedelta(seconds=self.timeout)
        while datetime.now() < end:
            with self.lock:
                if self.temperature and self.humidity:
                    return {
                        'temperature': self.temperature,
                        'humidity': self.humidity,
                    }

            time.sleep(1)

        raise ValueError("No reading available")
