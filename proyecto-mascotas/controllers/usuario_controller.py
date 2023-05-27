from flask_restful import Resource, request
from base_de_datos import conexion
from models.usuarios_model import UsuarioModel
from dtos.usuario_dto import UsuarioResponseDto, UsuarioRequestDto

class UsuariosController(Resource):
    # cuando yo heredo la clase Resource ahora los metodos que yo cree con el mismo nombre que  un metodo HTTP
    #

    def get(self):
        #Lista
        resultado = conexion.session.query(UsuarioModel).all()
        #many = TRue > el dto iterara el arreglo o lista y convertira cada uno de ellos
        dto = UsuarioResponseDto(many = True)
        data = dto.dump(resultado)
        #data = []
        #for usuario in resultado:
            #data.append({
            #    'id':usuario.id,
            #    'nombre':usuario.nombre,
            #    'apellido': usuario.apellido,
            #    'correo':usuario.correo,
             #   'dni': usuario.dni
            #})
        return {
            'content': data
        }
    
    def post(self):
        data=request.json
        dto = UsuarioRequestDto()
        #load valida el diccionario que le pasamos con los campos que cumplan las condiciones 
        dataValidada = dto.load(data)
        print(dataValidada)
        #inicializo mi nuevo usuario
        nuevoUsuario = UsuarioModel(**dataValidada)
        # nuevoUsuario = UsuarioModel(
        #     nombre='Guillermo',apellido ='Tapia', correo= '123@gmail.com', dni = '1234567')
        #indica que vamos agregar un nuevo registro
        conexion.session.add(nuevoUsuario)
        try:
            # se usa para transacciones sirve para indicar que todos los cambios se guarden
            #de manera permanente, sino hacemos el commit entonces no se guardara la info de manera
            #permanente
            conexion.session.commit()
            return {
                'message': 'Usuario creado exitosamente'
            },201 # CReado exitosaments
        except Exception as error:
            #rollback > para retroceder y dejar todos los posibles cambios sim efecto
            conexion.session.rollback()
            return {
                'message': 'Error al crear el usuario',
                'content': error.args #args > argumentos(porque fallo)
            },400