from flask_restful import Resource,request
from models.usuario_model import Usuario
from config import conexion
from dtos.usuario_dto import RegistroUsuarioRequestDto, LoginUsuarioRequestDto
from bcrypt import gensalt, hashpw

class RegistroController(Resource):
    def post(self):
        data = request.json
        dto = RegistroUsuarioRequestDto()
        
        try:
            dataValidada = dto.load(data)
            password = bytes(dataValidada.get('password'),'utf-8')
            # salt, es un texto creado aleatoriomente que se combinara con la contraseña
            salt = gensalt()
            hash = hashpw(password, salt)
            hashString = hash.decode('utf-8')
            print(hashString)
            #Sobrescribimos en el diccionario de la data Validada la nueva password
            #hasheada
            dataValidada['password'] = hashString

            nuevoUsuario = Usuario(**dataValidada)
            conexion.session.add(nuevoUsuario)
            conexion.session.commit()

            return {
                'message': 'Usuario creado exitosamente'
            },201
        except Exception as e:
            conexion.session.rollback()
            return {
                'message' : 'Error al crear el usuario',
                'content' : e.args
            }, 400

class LoginController(Resource):
    def post(self):
        dto = LoginUsuarioRequestDto ()
        data = request.json
        try:
            dto.load(data)

            return {
                'message': 'Bienvenido'
            }
        except Exception as e:
            return {
                'message': 'Error al hacer el login',
                'content' : e.args
            },400