import io
import logging
import platform
from functools import lru_cache as cached
from fastapi import HTTPException

from .raspberry.base import Raspberry


logger = logging.getLogger(__name__)

class VendorFactory:
    @staticmethod
    def get_vendor():
        if test_raspberry():
            return Raspberry
        elif test_windows():
            return Raspberry

        raise HTTPException(
            status_code=404,
            detail="Unknown vendor. Must be one of: raspberry, arduino, windows",
        )

@cached
def test_raspberry():
    try:
        logging.debug("Testing platform for raspberry")
        with io.open('/sys/firmware/devicetree/base/model', 'r') as m:
            if 'raspberry pi' in m.read().lower():
                return True
    except Exception:
        pass
    return False


@cached
def test_windows():
    return platform.system() == "Windows"
