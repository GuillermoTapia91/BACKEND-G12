from flask_restful import Resource, request
from base_de_datos import conexion
from models.mascotas_model import MascotaModel
from dtos.mascota_dto import MascotaRequestDto

class MascotasController(Resource):
    def post(self):
        try:
            data = request.json
            dto = MascotaRequestDto()
            dataValidada = dto.load(data)
            nuevaMascota = MascotaModel(**dataValidada)

            conexion.session.add(nuevaMascota)
            conexion.session.commit()

            return{
                'message':'Mascota creada Exitosamente'
            },201
        except Exception as error:
            conexion.session.rollback()
            return {
                'message': 'Error al crear la mascota',
                'content': error.args
            }