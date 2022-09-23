from engine.engine_factory import Engine_factory

class Capulet(Engine_factory):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def need_service(self):
        if self.current_mileage - self.last_service_mileage > 30000:
            return True
        else: 
            return False
