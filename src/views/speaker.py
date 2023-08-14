# CONTROLLER
from controllers.speaker import SpeakerController

# OUTPUT DEVICES

# VIEW
class SpeakerView:

    def __init__(self) -> None:
        self.speaker_ctl = SpeakerController()


    def get_speakers(self):
        speakers = self.speaker_ctl.get_speakers()
        print(f"\n{speakers}")


    def create_speaker(self):
        name = input("Ingrese el nombre del altavoz: ")
        brand = input("Ingrese la marca del altavoz: ")
        
        self.speaker_ctl.create_speaker(name, brand)
        print("\n¡Altavoz creado correctamente!")


    def get_speaker(self):
        id = input("Ingrese el id del altavoz: ")
        speaker = self.speaker_ctl.get_speaker(id)
        
        if speaker is None:
            return print("\n¡Altavoz no existe!")
        
        print(f"\n{speaker}")


    def update_speaker(self):
        id = input("Ingrese el id del altavoz: ")
        speaker = self.speaker_ctl.get_speaker(id)

        if speaker is not None:
            name = input("Ingrese el nuevo nombre del altavoz: ")
            bread = input("Ingrese la nueva marca del altavoz: ")
            msg = self.speaker_ctl.update_speaker(id, name, bread)
            return print(f"\n{msg}")
        
        return print("\n¡Altavoz no existe!")


    def delete_speaker(self):
        id = input("Ingrese el id del altavoz: ")
        speaker = self.speaker_ctl.get_speaker(id)

        if speaker is None:
            return print("\n¡Altavoz no existe!")
        
        msg = self.speaker_ctl.delete_speaker(id)
        print(f"\n{msg}")