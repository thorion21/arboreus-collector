import utils
from gpiozero import CPUTemperature

from core.domain import Domain


class Sensors(Domain):
    def __init__(self, runner):
        self.runner = runner

    @property
    def cpu_temp(self):
        try:
            return round(CPUTemperature().temperature, 2)
        except Exception as e:
            return "temp not available"
        
    @property
    def temperature(self):
        try:
            result = self.runner.collect('dht22')
        except Exception:
            return None
        
        return result['temperature']
    
    @property
    def humidity(self):
        try:
            result = self.runner.collect('dht22')
        except Exception:
            return None
        
        return result['humidity']

    def dump(self):
        return utils.dump(self)
