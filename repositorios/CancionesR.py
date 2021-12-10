import json
from dbConfig import db
import json
from bson import json_util

class CancionesRepositorio:
    def __init__(self):
        self.__baseDatos = db

    def agregarCancion(self, _atributosDict):
        self.__baseDatos.atributos.insert_one(_atributosDict)

    def obtenerCancion(self, _nombre):
        return self.__baseDatos.atributos.find_one({'nombre': _nombre})