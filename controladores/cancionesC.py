from app import app
from servicios import servicioCanciones
from flask import Flask, render_template, request, redirect, session, g, url_for, flash, Blueprint
import json


vistaCanciones = Blueprint('vistaCanciones', __name__)

@app.route('/agregarCancion')
def agregarCancion():
    dictPrueba = {
        'nombre': 'cancion prueba', 
        'flt': 0.898983,
        'lds': 0.23445454,
        'alds': 1.2343434,
        'strpk': 1.445665654,	
        'nrg': 0.345656767,
        'danc': 1.344545434545, 
        'bpm': 0.1232323,
        'ptch': 0.1232454,
        'mfcc': [1.34343, 0.12313, 2.34343, 0.34343121] 
    }
    js = json.dumps(dictPrueba)
    print(type(js))
    servicioCanciones.agregarCancion(js)
    return "prueba"
