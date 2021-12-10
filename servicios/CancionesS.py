from repositorios.CancionesR import CancionesRepositorio

class cancionesServicio:
    def __init__(self):
        self.__cancionesRepo = CancionesRepositorio()

    def agregarCancion(self, _dictCancion):
        self.__cancionesRepo.agregarCancion(_dictCancion)

    def obtenerCancion(self, _nombre):
        datos = self.__cancionesRepo.obtenerCancion(_nombre)
        del datos['_id']
        if datos != None:
            return datos
        else:
            return 0