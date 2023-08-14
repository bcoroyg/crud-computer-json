# CONTROLLER
from controllers.monitor import MonitorController

# OUTPUT DEVICES

# VIEW
class MonitorView:

    def __init__(self) -> None:
        self.monitor_ctl = MonitorController()


    def get_monitors(self):
        monitors = self.monitor_ctl.get_monitors()
        print(f"\n{monitors}")


    def create_monitor(self):
        name = input("Ingrese el nombre del monitor: ")
        brand = input("Ingrese la marca del monitor: ")
        
        self.monitor_ctl.create_monitor(name, brand)
        print("\n¡Altavoz creado correctamente!")
    

    def get_monitor(self):
        id = input("Ingrese el id del monitor: ")
        monitor = self.monitor_ctl.get_monitor(id)

        if monitor is None:
            return print("\n¡Monitor no existe!")
        
        return monitor
    

    def update_monitor(self):
        id = input("Ingrese el id del monitor: ")
        monitor = self.monitor_ctl.get_monitor(id)

        if monitor is None:
            return print("\n¡Monitor no existe!")
        
        name = input("Ingrese el nuevo nombre del monitor: ")
        bread = input("Ingrese la nueva marca del monitor: ")

        msg = self.monitor_ctl.update_monitor(id, name, bread)
        print(f"\n{msg}")


    def delete_monitor(self):
        id = input("Ingrese el id del monitor: ")
        monitor = self.monitor_ctl.get_monitor(id)

        if monitor is None:
            return print("\n¡Monitor no existe!")
        
        msg = self.monitor_ctl.delete_monitor(id)
        print(f"\n{msg}")