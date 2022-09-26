import unittest
from tire.octoprime_tire import Octoprime

class Test_Octoprime(unittest.TestCase):
    
    def test_need_serviced(self):
        test_sensor = [0.5,0.9,0.9,0.9,0.9]

        tire = Octoprime(test_sensor)
        self.assertTrue(tire.need_service())

    def test_not_need_serviced(self):
        test_sensor = []

        tire = Octoprime(test_sensor)
        self.assertFalse(tire.need_service())

if __name__ == "__main__":
    unittest.main()