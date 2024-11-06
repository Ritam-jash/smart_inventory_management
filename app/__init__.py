from flask import Flask
from flask_mysqldb import MySQL
from config import Config

mysql = MySQL()

def create_app():
    app = Flask(__name__, template_folder="../templates")  # Explicit template folder
    app.config.from_object(Config)
    mysql.init_app(app)

    with app.app_context():
        from .routes import app_routes
        app.register_blueprint(app_routes)

    return app
