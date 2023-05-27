from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.mascotas_model import MascotaModel

class MascotaRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = MascotaModel
        #indicamos al DTO que tambien
        include_fk = True