from engine_factory import Engine_factory

class Willoughby(Engine_factory):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def need_service(self):
        if self.current_mileage - self.last_service_mileage > 60000:
            return True
        else:
            return False