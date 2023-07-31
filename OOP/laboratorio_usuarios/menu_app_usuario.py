from usuario import Usuario
from usuario_dao import UsuarioDao
from logger_base import logger
entrada = "1"
while (entrada !="5"):
    print("\n    MENU DEL USUARIO:\n 1)Listar Usuarios \n 2)Agregar usuarios \n 3)Actualizar usuario \n 4)Eliminar usuario \n 5)Salir \n")
    entrada = input("Ingrese la opcion deseada (1-5): ")

    if (entrada == "1"):
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            logger.info(f"{usuario}")

    if (entrada == "2"):
        username = input("Ingrese username: ")
        password = input("Ingrese password: ")
        usuario = Usuario(None, username, password)
        insertados = UsuarioDao.insertar(usuario)
        logger.info(f"Usuarios insertados: {insertados}")

    if (entrada == "3"):
        id = str(input("Ingrese id_usuario a modificar: "))
        username = input("Ingrese username: ")
        password = input("Ingrese password: ")
        usuario = Usuario(id, username, password)
        modificados = UsuarioDao.actualizar(usuario)
        logger.info(f"Usuarios modificados: {modificados}")

    if (entrada == "4"):
        id = str(input("Ingrese id_usuario a eliminar: "))
        usuario = Usuario(id, None, None)
        eliminados = UsuarioDao.eliminar(usuario)
        logger.info(f"Usuarios eliminados: {eliminados}")

    if (entrada == "5"):
        print("Saliendo del programa...")
        break

