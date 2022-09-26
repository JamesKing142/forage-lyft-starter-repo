from battery.battery_factory import Battery_factory
from utils import add_year_to_date, get_current_date

class Spindler(Battery_factory): 
    def __init__(self, current_date, last_date_service):
        self.last_date_service = last_date_service
        self.current_date = current_date

    def need_service(self):
        service_threshold_date = add_year_to_date(self.last_date_service, 2)
        if service_threshold_date < get_current_date():
            return True
        else:
            return False