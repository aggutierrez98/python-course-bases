from figura_geometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
        
    def area(self):
        return self.get_alto() * self.get_ancho()
       
    def __str__(self):
        return FiguraGeometrica.__str__(self) + Color.__str__(self) + ", Area: " + str(self.area())