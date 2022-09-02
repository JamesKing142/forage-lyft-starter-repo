from abc import ABC, abstractmethod
from datetime import datetime


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass
