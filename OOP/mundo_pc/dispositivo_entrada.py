class DispositivoEntrada:
    def __init__(self, entrada, marca):
        self._tipo_entrada = entrada
        self._marca = marca
        
    def get_tipo_entrada(self):
        return self._tipo_entrada
    
    def set_tipo_entrada(self , entrada):
        self._tipo_entrada = entrada
        
    def get_marca(self):
        return self._marca
    
    def set_marca(self , marca):
        self._marca = marca
        
    