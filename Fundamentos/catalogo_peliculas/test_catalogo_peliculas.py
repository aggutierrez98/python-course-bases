from servicio.catalogo_peliculas import CatalogoPeliculas
from dominio.pelicula import Pelicula

numero_ingresado = None

while numero_ingresado != "4":
    
    if numero_ingresado == "1":
        nombre = input("Ingresar nombre: ")  
        pelicula = Pelicula(nombre)
        CatalogoPeliculas.agregar_pelicula(pelicula) 
    
    if numero_ingresado == "2":
        catalogo = CatalogoPeliculas()
        CatalogoPeliculas.listar_peliculas()
        
    if numero_ingresado == "3":
        catalogo = CatalogoPeliculas()
        CatalogoPeliculas.eliminar()

    print("\nMENU PELICULAS:")
    print("1)Agregar pelicula")
    print("2)Listar peliculas")
    print("3)Eliminar archivo de peliculas")
    print("4)Salir del programa\n")

    numero_ingresado = input("Ingresar opcion: ") 

else:
    print("Salimos del programa...")

