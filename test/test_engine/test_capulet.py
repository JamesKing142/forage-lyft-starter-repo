import unittest
from engine.capulet_engine import Capulet 

class Test_Capulet(unittest.TestCase):
    def test_need_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = Capulet(current_mileage, last_service_mileage)
        self.assertTrue(engine.need_service())

    def test_not_need_serviced(self):
        current_mileage = 0
        last_service_mileage = 0

        engine = Capulet(current_mileage, last_service_mileage)
        self.assertFalse(engine.need_service())

if __name__ == "__main__":
    unittest.main()