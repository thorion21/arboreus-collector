from fastapi import FastAPI

from core.types import DomainType
from core.vendor_factory import VendorFactory

from core.runner import Runner
from core.hardware.adafruit.dht22 import DHT22


def bootstrap(runner):
    runner.register_routine('dht22', DHT22())
    return runner


runner = bootstrap(Runner())
app = FastAPI()


@app.get("/system")
async def system():
    return VendorFactory.get_vendor().collect(domain=DomainType.System, runner=runner)


@app.get("/sensors")
async def sensors():
    return VendorFactory.get_vendor().collect(domain=DomainType.Sensors, runner=runner)


@app.get("/medium")
async def medium():
    return VendorFactory.get_vendor().collect(domain=DomainType.Medium, runner=runner)


@app.get("/all")
async def all():
    return VendorFactory.get_vendor().collect(domain=DomainType.All, runner=runner)
