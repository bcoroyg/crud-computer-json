# MODEL
from models.speaker import Speaker

# REPOSITORY
from repositories.device import DeviceRepository

# Output Devices
class SpeakerController:
    def __init__(self) -> None:
        self.respository = DeviceRepository()
        self.id = 0
        self.category =  "output_devices"
        self.sub_category = "speakers"


    def get_speakers(self):
        speakers = self.respository.get_all(self.category, self.sub_category)
        return speakers


    def create_speaker(self, name, brand):
        self.id+=1 
        new_speaker = Speaker(name, brand)
        new_speaker.id = self.id
        self.respository.add(new_speaker.__dict__, self.category, self.sub_category)
        return new_speaker.id


    def get_speaker(self, id):
        speaker = self.respository.get(id, self.category, self.sub_category)
        if speaker is None:
            return None
        return speaker


    def update_speaker(self, id, name, bread):
        self.respository.update(id, name, bread, self.category, self.sub_category)
        return "¡Altavoz actualizado correctamente!"


    def delete_speaker(self, id):
        self.respository.delete(id, self.category, self.sub_category)
        return "¡Altavoz eliminado correctamente!"