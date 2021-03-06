from app import app
from apiConfig import api
from servicios import servicioCanciones
from modelos.modAgregarCancion import modAgregarCancion
from flask import Flask, render_template, request, redirect, session, g, url_for, flash, Blueprint
from flask_restx import Resource


vistaCanciones = Blueprint('vistaCanciones', __name__)


@api.route('/obtenerCancion/<_nombre>')
class obtenerAtributosMusicales(Resource):
    @api.response(200, 'Success')
    @api.response(204, 'No content')
    @api.response(500, 'BD problem')
    def get(self, _nombre):
        cancion = servicioCanciones.obtenerCancion(_nombre)
        if cancion != "ERROR":
            if cancion != "NO DATA":
                return cancion, 200
            else:
                return {"ERROR": 'La cancion no existe'}, 204
        else:
            return {"ERROR": "Problema al conectarse a la base de datos"}, 500
    

@api.route('/agregarCancion')
class agregarAtributosMusicales(Resource):
    @api.response(201, 'Created')
    @api.response(500, 'BD problem')
    @api.response(400, 'Bad request')
    @api.expect(modAgregarCancion, validate=True)
    def post(self):
        cancion = api.payload
        salida = servicioCanciones.agregarCancion(cancion)
        if salida == "OK":
            return {"Success": "Cancion agegada"}, 201
        elif salida == "SCHEMA ERROR":
            return {"ERROR": "Formato erroneo"}, 400
        else:
            return {"ERROR": "Problema al conectarse a la base de datos"}, 500

@api.route('/eliminarCancion/<_nombre>')
class eliminarCancion(Resource):
    @api.response(200, 'Success')
    @api.response(204, 'No content')
    @api.response(500, 'BD problem')
    def delete(self, _nombre):
        salida = servicioCanciones.eliminarCancion(_nombre)
        if salida == "OK":
            return {"Success": "Cancion eliminada"}, 200
        elif salida == "NO DATA":
            return {"ERROR": 'La cancion no existe'}, 204
        else:
            return {"ERROR": "Problema al conectarse a la base de datos"}, 500 