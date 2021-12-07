from dbConfig import db
from dominios.CancionesD import Canciones

class CancionesRepositorio:
    def __init__(self):
        self.__canciones = Canciones()

    def agregarCancion(self, _atributosDict):
        self.__canciones.nombre = _atributosDict['nombre']
        self.__canciones.flt = _atributosDict['flt']
        self.__canciones.lds = _atributosDict['lds']
        self.__canciones.alds = _atributosDict['alds']
        self.__canciones.strpk = _atributosDict['strpk']
        self.__canciones.nrg = _atributosDict['nrg']
        self.__canciones.danc = _atributosDict['danc']
        self.__canciones.bpm = _atributosDict['bpm']
        self.__canciones.ptch = _atributosDict['ptch']
        self.__canciones.mfcc = _atributosDict['mfcc']
        self.__canciones.save()
