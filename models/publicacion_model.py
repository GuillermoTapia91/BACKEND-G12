from config import conexion
from sqlalchemy import Column, types, ForeignKey


class Publicacion(conexion.Model):
    id = Column(type_= types.Integer, primary_Key=True, autoincrement=True)
    titulo = Column(type_=types.Text, nullable=False)
    descripcion = Column(type_=types.Text)
    habilitado = Column(type_=types.Boolean, default=True)
    usuarioId = Column(ForeignKey(column='usuarios.id'),
                       type_=types.Integer, nullable=False, name='usuario_id')
    
    __tablename__ = 'publicaciones'

