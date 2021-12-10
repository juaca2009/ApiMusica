from app import app
from flask_restx import Api

api = Api(app, title="Api atributos musicales", 
          description= "Api encargada de enviar y obtener los atributos musicales de las canciones ya analizadas",
          contact_email="juaca2009@gmail.com", contact_url="https://github.com/juaca2009", default="Api Musica",
          default_label="endpoints")