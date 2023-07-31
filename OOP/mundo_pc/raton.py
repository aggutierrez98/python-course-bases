from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 0
    
    def __init__(self , entrada , marca):
        super().__init__(entrada , marca)
        Raton.contador_ratones += 1
        self.__id_raton = Raton.contador_ratones
        
    def __str__(self):
        return "Raton   --> Id: " + str(self.__id_raton) + "  Marca: " + self._marca + "  Tipo entrada: " + self._tipo_entrada 
        
    