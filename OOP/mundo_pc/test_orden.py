from raton import Raton
from teclado import Teclado
from monitor import Monitor
from computadora import Computadora
from orden import Orden

raton = Raton("usb", "razer")
teclado = Teclado("usb", "HyperX")
monitor = Monitor("Lg", "50 centimentros")
computadora = Computadora("Acer", monitor, teclado, raton)

raton2 = Raton("bluetoot", "logitech")
teclado2 = Teclado("bluetoot", "Redragon")
monitor2 = Monitor("Samsung", "70 centimentros")
computadora2 = Computadora("Lg", monitor2, teclado2, raton2)

computadoras = [computadora, computadora2]
orden = Orden(computadoras)
print(orden)

orden.agregar_computadora(computadora)
print(orden)
