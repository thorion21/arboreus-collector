from core.hardware.adafruit.dht22 import DHT22


class SensorFactory:
    @staticmethod
    def get_sensor(name):
        opts = {
            'dht22': DHT22,
        }

        if name not in opts:
            return

        return opts.get(name)()
