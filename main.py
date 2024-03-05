# Ejemplo de uso
from logica import UsuarioDAO

# Crear una instancia de UsuarioDAO
dao = UsuarioDAO()

# Agregar un nuevo usuario
usuario_nuevo = {
    'id': 1,
    'nombre': 'Juan',
    'apellido paterno': 'Perez',
    'apellido materno': 'Perez',
    'año_de_nacimiento': 2004,
    'edad': 30,
    'estado': 'hidalgo',
    'correo': 'juan@example.com',
    'clave_secreta': ''
}
# dao.agregar_usuario(usuario_nuevo)

# Obtener todos los usuarios
# usuarios = dao.obtener_usuarios()
# print(usuarios)

# Actualizar un usuario existente
usuario_id = dao.obtener_usuarios()[0]['id']
nuevos_datos = {'edad': 31}
dao.actualizar_usuario(usuario_id, nuevos_datos)

# Eliminar un usuario
dao.eliminar_usuario(usuario_id)


# realiza la logica para las funcinoes crud de esta clase


# utiliza la libreria faker para extraer datos y generar un registro con esa informacion

# utilizando faker y estructuras ciclicas, utiliza un for para insertar 10 documentos a la coleccion, utilizando while inserta 7 documentos a la coleccion
# por ultimo obteniendo la cantidad total de registros existentes hasta este punto, con un for, agrega esa cantidad de nuevosregistros,


# con codigo python muestra todos los usuarios de la base de datos que son mayores de 7 años y menores de 25


# muestra por consola al primer usuario de menor edad de la coleccion
# muestra por consola al primer usuario de mayor edad de la coleccion

# muestra por consola unicamente los nombres de todos los documentos de la coleccion

# haz una funcion que genere una clave secreta para cada usuario a partir de su informacion, esta debe contener lo siguiente:
# dos primeras letras de su nombre, primer letra de apellido materno, primeras dos letras de su apellido paterno,ultimos dos digitos de su fecha de nacimiento,
# edad, primera y ultimas dos letras de su estado, todos los caracteres que se encuentran antes del @ en su correo electronico, es decir, si tengo femm15@gmail.com, lo que voy a
# poner en la clave es unicamente femm15

# genera la clave secreta para los usuarios con id 1,2,3 y 4 y actualiza su respectivo campo de clave_secreta vacio que esta en la coleccion


# from faker import Faker
# from datetime import datetime
# from pymongo import MongoClient
# from conexion import ConexionMongo
