from repositorios.CancionesR import CancionesRepositorio

class cancionesServicio:
    def __init__(self):
        self.__cancionesRepo = CancionesRepositorio()

    def agregarCancion(self, _dictCancion):
        try:
            self.__cancionesRepo.agregarCancion(_dictCancion)
            return "OK"
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