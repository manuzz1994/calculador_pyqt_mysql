from database.conexion import Database

db = Database()

def obtener_recetas():
    return db.ejecutar_consulta("SELECT * FROM recetas")

def obtener_receta_por_tipo(tipo):
    return db.ejecutar_consulta("SELECT * FROM recetas WHERE tipo = %s", (tipo,))

def obtener_ingredientes_receta(receta_id):
    query = """
    SELECT mp.nombre, mp.precio_por_gramo, ri.porcentaje 
    FROM receta_ingredientes ri
    JOIN materia_prima mp ON ri.materia_prima_id = mp.id
    WHERE ri.receta_id = %s
    """
    return db.ejecutar_consulta(query, (receta_id,))

def obtener_envases_por_tipo(tipo):
    return db.ejecutar_consulta("SELECT * FROM envases WHERE tipo = %s", (tipo,))

def obtener_costos_fijos_por_tipo(tipo_producto):
    if tipo_producto == 'vela':
        aplica_a = ['todos', 'vela_refill']
    elif tipo_producto == 'refill':
        aplica_a = ['todos', 'vela_refill']
    elif tipo_producto == 'difusor':
        aplica_a = ['todos', 'difusor']
    else:  # yeso
        aplica_a = ['todos']
    
    placeholders = ', '.join(['%s'] * len(aplica_a))
    query = f"SELECT * FROM costos_fijos WHERE aplica_a IN ({placeholders})"
    return db.ejecutar_consulta(query, aplica_a)

def obtener_materia_prima():
    return db.ejecutar_consulta("SELECT * FROM materia_prima ORDER BY nombre")