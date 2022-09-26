import unittest
from engine.willoughby_engine import Willoughby as Wb

class Test_Willoughby(unittest.TestCase):
    def test_need_serviced(self):
        current_mileage = 1000000
        last_service_mileage = 0

        engine = Wb(current_mileage, last_service_mileage)
        self.assertTrue(engine.need_service())

    def test_not_need_serviced(self):
        current_mileage = 0
        last_service_mileage = 0

        engine = Wb(current_mileage, last_service_mileage)
        self.assertFalse(engine.need_service())

if __name__ == "__main__":
    unittest.main()