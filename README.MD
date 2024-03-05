# MongoDB con Python

![Python](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png)

## Descripción

Actividad destinada a mis compañerites, donde podrán aprender a utilizar un poquitin el paquete `mongopy` y `faker`, al mismo tiempo que practican sus habilidades y lógica de programación.

## Requisitos

Para ejecutar este proyecto, asegúrate de cumplir con los siguientes requisitos:

1. Tener Python instalado.
2. Agregar Python a tus variables de entorno.
3. Instalar `mongopy` con el comando: `pip install mongopy`.
4. Instalar `faker` con el comando: `pip install faker`.
5. Ejecutar todo desde el archivo `main.py`.

En el archivo `conexion`, ya tienes una conexión a MongoDB establecida, por lo que no será necesario realizar ninguna acción adicional.

Completa la lógica del CRUD en el archivo `logica`, utilizando las siguientes funciones de la conexión:

- `insertOne()`
- `find()` (este método no recibe ningún parámetro)
- `find_one()` (este método recibe como parámetro un objeto de MongoDB `{}` con la clave 'id' y como valor el id del usuario, por ejemplo, `{'id': usuario_id}`)
- `update_one()`
- `delete_one()`

Una vez hecho lo anterior, en el archivo `main.py`, resolverás lo siguiente:

## Tareas en main.py


# Estructura de un documento usuario:

```python
usuario = {
    'nombre': genera el valor con faker,
    'apellido paterno': genera el valor con faker,
    'apellido materno': genera el valor con faker,
    'año_de_nacimiento': genera el valor con faker,
    'edad': genera el valor con faker,
    'estado': genera el valor con faker,
    'correo': genera el valor con faker,
    'clave_secreta': ''  # Lo generarás después
}
```

1. Prueba todas las operaciones CRUD que implementaste:
   - Crea un documento.
   - Lee un documento (muéstralo).
   - Actualiza un documento.
   - Elimina un documento.

2. Utiliza la librería `faker` para extraer datos y generar un registro con esa información. Muestra ese registro por consola.

3. Utilizando `faker` y estructuras cíclicas:
   - Utiliza un bucle `for` para insertar 10 documentos a la colección.
   - Utiliza un bucle `while` para insertar 7 documentos a la colección.
   - Por último, obteniendo la cantidad total de registros existentes hasta este punto, agrega esa cantidad de nuevos registros con un bucle `for`.

4. Con código Python, muestra todos los usuarios de la coleccion que son mayores de 7 años y menores de 25.

5. Muestra por consola al primer usuario de menor edad de la colección.

6. Muestra por consola al primer usuario de mayor edad de la colección.

7. Muestra por consola únicamente los nombres de todos los documentos de la colección.

8. Crea una función que genere una clave secreta para cada usuario a partir de su información. La clave debe contener:
   - Dos primeras letras de su nombre.
   - Primera letra de apellido materno.
   - Primeras dos letras de su apellido paterno.
   - Últimos dos dígitos de su fecha de nacimiento.
   - Edad.
   - Primera y últimas dos letras de su estado.
   - Todos los caracteres que se encuentran antes del '@' en su correo electrónico.

9. Genera la clave secreta para los usuarios con id 1, 2, 3 y 4, y actualiza su respectivo campo de `clave_secreta` vacío que está en la colección.

## Tenkius

Cuando se trabaja en una aplicación 'real', es preferible evitar el manejo directo de consultas a la base de datos en entornos de producción por diversas razones, tales como seguridad, mantenibilidad y legibilidad. Aunque en esta práctica no se esté utilizando algún ORM, el objetivo principal es almacenar información en una base de datos, en este caso, no relacional. A través de esta aproximación, se llevan a cabo consultas y se realizan diversos tipos de operaciones o ejercicios lógicos para practicar ambas partes. Este enfoque refleja con mayor fidelidad lo que comúnmente se hace en contextos más reales. En estos escenarios, la manipulación y procesamiento de la información se efectúan mediante un lenguaje de programación una vez que los datos están disponibles, en lugar de realizar consultas a la base de datos cada vez que se requiere información.