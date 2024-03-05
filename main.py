from faker import Faker
from logica import UsuarioDAO

# Crea documentos usando los metodos de faker, en este archivo tienes ya disponible faker
# pudes llamar a los siguientes metodos que nos da el modulo de faker:
#       first_name(), last_name(), random_int(min=1980, max=2000), state()

# ejemplo (solo para que vean como juncia):

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
