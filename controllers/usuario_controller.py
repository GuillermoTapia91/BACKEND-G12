from flask_restful import Resource,request
from models.usuario_model import Usuario,TipoUsuario
from config import conexion
from dtos.usuario_dto import RegistroUsuarioRequestDto, LoginUsuarioRequestDto,UsuarioResponseDto
from bcrypt import gensalt, hashpw, checkpw
from flask_jwt_extended import create_access_token, jwt_required,get_jwt_identity


class RegistroController(Resource):
    @jwt_required()
    def post(self):
        #solo los administradores puden registar usuario
        usuarioId = get_jwt_identity()
        
        try:
            tipoUsuarioMaestro= conexion.session.query(Usuario).with_entities(Usuario.tipoUsuario).filter_by(id= usuarioId).first()
            print(tipoUsuarioMaestro[0])

            if tipoUsuarioMaestro[0] != TipoUsuario.ADMINISTRADOR:
                raise Exception(
                    "Solamente un administrador puede crear nuevos usuarios"
                )
            data = request.json
            dto = RegistroUsuarioRequestDto()
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
            dataValidada = dto.load(data)
            usuarioEncontrado= conexion.session.query(Usuario).filter_by(
                email=dataValidada.get('email')).first()
            print(usuarioEncontrado)
            if not usuarioEncontrado:
                raise Exception('Usuario con correo {}',format(dataValidada.get('email')))
            
            password = bytes(dataValidada.get('password'), 'utf-8')
            passwordHashed = bytes(usuarioEncontrado.password, 'utf-8')
            # el metodo checkpw sirve para validar si la contraseña es la mimas que la que tenemos hasheada en la base de datos, recordemos que la contraseña guarda esta hasheada (combinada con un texto aleatorio)
            resultado = checkpw(password, passwordHashed)
            print(resultado)
            if resultado:
                token=create_access_token(identity=usuarioEncontrado.id)
                return {
                    'message': 'Bienvenido',
                    'content': token
                }
            else:
                raise Exception('Contraseña incorrecta')
        except Exception as e:
            return {
                'message': 'Error al hacer el login',
                'content' : e.args
            },400

class PerfilController(Resource):
    #jwt_required se colocara al comienzo de cada metodo para indicar que este metodo tiene que solictar la token y esta pasara por todo el proceso de validacion (Si es una token valida, si es nuestra token, si tiempo de vida (aun no caduco))
    @jwt_required()
    def get(self):
        identificador =get_jwt_identity()
        print(identificador)
        usuarioEncontrado = conexion.session.query(Usuario).filter_by(id=identificador).first()
        dto = UsuarioResponseDto()
        resultado = dto.dump(usuarioEncontrado)
        return {
            'content': resultado
        }