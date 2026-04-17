from abc import ABC, abstractmethod

class Service(ABC):

    @abstractmethod
    def query(self, query: str):
        pass
