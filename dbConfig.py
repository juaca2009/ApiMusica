from app import app
from flask_pymongo import PyMongo

app.config['MONGO_URI'] = "mongodb+srv://juaca2009:songsAttributes@songsattributes.s9z1gij.mongodb.net/?retryWrites=true&w=majority"
client = PyMongo(app)
db = client.db