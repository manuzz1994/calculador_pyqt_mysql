"""

Módulo de consultas a la base de datos.
Contiene funciones para interactuar con la base de datos y realizar operaciones CRUD.

"""


from database.conexion import Database

db = Database()

# ==================================================
# Consultas MATERIA_PRIMA
# ==================================================
def obtener_materias_primas():
    """Obtiene todas las materias primas de la base de datos."""
    query = "SELECT * FROM MATERIA_PRIMA"
    return db.ejecutar_consulta(query)

def obtener_materia_prima_por_id(materia_id):
    """Obtiene una materia prima por su ID."""
    query = "SELECT * FROM MATERIA_PRIMA WHERE id = %s"
    return db.ejecutar_consulta(query, (materia_id,))

def agregar_materia_prima(nombre, precio_por_gramo, tipo):
    """Agrega una nueva materia prima a la base de datos."""
    query = "INSERT INTO MATERIA_PRIMA (nombre, precio_por_gramo, tipo) VALUES (%s, %s, %s)"
    return db.ejecutar_consulta(query, (nombre, precio_por_gramo, tipo))

def actualizar_materia_prima(materia_id, nombre, precio_por_gramo, tipo):
    """Actualiza materia prima existente"""
    query = """
    UPDATE MATERIA_PRIMA 
    SET nombre = %s, precio_por_gramo = %s, tipo = %s 
    WHERE id = %s
    """
    return db.ejecutar_consulta(query, (nombre, precio_por_gramo, tipo, materia_id))

def eliminar_materia_prima(materia_id):
    """Elimina una materia prima de la base de datos."""
    query = "DELETE FROM MATERIA_PRIMA WHERE id = %s"
    return db.ejecutar_consulta(query, (materia_id,))

# ==================================================
# Consultas RECETAS
# ==================================================

def obtener_recetas():
    """Obtiene todas las recetas de la base de datos."""
    query = "SELECT * FROM RECETAS"
    return db.ejecutar_consulta(query)

def obtener_receta_por_id(receta_id):
    """Obtiene una receta por su ID."""
    query = "SELECT * FROM RECETAS WHERE id = %s"
    return db.ejecutar_consulta(query, (receta_id,))

def obtener_receta_por_tipo(tipo):
    """Obtiene recetas por su tipo (vela, refil, difusor, yeso)"""
    query = "SELECT * FROM RECETAS WHERE tipo = %s"
    return db.ejecutar_consulta(query, (tipo,))

def agregar_receta(nombre, tipo, densidad):
    """Agrega una nueva receta a la base de datos."""
    query = "INSERT INTO RECETAS (nombre, tipo, densidad) VALUES (%s, %s, %s)"
    return db.ejecutar_consulta(query, (nombre, tipo, densidad))

def actualizar_receta(receta_id, nombre, tipo, densidad):
    """Actualiza una receta existente."""
    query = """
    UPDATE RECETAS 
    SET nombre = %s, tipo = %s, densidad = %s 
    WHERE id = %s
    """
    return db.ejecutar_consulta(query, (nombre, tipo, densidad, receta_id))

def eliminar_receta(receta_id):
    """Elimina una receta de la base de datos."""
    query = "DELETE FROM RECETAS WHERE id = %s"
    return db.ejecutar_consulta(query, (receta_id,))

# ==================================================
# Ingredientes para RECETAS
# ==================================================

def obtener_ingredientes_receta(receta_id):
    """Obtiene los ingredientes de una receta específica."""
    query = """
    SELECT ri_id, mp.id AS materia_prima_id, mp.nombre, mp.precio_por_gramo, ri.porcentaje, mp.tipo, ri.porcentaje
    FROM receta_ingredientes ri
    JOIN materia_prima mp ON ri.materia_prima_id = mp.id 
    WHERE ri.receta_id = %s
    ORDER BY ri_id ASC
    """
    return db.ejecutar_consulta(query, (receta_id,))

def agregar_ingrediente_receta(receta_id, materia_prima_id, porcentaje):
    query = """
    INSERT INTO receta_ingredientes (receta_id, materia_prima_id, porcentaje)
    VALUES (%s, %s, %s)
    """
    return db.ejecutar_consulta(query, (receta_id, materia_prima_id, porcentaje))

def actualizar_ingrediente_receta(ri_id, materia_prima_id, porcentaje):
    query = """
    UPDATE receta_ingredientes 
    SET materia_prima_id = %s, porcentaje = %s 
    WHERE ri_id = %s
    """
    return db.ejecutar_consulta(query, (materia_prima_id, porcentaje, ri_id))

def eliminar_ingrediente_receta(ri_id):
    """Elimina un ingrediente de una receta."""
    query = "DELETE FROM receta_ingredientes WHERE ri_id = %s"
    return db.ejecutar_consulta(query, (ri_id,))

