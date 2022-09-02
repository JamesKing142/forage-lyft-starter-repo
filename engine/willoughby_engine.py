from abc import ABC
from engine_factory import Engine_factory

class CapuletEngine(Engine_factory):
    
    def engine_should_be_serviced(self):
        if self.current_mileage - self.last_service_mileage > 60000:
            return True
