# MODEL
from models.keyboard import Keyboard

# REPOSITORY
from repositories.device import DeviceRepository

# Input Devices
class KeyboardController:
    def __init__(self) -> None:
        self.respository = DeviceRepository()
        self.id = 0
        self.category = "input_devices"
        self.sub_category = "keyboards"


    def get_keyboards(self):
        keyboards = self.respository.get_all(self.category, self.sub_category)
        return keyboards

    def create_keyboard(self, name, brand):
        self.id+=1 
        new_keyboard = Keyboard(name, brand)
        new_keyboard.id = self.id
        self.respository.add(new_keyboard.__dict__, self.category, self.sub_category)
        return new_keyboard.id


    def get_keyboard(self, id):
        keyboard = self.respository.get(id, self.category, self.sub_category)
        if keyboard is None:
            return None
        return keyboard


    def update_keyboard(self, id, name, bread):
        self.respository.update(id, name, bread, self.category, self.sub_category)
        return "¡Teclado actualizado correctamente!"


    def delete_keyboard(self, id):
        self.respository.delete(id, self.category, self.sub_category)
        return "¡Teclado eliminado correctamente!"