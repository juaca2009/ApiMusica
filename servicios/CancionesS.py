from repositorios.CancionesR import CancionesRepositorio
import json

class cancionesServicio:
    def __init__(self):
        self.__cancionesRepo = CancionesRepositorio()

    def agregarCancion(self, _jsonCanciones):
        dictCancion = json.loads(_jsonCanciones)
        self.__cancionesRepo.agregarCancion(dictCancion)