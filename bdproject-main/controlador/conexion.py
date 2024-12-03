import mysql.connector
from mysql.connector import Error

def execute_query(query, values=None):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='inventario',
            user='root',
            password=''
        )
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Ejecutar consulta
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
                
            # Confirmar cambios si es INSERT, UPDATE o DELETE
            if query.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
                connection.commit()
                print(f"Consulta ejecutada exitosamente. Filas afectadas: {cursor.rowcount}")
            
            # Imprimir resultados si es SELECT
            if query.strip().upper().startswith("SELECT"):
                results = cursor.fetchall()
                return results
    except Error as e:
        print("Error al ejecutar la consulta:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada.")
