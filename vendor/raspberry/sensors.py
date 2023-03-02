import utils

from vendor.domain import Domain

# from gpiozero import CPUTemperature


class Sensors(Domain):
    @property
    def cpu_temp(self):
        try:
            return CPUTemperature().temperature
        except Exception as e:
            return "temp not available"

    def dump(self):
        return utils.dump(self)
