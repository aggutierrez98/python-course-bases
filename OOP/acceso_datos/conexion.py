import psycopg2 as db
from logger_base import logger
import sys

class Conexion:
    __database= "test_db"
    __username= "postgres"
    __password= "admin"
    __db_port= "5432"
    __host= "127.0.0.1"
    __conexion= None
    __cursor= None
    
    @classmethod
    def obtener_conexion(cls):
        try:
            cls.__conexion = db.connect(database = Conexion.__database , user = Conexion.__username , password = Conexion.__password , port= Conexion.__db_port , host=  Conexion.__host)
            logger.debug(f"Conexion Exitosa: {cls.__conexion}")
            return cls.__conexion
        except Exception as e:
            logger.error(f"Error al conectar a la BD: {e}")
            sys.exit()

    @classmethod
    def obtener_cursor(cls):
        try:
            cls.__cursor = cls.__conexion.cursor()
            logger.debug(f"Se abrio el cursor con exito: {cls.__cursor}")
            return cls.__cursor
        except Exception as e:
            logger.error(f"Error al obtener cursor: {e}")
            sys.exit()
    
    @classmethod
    def cerrar(cls):
        cls.__cursor.close()
        cls.__conexion.close()
        
if __name__ == "__main__":
    logger.info (Conexion.obtener_conexion())
    
        