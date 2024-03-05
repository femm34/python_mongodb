from conexion import ConexionMongo


# realiza la logica para las funcinoes crud que faltan en esta clase, utilizando los metodos que tenemos disponibles en self.collection:


# insertOne()
# find() - este metodo no recibe ningun parametro
# find_one() -  este metodo recibe como parametro un objeto de mongodb {} con la clave 'id' y como valor el id del usuario, por ejemplo {'id': usuario_id}
# update_one()
# delete_one()

class UsuarioDAO:
    def __init__(self):
        self.conexion = ConexionMongo()
        self.collection = self.conexion.db['usuarios']

        # Obtener el valor máximo actual de 'id'
        self.max_id = self.get_max_id()

    def get_max_id(self):
        max_id = self.collection.find_one({}, sort=[("id", -1)])
        return max_id.get('id', 0) if max_id else 0

    def agregar_usuario(self, usuario):
        # Incrementar el valor de 'id'
        self.max_id += 1
        usuario['id'] = self.max_id
        self.collection.insert_one(usuario)

    def obtener_usuarios(self):
        return list(self.collection.find())

    def obtener_usuario_por_id(self, usuario_id):
        return self.collection.find_one({'id': usuario_id})

    def actualizar_usuario(self, usuario_id, nuevos_datos):
        self.collection.update_one({'id': usuario_id}, {'$set': nuevos_datos})

    def eliminar_usuario(self, usuario_id):
        self.collection.delete_one({'id': usuario_id})
