from abc import ABC, abstractmethod


class Vendor(ABC):
    @abstractmethod
    def collect():
        pass
