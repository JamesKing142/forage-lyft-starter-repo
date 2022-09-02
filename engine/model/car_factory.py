from engine.model import calliope, glissade, palindrome,rorschach,thovex
from car import Car

class car_factory(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, warning_light:bool):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_light = warning_light
    def create_car(self):
        if self.engine == "capulet" and self.battery == "spindler":
            return calliope.Calliope()
        elif self.engine == "willoughby" and  self.battery == "spindler":
            return glissade.Glissade()
        elif self.engine == "sternman" and self.battery == "spindler":
            return palindrome.Palindrome()
        elif self.engine == "willoughby" and self.battery == "nubbin": 
            return rorschach.Rorschach()
        elif self.engine == "capulet" and self.battery == "nubbin":
            return thovex.Thovex()
        else:
            return "Type D.N.E"