from repositorios.CancionesR import CancionesRepositorio
import json

class cancionesServicio:
    def __init__(self):
        self.__cancionesRepo = CancionesRepositorio()

    def agregarCancion(self, _jsonCanciones):
        dictCancion = json.loads(_jsonCanciones)
        self.__cancionesRepo.agregarCancion(dictCancion)

    def obtenerCancion(self, _nombre):
        datos = self.__cancionesRepo.obtenerCancion(_nombre)
        if datos != "[]":
            return datos
        else:
            return 0