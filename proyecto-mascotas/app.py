from flask import Flask
from base_de_datos import conexion
from flask_migrate import Migrate
from models.usuarios_model import UsuarioModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/mascotas'

conexion.init_app(app)

Migrate(app, conexion)


if __name__ == '__main__':
    app.run(debug=True)