""" respository computer"""
import json
            
class ComputerRepository:
    """ ComputerRepository """
    def __init__(self):
        self.filename = "data.json"
    

    # Escribir datos en data.json
    def write(self, data):
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=2)


    # Leer los datos de data.json
    def read(self):
        with open(self.filename, "r") as file:
            return json.load(file)
        

    # Listar
    def get_all(self, category):
        data_list = self.read()
        return data_list[0][category]
    

    # Crear 
    def add(self, data, category):
        data_list = self.read()
        data_list[0][category].append(data)
        self.write(data_list)


    # Buscar por id
    def get(self, id, category):
        data_list = self.get_all(category)
        for x in data_list:
            if x['id'] == int(id):
                return x

        return None


    # Atualizar 
    def update(self, id, name, monitor, mouse, speaker, keyboard, category):
        data_list = self.read()
        get_data = self.get(id, category)

        # Eliminando el campo id de la data enviada por el usuario
        # del data['id']
        
        data_list[0][category][get_data['id']-1]={
            **data_list[0][category][get_data['id']-1], 
            "name": get_data['name'] if name == "" else name,
            "monitor": get_data['monitor'] if monitor == "" else monitor,
            "mouse": get_data['mouse'] if mouse == "" else mouse,
            "speaker": get_data['speaker'] if speaker == "" else speaker,
            "keyboard": get_data['keyboard'] if keyboard == "" else keyboard,
        }
        self.write(data_list)
        
    # Eliminar
    def delete(self, id, category):
        data_list = self.read()
        data = self.get(id, category)
        del data_list[0][category][data['id']-1]
        self.write(data_list)