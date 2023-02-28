from repositories.SongsRepository import SongsRepository
from services.Helpers.Validator import Validator

class SongsCrudService:
    def __init__(self):
        self.__songs_repo = SongsRepository()
        self.__data_validator = Validator()

    def save_song(self, song_info):
        try:
            if self.__data_validator.validate(song_info):
                self.__songs_repo.save_song(song_info)
                return "OK"
            else:
                return "SCHEMA ERROR"
        except:
            return "ERROR"

    def get_song(self, name):
        try:
            data_song = self.__songs_repo.get_song_by_name(name)
            if data_song is not None:
                del data_song['_id']
                return data_song
            else:
                return "NO DATA"
        except:
            return "ERROR"

    def delete_song(self, name):
        try:
            if self.__songs_repo.delete_song_by_name(name) is not None:
                return "OK"
            else:
                return "NO DATA"
        except:
            return "ERROR"