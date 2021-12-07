from app import app
from controladores.cancionesC import vistaCanciones

app.register_blueprint(vistaCanciones)

if __name__ == "__main__":
    app.run(debug=True)