from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self , entrada , marca):
        super().__init__(entrada , marca)
        Teclado.contador_teclados += 1
        self.__id_teclado = Teclado.contador_teclados
        
    def __str__(self):
        return "Teclado --> Id: " + str(self.__id_teclado) + "  Marca: " + self._marca + "  Tipo entrada: " + self._tipo_entrada 
        
    