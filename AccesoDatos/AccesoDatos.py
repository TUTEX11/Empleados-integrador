from sqlite3 import connect

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

    def buscarEmpleado(legajo):

        pass