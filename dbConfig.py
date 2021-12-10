from app import app
from flask_pymongo import PyMongo

app.config['MONGO_URI'] = "mongodb+srv://juaca2009:12345@canciones.6yaip.mongodb.net/Canciones?retryWrites=true&w=majority"
cliente = PyMongo(app)
db = cliente.db