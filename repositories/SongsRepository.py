from dbConfig import db

class SongsRepository:
    def __init__(self):
        self.__data_base = db

    def save_song(self, song_info):
        self.__data_base.atributos.insert_one(song_info)

    def get_song_by_name(self, name):
        return self.__data_base.atributos.find_one({'Name': name})

    def delete_song_by_name(self, name):
        return self.__data_base.atributos.find_one_and_delete({'Name': name})

    def get_songs_by_gender(self, gender):
        return self.__data_base.find({'gender': {'$in': gender}})