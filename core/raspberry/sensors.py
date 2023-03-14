import utils
from gpiozero import CPUTemperature

from core.domain import Domain


class Sensors(Domain):
    def __init__(self, runner, config):
        self.runner = runner
        self.config = config

    @property
    def cpu_temp(self):
        try:
            return round(CPUTemperature().temperature, 2)
        except Exception as e:
            return "temp not available"
        
    @property
    def temperature(self):
        try:
            sensor_type = self.config['sensor.types']['temperature']
            result = self.runner.collect(sensor_type)
        except Exception:
            return None
        
        return {
            'value': result['temperature'],
            'sensor_type': sensor_type,
        }
    
    @property
    def air_humidity(self):
        try:
            sensor_type = self.config['sensor.types']['air_humidity']
            result = self.runner.collect(sensor_type)
        except Exception:
            return None
        
        return {
            'value': result['humidity'],
            'sensor_type': sensor_type,
        }

    def dump(self):
        return utils.dump(self)
