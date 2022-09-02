from battery_factory import Battery_factory
from datetime import datetime

class Nubbin_factory(Battery_factory): 
    current_date = datetime.today.date()
    def battery_should_be_serviced(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False