from app import app
from apiConfig import api
from servicios import servicioCanciones
from flask import Flask, render_template, request, redirect, session, g, url_for, flash, Blueprint
from flask_restx import Resource


vistaCanciones = Blueprint('vistaCanciones', __name__)


@api.route('/obtenerCancion/<_nombre>')
class atributosMusicales(Resource):
    @api.response(200, 'Success')
    @api.response(204, 'NO CONTENT')
    def get(self, _nombre):
        cancion = servicioCanciones.obtenerCancion(_nombre)
        if cancion != 0:
            return cancion, 200
        else:
            return {"ERROR": 'La cancion no existe'}, 204
