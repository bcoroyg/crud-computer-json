# CONTROLLER
from controllers.mouse import MouseController

# INPUT DEVICES

# VIEW
class MouseView:

    def __init__(self) -> None:
        self.mouse_ctl = MouseController()


    def get_mouses(self):
        mouses = self.mouse_ctl.get_mouses()
        print(f"\n{mouses}")


    def create_mouse(self):
        name = input("Ingrese el nombre del mouse: ")
        brand = input("Ingrese la marca del mouse: ")

        self.mouse_ctl.create_mouse(name, brand)
        print("\n¡Mouse creado correctamente!")


    def get_mouse(self):
        id = input("Ingrese el id del mouse que buscas: ")
        mouse = self.mouse_ctl.get_mouse(id)

        if mouse is None:
            return print("\n¡Mouse no existe!")
        
        print(f"\n{mouse}")


    def update_mouse(self):
        id = input("Ingrese el id del mouse que desea actualizar: ")
        mouse = self.mouse_ctl.get_mouse(id)

        if mouse is None:
            return print("\n¡Mouse no existe!")
        
        name = input("Ingrese el nuevo nombre del mouse: ")
        bread = input("Ingrese la nueva marca del mouse: ")

        msg = self.mouse_ctl.update_mouse(id, name, bread)
        print(f"\n{msg}")


    def delete_mouse(self):
        id = input("Ingrese el id del mouse que desea eliminar: ")
        mouse = self.mouse_ctl.get_mouse(id)

        if mouse is None:
            return print("\n¡Mouse no existe!")
        
        msg = self.mouse_ctl.delete_mouse(id)
        print(f"\n{msg}")