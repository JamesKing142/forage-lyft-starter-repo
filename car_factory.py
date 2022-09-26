from engine import capulet_engine
from engine import willoughby_engine
from engine import sternman_engine
from battery import spindler_battery
from battery import nubbin_battery
from tire import carrigan_tire
from tire import octoprime_tire
from car import Car

class Car_factory:

    @staticmethod
    def create_calliope(last_service_date, current_mileage, last_service_mileage, tire_sensor):

        engine = capulet_engine.Capulet(current_mileage, last_service_mileage)
        battery = spindler_battery.Spindler(last_service_date)
        tire = carrigan_tire.Carrigan(tire_sensor)
        car = Car(engine, battery, tire)

        return car

    @staticmethod
    def create_glissade(last_service_date, current_mileage, last_service_mileage, tire_sensor):

        engine = willoughby_engine.Willoughby(current_mileage, last_service_mileage)
        battery = spindler_battery.Spindler(last_service_date)
        tire = octoprime_tire.Octoprime(tire_sensor)
        car = Car(engine, battery, tire)

        return car

    @staticmethod
    def create_palindrome(last_service_date, warning_light: bool, tire_sensor):

        engine = sternman_engine.Sternman(warning_light)
        battery = spindler_battery.Spindler(last_service_date)
        tire = carrigan_tire.Carrigan(tire_sensor)
        car = Car(engine, battery, tire)

        return car

    @staticmethod
    def create_rorschach(last_service_date, current_mileage, last_service_mileage, tire_sensor):

        engine = willoughby_engine.Willoughby(current_mileage, last_service_mileage)
        battery = nubbin_battery.Nubbin(last_service_date)
        tire = octoprime_tire.Octoprime(tire_sensor)
        car = Car(engine, battery, tire)

        return car

    @staticmethod
    def create_thovex(last_service_date, current_mileage, last_service_mileage, tire_sensor):

        engine = capulet_engine.Capulet(current_mileage, last_service_mileage)
        battery = nubbin_battery.Nubbin(last_service_date)
        tire = carrigan_tire.Carrigan(tire_sensor)
        car = Car(engine, battery, tire)

        return car