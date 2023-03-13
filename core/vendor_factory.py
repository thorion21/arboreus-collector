import platform
from fastapi import HTTPException

from .raspberry.base import Raspberry


class VendorFactory:
    @staticmethod
    def get_vendor():
        if test_raspberry():
            return Raspberry
        elif test_arduino():
            return None
        elif test_windows():
            return Raspberry

        raise HTTPException(
            status_code=404,
            detail="Unknown vendor. Must be one of: raspberry, arduino, windows",
        )


def test_raspberry():
    return platform.system() == "Linux" and "raspberry" in platform.node()


def test_arduino():
    return platform.system() == "Windows" and "Arduino" in platform.node()


def test_windows():
    return platform.system() == "Windows"
