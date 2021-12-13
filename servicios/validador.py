from schema import Schema, And

class validador:
    def __init__(self):
        self.__schema = Schema({
            'nombre': str,
            'flt': float,
            'lds': float,
            'alds': float, 
            'strpk': float,
            'nrg': float,
            'danc': float,
            'bpm': float,
            'ptch': float,
            'mfcc': And([float], lambda n: len(n) == 4),
            'genero': str
        })

    def validar(self, _dictEntrada):
        return self.__schema.is_valid(_dictEntrada)
       