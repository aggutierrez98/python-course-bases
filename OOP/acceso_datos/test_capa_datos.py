from persona import Persona
from conexion import Conexion
from persona_dao import PersonaDao

conexion = Conexion.obtener_conexion()
cursor = Conexion.obtener_cursor()

persona1 = Persona("1", "Agustin", "Gomez", "agomez@gmail.com")
persona2 = Persona("2", "Jorge", "Gomez", "jgomez@gmail.com")
persona3 = Persona("3", "Santiago", "Gomez", "sgomez@gmail.com")
personas = (persona1,persona2,persona3)

PersonaDao.insertar(conexion, cursor, personas)

entrada = input("Proporciona las pk a buscar (separado por comas): ")
tupla = tuple(entrada.split(','))
llaves_buscar = (tupla,)

personas = PersonaDao.seleccionar(conexion, cursor, llaves_buscar)
for persona in personas:
    print(persona)

valores_actualizar = (
    ('Juan', 'Perez', 'jperez@mail.com', 1),
    ('Karla1', 'Gomez2', 'kgomez3@mail.com', 2)
)

registros_actualizados = PersonaDao.actualizar(conexion, cursor, valores_actualizar)
print("Registros actualizados: ",registros_actualizados)

entrada = input("Proporciona las pk a eliminar separadas por coma: ")
tupla2 = tuple(entrada.split(","))
llaves_eliminar = tupla2

registros_eliminados = PersonaDao.eliminar(conexion, cursor, llaves_eliminar)
print("Registros eliminados: ",registros_eliminados)

Conexion.cerrar()
