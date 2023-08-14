# Output devices
from .output_device import OutputDevice

class Speaker(OutputDevice):
    """Speaker class"""
    def __init__(self, name, brand):
        super().__init__(name, brand)
        self.id = 0
        self.units = 0