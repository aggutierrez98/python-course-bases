import psycopg2 as db

conexion = db.connect(host="127.0.0.1", user="postgres",
                      port="5432", database="test_db", password="admin")
try:
    cursor = conexion.cursor()
    sentencia = "DELETE FROM persona WHERE id_persona=%s"
    entrada = input("Proporciona las pk a eliminar separadas por coma: ")
    tupla = tuple(entrada.split(","))
    valores = tupla
    cursor.executemany(sentencia, valores)
    
    
    
    registros_eliminados = cursor.rowcount
    conexion.commit()
    print(f"Registros eliminados: {registros_eliminados}")
except Exception as e:
    conexion.rollback()
    print("Ocurrio un error en la transaccion: " , e)
finally:
    cursor.close()
    conexion.close()
