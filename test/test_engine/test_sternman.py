from tkinter.tix import Tree
import unittest
from engine.sternman_engine import Sternman

class Test_Sternman(unittest.TestCase):
    def test_need_serviced(self):
        warning_light = True

        engine = Sternman(warning_light)
        self.assertTrue(engine.need_service())

    def test_not_need_serviced(self):
        warning_light = False

        engine = Sternman(warning_light)
        self.assertFalse(engine.need_service())

if __name__ == "__main__":
    unittest.main()