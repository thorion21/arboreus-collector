import logging
import configparser
from fastapi import FastAPI

from core.runner import Runner
from core.logger import configure
from core.types import DomainType
from core.vendor_factory import VendorFactory
from core.hardware.adafruit.dht22 import DHT22
from core.hardware.sensor_factory import SensorFactory

configure(logging.getLogger())


def parse_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config


def bootstrap(runner, config):
    for _, sensor_type in config["sensor.types"].items():
        if not sensor_type:
            raise ValueError("Incomplete sensors definitions")

        runner.register_routine(sensor_type, SensorFactory.get_sensor(sensor_type))

    return runner


config = parse_config("config.ini")
runner = bootstrap(Runner(), config)
app = FastAPI()


@app.get("/system")
async def system():
    return VendorFactory.get_vendor().collect(
        domain=DomainType.System, runner=runner, config=config
    )


@app.get("/sensors")
async def sensors():
    return VendorFactory.get_vendor().collect(
        domain=DomainType.Sensors, runner=runner, config=config
    )


@app.get("/medium")
async def medium():
    return VendorFactory.get_vendor().collect(
        domain=DomainType.Medium, runner=runner, config=config
    )


@app.get("/all")
async def all():
    return VendorFactory.get_vendor().collect(
        domain=DomainType.All, runner=runner, config=config
    )
