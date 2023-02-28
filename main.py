from app import app
from controllers.SongsCrudController import songCrudView

app.register_blueprint(songCrudView)

if __name__ == "__main__":
    app.run(debug=True)