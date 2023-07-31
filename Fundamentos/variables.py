calificacion = int( input("Ingresar calificacion entre 0 y 10: "))
if (calificacion >= 0 and calificacion < 6):
    print("Resultado final: F")
elif (calificacion == 6 and calificacion < 7):
    print("Resultado final: D")
elif (calificacion == 7 and calificacion < 8):
    print("Resultado final: C")
elif (calificacion == 8 and calificacion < 9):
    print("Resultado final: B")
elif (calificacion >= 9 and calificacion <= 10):
    print("Resultado final: A")
else:
    print("ERROR: Calificacion no valida, debe estar entre 0 y 10 ")
