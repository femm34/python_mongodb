from logica import AsignaturaDAO

asignatura_dao = AsignaturaDAO()

# Agregar una asignatura
nueva_asignatura = {
    'nombre': 'Aplicaciones web',
    'creditos': 10,
    'profesor': 'Alberto Corona'
}

# asignatura_dao.agregar_asignatura(nueva_asignatura)


# Obtener todas las asignaturas
todas_asignaturas = asignatura_dao.obtener_asignaturas()
print("Todas las asignaturas:")
print(todas_asignaturas)

# Obtener una asignatura por ID
# asignatura_por_id = asignatura_dao.obtener_asignatura_por_id(
#     asignatura_dao.obtener_asignaturas()[2]['_id'])
# print("\nAsignatura por ID:")
# print(asignatura_por_id)

# # Actualizar una asignatura
# asignatura_id_a_actualizar = asignatura_dao.obtener_asignaturas()[2]['_id']
# nuevos_datos_asignatura = {'profesor': 'Cinthya Diaz'}
# asignatura_dao.actualizar_asignatura(
#     asignatura_id_a_actualizar, nuevos_datos_asignatura)

# # Obtener todas las asignaturas después de la actualización
# todas_asignaturas_actualizadas = asignatura_dao.obtener_asignaturas()
# print("\nTodas las asignaturas después de la actualización:")
# print(todas_asignaturas_actualizadas)

# # Eliminar una asignatura


# asignatura_id_a_eliminar = asignatura_dao.obtener_asignaturas()[2]['_id']
# asignatura_dao.eliminar_asignatura(asignatura_id_a_eliminar)

# # Obtener todas las asignaturas después de la eliminación
# todas_asignaturas_despues_eliminar = asignatura_dao.obtener_asignaturas()
# print("\nTodas las asignaturas después de la eliminación:")
# print(todas_asignaturas_despues_eliminar)

# # Cerrar la conexión
# asignatura_dao.conexion.cerrar_conexion()
