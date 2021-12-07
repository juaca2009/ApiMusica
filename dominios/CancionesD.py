from dbConfig import db

class Canciones(db.Document):
    nombre = db.StringField()
    flt = db.FloatField()
    lds = db.FloatField()
    alds = db.FloatField()
    strpk = db.FloatField()	
    nrg = db.FloatField()
    danc = db.FloatField()	
    bpm = db.FloatField()
    ptch = db.FloatField()
    mfcc = db.ListField(db.FloatField())