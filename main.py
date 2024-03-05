from faker import Faker
from logica import UsuarioDAO

# Crea documentos usando los metodos de faker, en este archivo tienes ya disponible faker
# pudes llamar a los siguientes metodos que nos da el modulo de faker:
#       first_name(), last_name(), random_int(min=1980, max=2000), state()
# ejemplo:

fake = Faker()
print(fake.first_name())  # te da un nombre random

# la estructura de un documento usuario, es la siguiente
#   usuario = {
#            'nombre': genera el valor con faker,
#            'apellido paterno': genera el valor con faker,
#            'apellido materno': genera el valor con faker,
#            'año_de_nacimiento': genera el valor con faker,
#            'edad': genera el valor con faker,
#            'estado': genera el valor con faker,
#            'correo': genera el valor con faker,
#            'clave_secreta': dejalo con un string vacio, lo generaras despues
#   }


def generar_usuario_faker():
    fake = Faker()
    usuario = {
        'nombre': fake.first_name(),
        'apellido paterno': fake.last_name(),
        'apellido materno': fake.last_name(),
        'año_de_nacimiento': fake.random_int(min=1980, max=2000),
        'edad': fake.random_int(min=18, max=60),
        'estado': fake.state(),
        'correo': fake.email(),
        'clave_secreta': fake.password()
    }
    return usuario


def main():
    # Crear una instancia de UsuarioDAO
    dao = UsuarioDAO()

    # Generar y agregar varios usuarios utilizando Faker
    for _ in range(5):
        usuario_nuevo = generar_usuario_faker()
        dao.agregar_usuario(usuario_nuevo)

    # Obtener y mostrar todos los usuarios
    usuarios = dao.obtener_usuarios()
    print("Todos los usuarios:")
    print(usuarios)

    # Actualizar el primer usuario (cambia la edad)
    if usuarios:
        usuario_id = usuarios[0]['id']
        nuevos_datos = {'edad': 31}
        dao.actualizar_usuario(usuario_id, nuevos_datos)
        print("\nUsuario actualizado:")
        print(dao.obtener_usuario_por_id(usuario_id))

    # Eliminar el último usuario
    if usuarios:
        usuario_id_eliminar = usuarios[-1]['id']
        dao.eliminar_usuario(usuario_id_eliminar)
        print(f"\nUsuario con id {usuario_id_eliminar} eliminado.")


if __name__ == "__main__":
    main()

# realiza la logica para las funcinoes crud de esta clase


# prueba todas las operaciones CRUD que hiciste, crea un documento, lee un documento (muestralo), actualiza un documento, elimina un documento


# utiliza la libreria faker para extraer datos y generar un registro con esa informacion, tambien muestra por consola ese registro


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
