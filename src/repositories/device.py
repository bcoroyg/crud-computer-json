""" respository devices"""
import json

class DeviceRepository:
    """ DevicesRepository """
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
    def get_all(self, category, sub_category):
        data_list = self.read()
        return data_list[0][category][0][sub_category]
    

    # Crear
    def add(self, data, category, sub_category):
        data_list = self.read()
        data_list[0][category][0][sub_category].append(data)
        self.write(data_list)


    # Buscar por Id
    def get(self, id, category, sub_category):
        data_list = self.get_all(category, sub_category)
        
        for x in data_list:
            if x['id'] == int(id):
                return x
        
        return None


    # Actualizar 
    def update(self, id, name, brand, category, sub_category):
        data_list = self.read()
        get_data = self.get(id, category, sub_category)

        # Eliminando el campo id de la data enviada por el usuario
        # del data['id']

        data_list[0][category][0][sub_category][get_data['id']-1]={
            **data_list[0][category][0][sub_category][get_data['id']-1], 
            "name": get_data['name'] if name == "" else name,
            "brand": get_data['brand'] if brand == "" else brand,
        }
        self.write(data_list)
        

    # Eliminar
    def delete(self, id, category, sub_category):
        data_list = self.read()
        data = self.get(id, category, sub_category)
        del data_list[0][category][0][sub_category][data['id']-1]
        self.write(data_list)