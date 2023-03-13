from abc import ABC, abstractmethod


class Routine(ABC):
    @abstractmethod
    def loop(self):
        pass

    @abstractmethod
    def collect(self):
        pass
