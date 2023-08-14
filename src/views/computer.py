# CONTROLLER
from controllers.computer import ComputerController

# VIEW
class ComputerView:

    def __init__(self) -> None:
        self.computer_ctl = ComputerController()


    def get_computers(self):
        computers = self.computer_ctl.get_computers()
        print(computers)


    def create_computer(self):
        name = input("Ingrese el nombre del computador: ")
        mouse_name = input("Ingrese el nombre del mouse: ")
        mouse_brand = input("Ingrese la marca del mouse: ")
        keyboard_name = input("Ingrese el nombre del teclado: ")
        keyboard_brand = input("Ingrese la marca del teclado: ")
        monitor_name = input("Ingrese el nombre del monitor: ")
        monitor_brand = input("Ingrese la marca del monitor: ")
        speaker_name = input("Ingrese el nombre del altavoz: ")
        speaker_brand = input("Ingrese la marca del altavoz: ")

        data = {
            "name": name,
            "mouse": {
                "name": mouse_name,
                "brand": mouse_brand
            },
            "keyboard": {
                "name": keyboard_name,
                "brand": keyboard_brand
            },
            "monitor": {
                "name": monitor_name,
                "brand": monitor_brand
            },
            "speaker": {
                "name": speaker_name,
                "brand": speaker_brand
            }
        }
        self.computer_ctl.create_computer(data)
        print("\n¡Computador creado correctamente!")


    def get_computer(self):
        id = input("Ingrese el id del computador: ")
        computer = self.computer_ctl.get_computer(id)

        if computer is None:
            return print("\n¡Computer no existe!")
        
        print(f"\n{computer}")


    def update_computer(self):
        id = input("Ingrese el id del computador que desea actualizar: ")
        computer = self.computer_ctl.get_computer(id)

        if computer is None:
            return print("\n¡Computer no existe!")
        
        name = input("Ingrese el nuevo nombre del computador: ")
        mouse_name = input("Ingrese el nuevo nombre del mouse: ")
        mouse_brand = input("Ingrese la nueva marca del mouse: ")
        keyboard_name = input("Ingrese el nuevo nombre del teclado: ")
        keyboard_brand = input("Ingrese la nueva marca del teclado: ")
        monitor_name = input("Ingrese el nuevo nombre del monitor: ")
        monitor_brand = input("Ingrese la nueva marca del monitor: ")
        speaker_name = input("Ingrese el nuevo nombre del altavoz: ")
        speaker_brand = input("Ingrese la nueva marca del altavoz: ")

        data = {
            "name": name,
            "mouse": {
                "name": mouse_name,
                "brand": mouse_brand
            },
            "keyboard": {
                "name": keyboard_name,
                "brand": keyboard_brand
            },
            "monitor": {
                "name": monitor_name,
                "brand": monitor_brand
            },
            "speaker": {
                "name": speaker_name,
                "brand": speaker_brand
            }
        }
        
        msg = self.computer_ctl.update_computer(computer, data)
        print(f"\n{msg}")


    def delete_computer(self):
        id = input("Ingrese el id del computador que desea eliminar: ")
        computer = self.computer_ctl.get_computer(id)

        if computer is None:
            return print("\nComputador no existe")
        
        msg = self.computer_ctl.delete_computer(computer)
        print(f"\n{msg}")