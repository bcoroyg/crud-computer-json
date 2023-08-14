# Input devices
from .input_device import InputDevice

class Mouse(InputDevice):
    """Mouse class"""
    def __init__(self, name, brand):
        super().__init__(name, brand)
        self.id = 0
        self.units = 0