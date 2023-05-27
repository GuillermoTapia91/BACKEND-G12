from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.usuarios_model import UsuarioModel

#DTO > Data Transfer Object
class UsuarioResponseDto(SQLAlchemyAutoSchema):
    class Meta:
        #sirve para pasar metadatos
        model = UsuarioModel

class UsuarioRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        #sirve para pasar metadatos
        model = UsuarioModel