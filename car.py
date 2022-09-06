from serviceable import Serviceable

class Car(Serviceable):

    def __init__(self, engine, battery):

        self.engine = engine
        self.battery = battery

    def need_service(self):
        if self.engine.need_service() == True or self.battery.need_service() == True:
            return True
        else:
            return False
