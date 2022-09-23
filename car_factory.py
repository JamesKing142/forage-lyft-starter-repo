from engine import capulet_engine
from engine import willoughby_engine
from engine import sternman_engine
from battery import spindler_battery
from battery import nubbin_battery
from car import Car

class Car_factory:

    @staticmethod
    def create_calliope(last_service_date, current_mileage, last_service_mileage):

        engine = capulet_engine.Capulet(current_mileage, last_service_mileage)
        battery = spindler_battery.Spindler(last_service_date)
        car = Car(engine, battery)

        return car

    @staticmethod
    def create_glissade(last_service_date, current_mileage, last_service_mileage):

        engine = willoughby_engine.Willoughby(current_mileage, last_service_mileage)
        battery = spindler_battery.Spindler(last_service_date)
        car = Car(engine, battery)

        return car

    @staticmethod
    def create_palindrome(last_service_date, warning_light: bool):

        engine = sternman_engine.Sternman(warning_light)
        battery = spindler_battery.Spindler(last_service_date)
        car = Car(engine, battery)

        return car

    @staticmethod
    def create_rorschach(last_service_date, current_mileage, last_service_mileage):

        engine = willoughby_engine.Willoughby(current_mileage, last_service_mileage)
        battery = nubbin_battery.Nubbin(last_service_date)
        car = Car(engine, battery)

        return car

    @staticmethod
    def create_thovex(last_service_date, current_mileage, last_service_mileage):

        engine = capulet_engine.Capulet(current_mileage, last_service_mileage)
        battery = nubbin_battery.Nubbin(last_service_date)
        car = Car(engine, battery)

        return car