# MODEL
from models.computer import Computer

# REPOSITORY
from repositories.computer import ComputerRepository

# CONTROLLERS
from .monitor import MonitorController
from .mouse import MouseController
from .keyboard import KeyboardController
from .speaker import SpeakerController

# Computer
class ComputerController:
    def __init__(self) -> None:
        self.monitor_ctl = MonitorController()
        self.mouse_ctl = MouseController()
        self.keyboard_ctl = KeyboardController()
        self.speaker_ctl = SpeakerController()
        self.respository = ComputerRepository()
        self.id = 0
        self.category = "computers"


    def get_computers(self):
        computers = self.respository.get_all(self.category)
        data = []
        for computer in computers:
            data.append(self.get_computer(computer["id"]))
        return data


    def create_computer(self, data):
        self.id+=1 
        monitor = self.monitor_ctl.create_monitor(data["monitor"]["name"], data["monitor"]["brand"])
        mouse = self.mouse_ctl.create_mouse(data["mouse"]["name"], data["mouse"]["brand"])
        speaker = self.speaker_ctl.create_speaker(data["speaker"]["name"], data["speaker"]["brand"])
        keyboard = self.keyboard_ctl.create_keyboard(data["keyboard"]["name"], data["keyboard"]["brand"])
        computer = Computer(data["name"], monitor, mouse, speaker, keyboard)
        computer.id = self.id
        self.respository.add(computer.__dict__, self.category)
        return "¡Computador creado correctamente!"


    def get_computer(self, id):
        computer = self.respository.get(id, self.category)
        if computer is None:
            return None
        monitor = self.monitor_ctl.get_monitor(computer["monitor"])
        mouse = self.mouse_ctl.get_mouse(computer["mouse"])
        speaker = self.speaker_ctl.get_speaker(computer["speaker"])
        keyboard = self.keyboard_ctl.get_keyboard(computer["keyboard"])

        # data
        computer = {
            **computer,
            "monitor": monitor,
            "mouse": mouse,
            "speaker": speaker,
            "keyboard": keyboard,
        }
        return computer


    def update_computer(self, computer, data):
        self.monitor_ctl.update_monitor(computer["monitor"]["id"], data["monitor"]["name"], data["monitor"]["brand"])
        self.mouse_ctl.update_mouse(computer["mouse"]["id"], data["mouse"]["name"], data["mouse"]["brand"])
        self.speaker_ctl.update_speaker(computer["speaker"]["id"], data["speaker"]["name"], data["speaker"]["brand"])
        self.keyboard_ctl.update_keyboard(computer["keyboard"]["id"], data["keyboard"]["name"], data["keyboard"]["brand"])
        self.respository.update(computer["id"], data["name"], computer["monitor"]["id"], computer["mouse"]["id"], computer["speaker"]["id"], computer["keyboard"]["id"], self.category)
        return "¡Computador actualizado correctamente!"


    def delete_computer(self, computer):
        self.monitor_ctl.delete_monitor(computer["monitor"]["id"])
        self.mouse_ctl.delete_mouse(computer["mouse"]["id"])
        self.speaker_ctl.delete_speaker(computer["speaker"]["id"])
        self.keyboard_ctl.delete_keyboard(computer["keyboard"]["id"])
        self.respository.delete(computer["id"], self.category)
        return "¡Computador eliminado correctamente!"