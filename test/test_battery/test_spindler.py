from multiprocessing import current_process
import unittest
from utils import get_current_date, add_year_to_date
from battery.spindler_battery import Spindler as Sd

class Test_Spindler(unittest.TestCase):
    
    def test_need_serviced(self):
        current_date = get_current_date()
        last_service_date = add_year_to_date(current_date, -3)

        battery = Sd(current_date, last_service_date)
        self.assertTrue(battery.need_service())

    def test_not_need_serviced(self):
        current_date = get_current_date()
        last_service_date = add_year_to_date(current_date, 0)

        battery = Sd(current_date, last_service_date)
        self.assertFalse(battery.need_service())

class Test_Spindler_1(unittest.TestCase):
    # Test spindler batteries version 0.0.1
    # Updatte Spindler batteries: modify the spindler battery so it requires service after three years instead of two
    def test_need_serviced(self):
        current_date = get_current_date()
        last_service_date = add_year_to_date(current_date, -4)

        battery = Sd(current_date, last_service_date)
        self.assertTrue(battery.need_service())
    
    def test_not_need_serviced(self):
        current_date = get_current_date()
        last_service_date = add_year_to_date(current_date, -2)

        battery = Sd(current_date, last_service_date)
        self.assertFalse(battery.need_service())


if __name__ == "__main__":
    unittest.main()
