from conexion import Conexion
from persona import Persona
from logger_base import logger

class PersonaDao:
    __seleccionar = "SELECT * FROM persona WHERE id_persona IN %s"
    __insertar = "INSERT INTO persona(id_persona, nombre, apellido, email) VALUES(%s, %s, %s, %s)"
    __actualizar = "UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s"
    __eliminar = "DELETE FROM persona WHERE id_persona=%s"

    @classmethod
    def seleccionar(cls, conexion, cursor, llaves):
        cursor.execute(PersonaDao.__seleccionar, llaves)
        registros = cursor.fetchall()
        personas = []
        for registro in registros:
            persona = Persona(registro[0],registro[1],registro[2],registro[3])
            personas.append(persona)
        return personas

    @classmethod
    def insertar(cls, conexion, cursor, personas):
        try:
            for persona in personas:  
                cursor.execute(PersonaDao.__insertar, (persona.get_id_persona() , persona.get_nombre() , persona.get_apellido() , persona.get_email()))
            conexion.commit()  
        except:
            print("Error al insertar los objetos de tipo persona")
            
            
    @classmethod
    def actualizar(cls, conexion, cursor, valores):
        cursor.executemany(PersonaDao.__actualizar, valores)
        conexion.commit()
        registros_actualizados = cursor.rowcount
        return registros_actualizados

    @classmethod
    def eliminar(cls, conexion, cursor, llaves):
        cursor.executemany(PersonaDao.__eliminar, llaves)
        conexion.commit()
        registros_eliminados = cursor.rowcount
        return registros_eliminados

if __name__ == "__main__":
    logger.info ("Desde PersonaDao")