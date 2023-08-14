# CONTROLLER
from controllers.keyboard import KeyboardController

# INPUT DEVICES

# VIEW
class KeyboardView:

    def __init__(self) -> None:
        self.keyboard_ctl = KeyboardController()


    def get_keyboards(self):
        keyboards = self.keyboard_ctl.get_keyboards()
        print(f"\n{keyboards}")


    def create_keyboard(self):
        name = input("Ingrese el nombre del teclado: ")
        brand = input("Ingrese la marca del teclado: ")

        self.keyboard_ctl.create_keyboard(name, brand)
        print("\n¡Teclado creado correctamente!")


    def get_keyboard(self):
        id = input("Ingrese el id del teclado: ")
        keyboard = self.keyboard_ctl.get_keyboard(id)

        if keyboard is None:
            return print("\n¡Teclado no existe!")
        
        print(f"\n{keyboard}")


    def update_keyboard(self):
        id = input("Ingrese el id del teclado: ")
        keyboard = self.keyboard_ctl.get_keyboard(id)

        if keyboard is None:
            return print("\n¡Teclado no existe!")
        
        name = input("Ingrese el nuevo nombre del teclado: ")
        bread = input("Ingrese la nueva marca del teclado: ")

        msg = self.keyboard_ctl.update_keyboard(id, name, bread)
        print(f"\n{msg}")


    def delete_keyboard(self):
        id = input("Ingrese el id del teclado: ")
        keyboard = self.keyboard_ctl.get_keyboard(id)

        if keyboard is None:
            return print("\n¡Teclado no existe!")
        
        msg = self.keyboard_ctl.delete_keyboard(id)
        print(f"\n{msg}")