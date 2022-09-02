from abc import ABC
from engine_factory import Engine_factory

class SternmanEngine(Engine_factory):
    
    def engine_should_be_serviced(self):
        if self.warning_light:
            return True