def verificar_porcentaje_receta(receta_id):
    """Verifica que el porcentaje total de los ingredientes de una receta sea 100%."""
    query = """
    SELECT SUM(porcentaje) AS total_porcentaje
    FROM receta_ingredientes
    WHERE receta_id = %s
    """ # Verifica que el porcentaje total de los ingredientes de una receta sea 100%
    resultado = db.ejecutar_consulta(query, (receta_id,))
    if resultado and resultado[0]['total_porcentaje'] is not None: # Si resultado no es None y total_porcentaje no es None
        return resultado[0]['total_porcentaje'] == 100.0 # Retorna True si es 100.0, sino False
    return False 

# ==================================================
# Consultas ENVASES
# ==================================================

def obtener_envases():
    """Obtiene todos los envases de la base de datos."""
    query = """
    SELECT * FROM envases
    ORDER BY tipo
    """
    return db.ejecutar_consulta(query)

def obtener_envase_por_tipo(tipo):
    """Obtiene un envase por su tipo."""
    query = "SELECT * FROM envases WHERE tipo = %s"
    return db.ejecutar_consulta(query, (tipo,))

def obtener_envase_por_id(envase_id):
    """Obtiene un envase por su ID."""
    query = "SELECT * FROM envases WHERE id = %s"
    return db.ejecutar_consulta(query, (envase_id,))

def agregar_envase(nombre, tipo, precio):
    """Agrega un nuevo envase a la base de datos."""
    query = "INSERT INTO envases (nombre, tipo, precio) VALUES (%s, %s, %s)"
    return db.ejecutar_consulta(query, (nombre, tipo, precio))

def actualizar_envase(envase_id, nombre, tipo, precio):
    """Actualiza un envase existente."""
    query = """
    UPDATE envases 
    SET nombre = %s, tipo = %s, precio = %s 
    WHERE id = %s
    """
    return db.ejecutar_consulta(query, (nombre, tipo, precio, envase_id))

def eliminar_envase(envase_id):
    """Elimina un envase de la base de datos."""
    query = "DELETE FROM envases WHERE id = %s"
    return db.ejecutar_consulta(query, (envase_id,))

# ==================================================
# Consultas COSTOS FIJOS
# ==================================================

def obtener_costos_fijos():
    """Obtiene todos los costos fijos de la base de datos."""
    query = "SELECT * FROM costos_fijos ORDER BY concepto"
    return db.ejecutar_consulta(query)

def obtener_costo_fijo_tipo(tipo_producto):
    """Obtener costos fijos que aplican a un tipo específico de producto"""
    if tipo_producto == 'vela':
        aplica_a = ['todos', 'vela_refill']
    elif tipo_producto == 'refill':
        aplica_a = ['todos', 'vela_refill']
    elif tipo_producto == 'difusor':
        aplica_a = ['todos', 'difusor']
    else:  # yeso
        aplica_a = ['todos']

    query = f"""
    SELECT * FROM costos_fijos
    WHERE aplica_a IN ({', '.join(['%s'] * len(aplica_a))})
    ORDER BY concepto
    """
    return db.ejecutar_consulta(query, aplica_a)

def agregar_costo_fijo(concepto, precio, aplica_a):
    """Agrega un nuevo costo fijo a la base de datos."""
    query = "INSERT INTO costos_fijos (concepto, precio, aplica_a) VALUES (%s, %s, %s)"
    return db.ejecutar_consulta(query, (concepto, precio, aplica_a))

def actualizar_costo_fijo(costo_id, concepto, precio, aplica_a):
    """Actualiza un costo fijo existente."""
    query = """
    UPDATE costos_fijos 
    SET concepto = %s, precio = %s, aplica_a = %s 
    WHERE id = %s
    """
    return db.ejecutar_consulta(query, (concepto, precio, aplica_a, costo_id))

def eliminar_costo_fijo(costo_id):
    """Elimina un costo fijo de la base de datos."""
    query = "DELETE FROM costos_fijos WHERE id = %s"
    return db.ejecutar_consulta(query, (costo_id,))

# ==================================================
# Consultas para CALCULO DE COSTOS
# ==================================================

def obtener_datos_calculo(tipo_producto):
    """Obtiene los datos necesarios para el cálculo de costos según el tipo de producto."""
    datos = {
        'recetas': obtener_receta_por_tipo(tipo_producto),
        'envases': obtener_envases(),
        'costos_fijos': obtener_costo_fijo_tipo(tipo_producto)
    }

    if datos['receta']: # Si hay una receta seleccionada, obtener sus ingredientes
        datos['ingredientes'] = obtener_ingredientes_receta(datos['receta'][0]['id']) # Obtener ingredientes de la receta seleccionada

    return datos
    