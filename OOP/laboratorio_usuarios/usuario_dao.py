from usuario import Usuario
from cursor_del_pool import CursorDelPool
from logger_base import logger


class UsuarioDao:

    __SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    __INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s,%s)'
    __ACTUALIZAR = 'UPDATE usuario SET username= %s, password=%s WHERE id_usuario=%s'
    __ELIMINAR = 'DELETE FROM usuario WHERE id_usuario = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.get_username(), usuario.get_password())
            cursor.execute(cls.__INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.get_username(),
                       usuario.get_password(), usuario.get_id_usuario())
            cursor.execute(cls.__ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.get_id_usuario(),)
            cursor.execute(cls.__ELIMINAR, valores)
            return cursor.rowcount
