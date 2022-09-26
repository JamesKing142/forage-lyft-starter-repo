from tire.tire_factory import Tire_factory

class Octoprime(Tire_factory):
    def __init__(self, tire_sensor):
        self.tire_sensor = tire_sensor

    def need_service(self):
        if not self.tire_sensor:
            return False
            
        total_wear_value = sum(self.tire_sensor)
        if total_wear_value >= 3:
            return True
        else:
            return False