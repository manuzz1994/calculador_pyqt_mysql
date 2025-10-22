import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.database = 'calculadora_costos'
        self.user = 'root' 
        self.password = 'brambilla09'  # PW bdd
        
    def get_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            return connection
        except Error as e:
            print(f"Error conectando a MySQL: {e}")
            return None
    
    def ejecutar_consulta(self, query, params=None):
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute(query, params or ())
                
                if query.strip().upper().startswith('SELECT'):
                    result = cursor.fetchall()
                else:
                    connection.commit()
                    result = cursor.lastrowid
                    
                cursor.close()
                connection.close()
                return result
            except Error as e:
                print(f"Error ejecutando consulta: {e}")
                return None
        return None