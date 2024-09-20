from sqlite3 import *

class ConexionBaseDatos:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(ConexionBaseDatos, cls).__new__(cls)
            cls._instancia.conn = connect('Empleados.db')
        return cls._instancia

    def obtener_conexion(self):
        return self.conn

class AccesoDatosEmpleados:

    def generar_legajo(self):

        with ConexionBaseDatos().obtener_conexion() as conn:

            cur = conn.cursor()
            try:
                cur.execute('select max(legajo) from empleados')
                nuevo_legajo = int(cur.fetchone()[0]) + 1
                return nuevo_legajo
            except Exception:
                print('Error al tratar de generar nuevo legajo')


    def buscarEmpleado(self, legajo):
        pass

