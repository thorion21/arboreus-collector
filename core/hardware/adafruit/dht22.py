import time
import board
import adafruit_dht as dht
from datetime import datetime, timedelta

from utils import DATE_FORMAT
from threading import Lock
from core.routine import Routine


class DHT22(Routine):
    # Use config file, not constructor arguments
    # Also for the data pin
    def __init__(self, read_interval_secs=2, timeout=10):
        self.device = dht.DHT22(board.D4)
        self.read_interval_secs = read_interval_secs
        self.timeout = timeout

        self.lock = Lock()
        self.temperature = None
        self.humidity = None
        self.last_reading = None

    def loop(self):
        while True:
            try:
                with self.lock:
                    self.temperature = self.device.temperature
                    self.humidity = self.device.humidity
                    self.last_reading = datetime.utcnow().strftime(DATE_FORMAT)
                    print('worked!')
            except Exception:
                print('General sensor exception')

            time.sleep(self.read_interval_secs)

    def collect(self):
        end = datetime.now() + timedelta(seconds=self.timeout)
        while datetime.now() < end:
            with self.lock:
                if self.temperature and self.humidity and self.last_reading:
                    return {
                        'temperature': self.temperature,
                        'humidity': self.humidity,
                        'last_reading': self.last_reading,
                    }

            time.sleep(1)

        raise ValueError("No reading available")
