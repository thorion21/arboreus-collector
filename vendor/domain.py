from abc import ABC, abstractmethod


class Domain(ABC):
    @abstractmethod
    def dump():
        pass
