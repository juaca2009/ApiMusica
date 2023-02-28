import joblib

class GenderClassification:

    def __int__(self):
        self.__classification_model = joblib.load('helpers/ClasificacionMusical.joblib')

    def predict_gender(self, song_data):
        return self.__classification_model.predict(song_data)