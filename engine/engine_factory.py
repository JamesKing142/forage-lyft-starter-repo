from model.car_factory import car_factory
from engine import capulet_engine, sternman_engine, willoughby_engine

class Engine_factory(car_factory):
    def check_engine(self, name):
        if name == "capulet":
            return capulet_engine()
        elif name == " sternman":
            return sternman_engine()
        elif name == "willoughby":
            return willoughby_engine()
