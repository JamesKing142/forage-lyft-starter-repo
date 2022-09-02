from engine.model.car_factory import car_factory
from battery import nubbin_battery, spindler_battery

class Battery_factory(car_factory):
    def check_battery(self, name):
        if name == "nubbin":
            return nubbin_battery.Nubbin_battery()
        elif name == " spindler":
            return spindler_battery.Spindler_battery()
