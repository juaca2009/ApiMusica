from dbConfig import db

class CancionesRepositorio:
    def __init__(self):
        self.__baseDatos = db

    def agregarCancion(self, _atributosDict):
        self.__baseDatos.atributos.insert_one(_atributosDict)

