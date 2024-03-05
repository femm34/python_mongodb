from conexion import ConexionMongo


class AsignaturaDAO:
    def __init__(self):
        self.conexion.find = ConexionMongo()
        self.collection = self.conexion.db['asignaturas']

    def agregar_asignatura(self, asignatura):
        self.collection.insert_one(asignatura)

    def obtener_asignaturas(self):
        return list(self.collection.find())

    def obtener_asignatura_por_id(self, asignatura_id):
        return self.collection.find_one({'_id': asignatura_id})

    def actualizar_asignatura(self, asignatura_id, nuevos_datos):
        self.collection.update_one({'_id': asignatura_id}, {
                                   '$set': nuevos_datos})

    def eliminar_asignatura(self, asignatura_id):
        self.collection.delete_one({'_id': asignatura_id})
