from numpy import dot
from numpy.linalg import norm

class CosineSimilarity:

    @staticmethod
    def base_formula(self, base_song, second_song):
        return dot(base_song, second_song) / (norm(base_song) * norm(second_song))

    @staticmethod
    def similarity_one_much(self, base_song, songs):
        similarity, row = list(), list()
        similarity.append(songs["Name"].tolist())
        row.append(base_song["Name"].values[0])
        song_without_name = base_song.drop(['Name'], axis=1)
        songs_without_name = songs.drop(['Name'], axis=1)
        for i in range(len(songs)):
            temp = songs_without_name.iloc[i]
            row.append(self.base_formula(song_without_name.values.tolist()[0], temp.values.tolist()))
        similarity.append(row)
        return similarity

    @staticmethod
    def similarity_much_much(self, base_songs, songs):
        matrix_similarity = list()
        matrix_similarity.append(base_songs["Name"].tolist())
        matrix_similarity.append(songs["Name"].tolist())
        base_songs_without_name = base_songs.drop(['Name'], axis=1)
        songs_without_name = songs.drop(['Name'], axis=1)
        for i in range(len(base_songs_without_name)):
            fila = list()
            for j in range(len(songs_without_name)):
                fila.append(self.base_formula(base_songs_without_name.iloc[i], songs_without_name.iloc[j]))
            matrix_similarity.append(fila)
        return matrix_similarity