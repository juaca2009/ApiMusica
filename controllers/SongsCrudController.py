from apiConfig import api
from services import SongsCrudService
from models.SaveSongModel import saveSongModel
from flask import Blueprint
from flask_restx import Resource


songCrudView = Blueprint('songCrudView', __name__)


@api.route('/obtenerCancion/<name>')
class GetSongInfo(Resource):
    @api.response(200, 'Success')
    @api.response(204, 'No content')
    @api.response(500, 'BD problem')
    def get(self, name):
        song = SongsCrudService.get_song(name)
        if song != "ERROR":
            if song != "NO DATA":
                return song, 200
            else:
                return {"ERROR": 'La cancion no existe'}, 204
        else:
            return {"ERROR": "Problema al conectarse a la base de datos"}, 500
    

@api.route('/agregarCancion')
class SaveSongInfo(Resource):
    @api.response(201, 'Created')
    @api.response(500, 'BD problem')
    @api.response(400, 'Bad request')
    @api.expect(saveSongModel, validate=True)
    def post(self):
        song = api.payload
        response = SongsCrudService.save_song(song)
        if response == "OK":
            return {"Success": "Cancion agegada"}, 201
        elif response == "SCHEMA ERROR":
            return {"ERROR": "Formato erroneo"}, 400
        else:
            return {"ERROR": "Problema al conectarse a la base de datos"}, 500

@api.route('/eliminarCancion/<name>')
class DeleteSong(Resource):
    @api.response(200, 'Success')
    @api.response(204, 'No content')
    @api.response(500, 'BD problem')
    def delete(self, name):
        response = SongsCrudService.delete_song(name)
        if response == "OK":
            return {"Success": "Cancion eliminada"}, 200
        elif response == "NO DATA":
            return {"ERROR": 'La cancion no existe'}, 204
        else:
            return {"ERROR": "Problema al conectarse a la base de datos"}, 500 