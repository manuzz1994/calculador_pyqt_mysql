from database.consultas import *

def probar_conexion():
    print("=== PROBANDO CONEXIÓN A LA BASE DE DATOS ===\n")
    
    # 1. Probar obtener recetas
    print("1. Recetas en la base de datos:")
    recetas = obtener_recetas()
    if recetas:
        for receta in recetas:
            print(f"   - {receta['nombre']}") # ({receta['tipo']})")
    else:
        print("   ❌ No se pudieron obtener las recetas")
        return False
    
    # 2. Probar obtener envases de velas
    print("\n2. Envases para velas:")
    envases_vela = obtener_envases_por_tipo('vela')
    if envases_vela:
        for envase in envases_vela:
            print(f"   - {envase['nombre']}: ${envase['precio']}")
    else:
        print("   ❌ No se pudieron obtener los envases")
        return False
    
    # 3. Probar obtener materia prima
    print("\n3. Materia prima disponible:")
    materia_prima = obtener_materia_prima()
    if materia_prima:
        for mp in materia_prima:
            print(f"   - {mp['nombre']}: ${mp['precio_por_gramo']}/g")
    else:
        print("   ❌ No se pudieron obtener los materiales")
        return False
    
    print("\n✅ ¡Conexión exitosa! Todas las consultas funcionan.")
    return True

# Agregar esta función a consultas.py para probar
def obtener_materia_prima():
    return db.ejecutar_consulta("SELECT * FROM materia_prima")

if __name__ == "__main__":
    probar_conexion()