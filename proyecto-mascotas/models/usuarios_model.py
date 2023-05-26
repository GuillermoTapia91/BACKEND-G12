from sqlalchemy.schema import Column
from sqlalchemy import types
from base_de_datos import conexion

class UsuarioModel(conexion.Model):
    id = Column(type_ = types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text)
    apellido = Column(type_=types.Text)
    correo = Column(type_=types.Text, unique=True, nullable=False)
    dni = Column(type_=types.Text, unique=True, nullable=False)

    # Como se llamara la tabla en la base de datos si no le ponemos este nombre, sera el mismo que la clase
    #(UsuarioMODEL)
    __tablename__ = 'usuarios'


