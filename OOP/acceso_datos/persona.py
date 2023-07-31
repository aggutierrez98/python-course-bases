from logger_base import logger

class Persona:
    def __init__(self, id_persona , nombre , apellido, email):
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        
    def __str__(self):
        return "Valores del objeto persona: \n " + "Id_persona: " + str(self.__id_persona) + "  Nombre: " + self.__nombre + "  Apellido: " + self.__apellido + "  Email: " + self.__email 
    
    def get_id_persona(self):
        return self.__id_persona
    
    def set_id_persona(self, id_persona):
        self.__id_persona = id_persona
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_apellido(self):
        return self.__apellido
    
    def set_apellido(self, apellido):
        self.__apellido = apellido
        
    def get_email(self):
        return self.__email
    
    def set_id_persona(self, email):
        self.__email = email
        
if __name__ == "__main__":
    logger.info ("Desde Persona")