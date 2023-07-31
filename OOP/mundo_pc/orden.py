from computadora import Computadora

class Orden:
    contador_ordenes = 0 
    
    def __init__(self, computadoras):
        self.__computadoras = computadoras
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
    
    def agregar_computadora(self, computadora):
        self.__computadoras.append(computadora)
        
    def __str__(self):
        string = ""
        
        for computadora in self.__computadoras:
            string = string + computadora.__str__()
        
        string = ("Orden: " + str(self.__id_orden) + ", computadoras: \n") + string    
        return string
    
    def get_computadoras(self):
        return self.__computadoras
    
    def set_computadoras(self , computadoras):
        self.__computadoras = computadoras
        