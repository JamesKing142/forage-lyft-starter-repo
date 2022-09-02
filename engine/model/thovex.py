from car_factory import car_factory
from engine_factory import Engine_factory
from battery.battery_factory import Battery_factory


class Thovex(car_factory):
    def Engine(self):
        return Engine_factory.check_engine(self,self.engine)
    def Battery(self):
        return Battery_factory.check_battery(self,self.battery)
    def needs_service(self):
        if Thovex.Engine() == True or Thovex.Battery() == True:
            return True
        else:
            return False