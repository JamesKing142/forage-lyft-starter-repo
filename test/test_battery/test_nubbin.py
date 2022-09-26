import unittest
from battery.nubbin_battery import Nubbin as Nb
from utils import add_year_to_date, get_current_date
import unittest

class Test_Nubbin(unittest.TestCase):
    def test_need_serviced(self):
        current_date = get_current_date()
        last_service_date = add_year_to_date(current_date,-5)

        battery = Nb(current_date, last_service_date)
        self.assertTrue(battery.need_service())
    
    def test_not_need_serviced(self):
        current_date = get_current_date()
        last_service_date = add_year_to_date(current_date, 0)

        battery = Nb(current_date, last_service_date)
        self.assertFalse(battery.need_service())
    
if __name__ == "__main__":
    unittest.main()