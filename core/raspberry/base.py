from functools import reduce
from datetime import datetime
from fastapi import HTTPException

from utils import *
from .system import System
from .sensors import Sensors
from core.types import DomainType
from core.vendor import Vendor


class Raspberry(Vendor):
    @staticmethod
    def collect(domain, runner, config):
        opts = {
            DomainType.System: System,
            DomainType.Sensors: Sensors,
            DomainType.All: [System, Sensors],
        }

        filtered_domain = opts.get(domain, DomainType.Unknown)

        if filtered_domain is DomainType.Unknown:
            raise HTTPException(
                status_code=404,
                detail=f"Unknown domain. Must be one of: {present_domains(opts)}",
            )

        if isinstance(filtered_domain, list):
            domains = reduce(
                lambda x, y: x | y, [domain(runner, config).dump() for domain in filtered_domain]
            )
        else:
            domains = filtered_domain(runner, config).dump()

        return {
            "vendor": "raspberry",
            "domains": domains,
            "location": config['general']['location'],
            "local_time": datetime.utcnow().strftime(DATE_FORMAT),
        }
