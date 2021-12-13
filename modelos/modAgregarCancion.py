from flask_restx import fields
from apiConfig import api

modAgregarCancion = api.model('Agregar Canciones', {
    'nombre': fields.String(default="La cancion"),'flt': fields.Float(default=0.99999),
    'lds': fields.Float(default=0.99999),'alds': fields.Float(default=0.99999), 
    'strpk': fields.Float(default=0.99999),'nrg': fields.Float(default=0.99999),
    'danc': fields.Float(default=0.99999),'bpm': fields.Float(default=0.99999),
    'ptch': fields.Float(default=0.99999),'mfcc': fields.List(fields.Float(dafault=[0.9999, 0.9999, 0.9999, 0.9999])),
    'genero': fields.String(default="Un genero")
})