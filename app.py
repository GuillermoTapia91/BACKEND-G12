from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from os import environ #muestra las variables de entorno

#las variables de entorno son variables que estan presentes de manera global en toda la
#la maquina/servidor y es aca donde se suelen guardar las credenciales (a la bd, información a otras APIS'S)
#MENSAJERIA(EMAILS) entre otros), credenciales sensibles que no deben ser expuestas

#load_dotenv , carga todas las variables en el archivo .env y las coloca como si fuesen
#variables de entorno, siempre debe ir en la primera linea del archivo principal del proyecto
load_dotenv()

#instancias
app = Flask(__name__)
api = Api(app)

#el metodo get de los diccionarios intentara buscar esa llave y si no existe, retornara None, a
#diferencia de las [] (llaves) que si no encuentra emitira un eeror de tipo KeyError
#el metodo .get() solamente se puede utilizar para devolver o vizualizar los valores, mas
# no para asiganr
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')


if __name__ == '__main__':
    app.run(debug=True)