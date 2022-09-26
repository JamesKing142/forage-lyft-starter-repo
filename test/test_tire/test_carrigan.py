import unittest
from tire.carrigan_tire import Carrigan

class Test_Carrigan(unittest.TestCase):
    def test_need_serviced(self):
        tire_sensor = [0.1, 0.4, 0.95]

        tire = Carrigan(tire_sensor)
        self.assertTrue(tire.need_service())
    
    def test_not_need_serviced(self):
        tire_sensor = []

        tire = Carrigan(tire_sensor)
        self.assertFalse(tire.need_service())

if __name__ == "__main__":
    unittest.main()