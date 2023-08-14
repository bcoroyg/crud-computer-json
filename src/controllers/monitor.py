# MODEL
from models.monitor import Monitor

# REPOSITORY
from repositories.device import DeviceRepository

# Input Devices
class MonitorController:
    def __init__(self) -> None:
        self.respository = DeviceRepository()
        self.id = 0
        self.category = "output_devices"
        self.sub_category = "monitors"


    def get_monitors(self):
        monitors = self.respository.get_all(self.category, self.sub_category)
        return monitors


    def create_monitor(self, name, brand):
        self.id+=1 
        new_monitor = Monitor(name, brand)
        new_monitor.id = self.id
        self.respository.add(new_monitor.__dict__, self.category, self.sub_category)
        return new_monitor.id


    def get_monitor(self, id):
        monitor = self.respository.get(id, self.category, self.sub_category)
        if monitor is None:
            return None
        return monitor


    def update_monitor(self, id, name, bread):
        self.respository.update(id, name, bread, self.category, self.sub_category)
        return "¡Monitor actualizado correctamente!"


    def delete_monitor(self, id):
        self.respository.delete(id, self.category, self.sub_category)
        return "¡Monitor eliminado correctamente!"