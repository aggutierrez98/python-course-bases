from monitor import Monitor
from teclado import Teclado
from raton import Raton

class Computadora:
    contador_computadoras = 0 
    
    def __init__(self, nombre, monitor, teclado, raton):
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton
        Computadora.contador_computadoras += 1
        self.__id_computadora = Computadora.contador_computadoras
   
    def __str__(self):
        return self.__nombre + ": " + str(self.__id_computadora) + "\n" + "    " + self.__monitor.__str__() + "\n" + "    " + self.__teclado.__str__() + "\n" + "    " + self.__raton.__str__() + "\n"

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_monitor(self):
        return self.__monitor
    
    def set_monitor(self, monitor):
        self.__monitor = monitor
        
    def get_teclado(self):
        return self.__teclado
    
    def set_teclado(self, teclado):
        self.__teclado = teclado
        
    def get_raton(self):
        return self.__raton
    
    def set_raton(self, raton):
        self.__raton = raton
    
    def get_id(self):
        return __id_computadora
        
        