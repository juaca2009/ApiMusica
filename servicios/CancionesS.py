from repositorios.CancionesR import CancionesRepositorio
from servicios.validador import validador

class cancionesServicio:
    def __init__(self):
        self.__cancionesRepo = CancionesRepositorio()
        self.__valData = validador()

    def agregarCancion(self, _dictCancion):
        try:
            if self.__valData.validar(_dictCancion):
                self.__cancionesRepo.agregarCancion(_dictCancion)
                return "OK"
            else:
                return "SCHEMA ERROR"
        except:
            return "ERROR"

    def obtenerCancion(self, _nombre):
        try:
            datos = self.__cancionesRepo.obtenerCancion(_nombre)
            if datos != None:
                del datos['_id']
                return datos
            else:
                return "NO DATA"
        except:
            return "ERROR"

    def eliminarCancion(self, _nombre):
        try:
            if self.__cancionesRepo.eliminarCancion(_nombre) is not None:
                return "OK"
            else:
                return "NO DATA"
        except:
            return "ERROR"