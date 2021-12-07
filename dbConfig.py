from app import app
from flask_mongoalchemy import MongoAlchemy

app.config['MONGOALCHEMY_CONNECTION_STRING'] = "mongodb+srv://juaca2009:12345@canciones.6yaip.mongodb.net/Canciones?retryWrites=true&w=majority"
app.config['MONGOALCHEMY_DATABASE'] = 'Canciones'
app.config['MONGOALCHEMY_USER'] = 'juaca2009'
app.config['MONGOALCHEMY_PASSWORD'] = '12345'
db = MongoAlchemy(app)