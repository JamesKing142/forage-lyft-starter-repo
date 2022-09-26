from array import array
from tire.tire_factory import Tire_factory

class Carrigan(Tire_factory):
    def __init__(self, tire_sensor):
        self.tire_sensor = tire_sensor

    def need_service(self):
        if not self.tire_sensor:
            return False

        max_wear_value = max(self.tire_sensor)

        if max_wear_value >= 0.9:
            return True
        else:
            return False
