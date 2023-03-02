from fastapi import FastAPI

from vendor.types import DomainType
from vendor.vendor_factory import VendorFactory


app = FastAPI()


@app.get("/system")
async def system():
    return VendorFactory.get_vendor().collect(domain=DomainType.System)


@app.get("/sensors")
async def sensors():
    return VendorFactory.get_vendor().collect(domain=DomainType.Sensors)


@app.get("/medium")
async def medium():
    return VendorFactory.get_vendor().collect(domain=DomainType.Medium)


@app.get("/all")
async def all():
    return VendorFactory.get_vendor().collect(domain=DomainType.All)
