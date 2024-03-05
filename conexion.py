from pymongo import MongoClient


class ConexionMongo:
    def __init__(self, host='localhost', port=27017, database='mi_database'):
        self.client = MongoClient(host, port)
        self.db = self.client[database]

    def cerrar_conexion(self):
        self.client.close()
