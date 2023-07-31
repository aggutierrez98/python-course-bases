import os

class CatalogoPeliculas:
    
    ruta_archivo = "pelicula.txt"

    @staticmethod
    def agregar_pelicula(pelicula):
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo , "a")
            archivo.write(pelicula.get_nombre() + "\n")
        except Exception as e:
            print("Ocurrio un error al agregar pelicula: " , e) 
        finally:
            archivo.close()
    
    @staticmethod    
    def listar_peliculas():
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, "r")
            print("Catalogo de peliculas:\n", archivo.read())
        except Exception as e:
            print("Ocurrio un error al listar peliculas: " , e) 
        finally:
            archivo.close()

    
    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta_archivo)
        except Exception as e:
            print("Ocurrio un error al eliminar archivo: " , e) 
    