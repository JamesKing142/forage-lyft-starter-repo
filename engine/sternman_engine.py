from engine_factory import Engine_factory

class Sternman(Engine_factory):
    def __init__ (self, warning_light: bool):
        self.warning_light: warning_light

    def need_service(self):
        if self.warning_light:
            return True
        else:
            return False
