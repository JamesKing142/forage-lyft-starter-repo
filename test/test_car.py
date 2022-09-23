import sys
import os

# Getting the absolute path to the current directory
current_dir = os.path.dirname(os.path.realpath(__file__))

#Getting the path to  the parent directory
parent = os.path.dirname(current_dir)

#setting path
sys.path.append(parent)

#importing
import unittest
from car_factory import Car_factory
from utils import add_year_to_date, get_current_date

class Test_Calliope(unittest.TestCase):
    def test_engine_serviced(self):
        current_date = 0 
        last_service_date = 0
        current_mileage = 30001
        last_service_mileage = 0

        car = Car_factory.create_calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.need_service())
    
    def test_engine_not_serviced(self):
        current_date = 0
        last_service_date = 0
        current_mileage = 0
        last_service_mileage = 0

        car = Car_factory.create_calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.need_service())
    
    def test_battery_serviced(self):
        current_date = get_current_date()
        last_service_date = add_year_to_date(current_date, -3)
        current_mileage = 0
        last_service_mileage = 0

        car = Car_factory.create_calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.need_service())
    
    def test_battery_not_serviced(self):
        current_date = get_current_date()
        last_service_date = add_year_to_date(current_date, 0)
        current_mileage = 0
        last_service_mileage = 0

        car = Car_factory.create_calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.need_service())

class Test_Glissade(unittest.TestCase):
    def test_engine_serviced(self):
        current_date = 0
        last_service_date = 0
        current_mileage = 50001
        last_service_mileage = 0

        car = Car_factory.create_glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.need_service())

    def test_engine_not_serviced(self):
        current_date = 0
        last_service_date = 0
        current_mileage = 0
        last_service_mileage = 0

        car = Car_factory.create_glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.need_service())
    
    def test_battery_serviced(self):
        current_date = get_current_date()
        last_service_date = add_year_to_date(current_date, -3)
        current_mileage = 0
        last_service_mileage = 0

        car = Car_factory.create_glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.need_service())

    def test_battery_not_serviced(self):
        current_date = get_current_date()
        last_service_date = add_year_to_date(current_date, 0)
        current_mileage = 0
        last_service_mileage = 0

        car = Car_factory.create_glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.need_service())

class Test_Palindrome (unittest.TestCase):
    def test_engine_serviced(self):
        current_date = 0
        last_service_date = 0
        self_warning_light = True

        car = Car_factory.create_palindrome(last_service_date, self_warning_light)
        self.assertTrue(car.need_service())

    def test_engine_not_serviced(self):
        current_date = 0
        last_service_date = 0
        self_warning_light = False

        car  = Car_factory.create_palindrome(last_service_date, self_warning_light)
        self.assertFalse(car.need_service())

    def test_battery_serviced(self):
        current_date = get_current_date()
        last_service_date = add_year_to_date(current_date, -3)
        self_warning_light = False

        car = Car_factory.create_palindrome(last_service_date, self_warning_light)
        self.assertTrue(car.need_service())

    def test_battery_not_serviced(self):
        current_date = get_current_date()
        last_service_date = add_year_to_date(current_date, 0)
        self_warning_light = False

        car = Car_factory.create_palindrome(last_service_date, self_warning_light)
        self.assertFalse(car.need_service())  


class Test_Rorschach (unittest.TestCase):
    def test_engine_serviced(self):
        current_date = 0
        last_service_date = 0
        current_mileage = 50001
        last_service_mileage = 0

        car = Car_factory.create_rorschach(last_service_date, current_mileage,)
        self.assertTrue(car.need_service())
    
    def test_engine_not_serviced(self):
        current_date = 0
        last_service_date = 0
        current_mileage = 0
        last_service_mileage = 0

        car = Car_factory.create_rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.need_service())

    def test_battery_serviced(self):
        current_date = get_current_date()
        last_service_date = add_year_to_date(current_date, -5)
        current_mileage = 0
        last_service_mileage = 0

        car = Car_factory.create_rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.need_service())

    def test_battery_not_serviced(self):
        current_date = get_current_date()
        last_service_date = 0
        current_mileage = 0
        last_service_mileage = 0

        car = Car_factory.create_rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.need_service())

class Test_Thovex (unittest.TestCase):
    def test_engine_serviced(self):
        current_date = 0
        last_service_date = 0
        current_mileage = 300001
        last_service_mileage = 0

        car = Car_factory.create_thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.need_service())

    def test_engine_not_serviced(self):
        current_date = 0
        last_service_date = 0
        current_mileage = 0
        last_service_mileage = 0

        car = Car_factory.create_thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.need_service())

    def test_battery_serviced(self):
        current_date = get_current_date
        last_service_date = add_year_to_date(current_date, -5)
        current_mileage = 0
        last_service_mileage = 0

        car = Car_factory.create_thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.need_service())

    def test_battery_not_serviced(self):
        current_date = get_current_date()
        last_service_date = add_year_to_date(current_date, 0)
        current_mileage = 0
        last_service_mileage = 0

        car = Car_factory.create_thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.need_service())
    

if __name__ == '__main__':
    unittest.main()
    