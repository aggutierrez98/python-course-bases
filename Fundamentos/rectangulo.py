class Rectangulo:
    def __init__ (self, largo, ancho, alto): 
        self.numero1 = largo
        self.numero2 = ancho
        self.numero3 = alto
    def calcularvolumen (self):
        return self.numero1 * self.numero2 * self.numero3
    
largo = int ( input (" Ingresar largo del rectangulo: ") )
ancho = int ( input (" Ingresar ancho del rectangulo: ") )
alto = int ( input (" Ingresar alto del rectangulo: ") )

rec = Rectangulo (largo , ancho , alto)

print ( "El volumen del rectangulo es: " , rec.calcularvolumen () )