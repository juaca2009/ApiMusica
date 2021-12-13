from flask_restx import fields
from apiConfig import api

modAgregarCancion = api.model('Agregar Canciones', {
    'nombre': fields.String,'flt': fields.Float,
    'lds': fields.Float,'alds': fields.Float, 
    'strpk': fields.Float,'nrg': fields.Float,
    'danc': fields.Float,'bpm': fields.Float,
    'ptch': fields.Float,'mfcc': fields.List(fields.Float),
    'genero': fields.String
})