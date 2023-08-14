# MODEL
from models.mouse import Mouse

# REPOSITORY
from repositories.device import DeviceRepository

# Input Devices
class MouseController:
    def __init__(self) -> None:
        self.respository = DeviceRepository()
        self.id = 0
        self.category =  "input_devices"
        self.sub_category = "mouses"


    def get_mouses(self):
        mouses = self.respository.get_all(self.category, self.sub_category)
        return mouses


    def create_mouse(self, name, brand):
        self.id+=1 
        new_mouse = Mouse(name, brand)
        new_mouse.id = self.id
        self.respository.add(new_mouse.__dict__, self.category, self.sub_category)
        return new_mouse.id


    def get_mouse(self, id):
        mouse = self.respository.get(id, self.category, self.sub_category)
        if mouse is None:
            return None
        return mouse


    def update_mouse(self, id, name, bread):
        self.respository.update(id, name, bread, self.category, self.sub_category)
        return "¡Mouse actualizado correctamente!"


    def delete_mouse(self, id):
        self.respository.delete(id, self.category, self.sub_category)
        return "¡Mouse eliminado correctamente!"