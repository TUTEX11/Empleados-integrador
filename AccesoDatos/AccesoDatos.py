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

    ref_sub_tabla = {
        1 : 'dias_trabajados_obrero',
        2 : 'presentismo_administrativos',
        3 : 'ventas_vendedores'
    }

    col_sub_tabla = {
        1 : 'cant_dias_trabajados',
        2 : 'presentismo',
        3 : 'ventas'
    }

    def generar_legajo(self):

        with ConexionBaseDatos().obtener_conexion() as conn:

            cur = conn.cursor()
            try:
                cur.execute('select max(legajo) from empleados')
                nuevo_legajo = int(cur.fetchone()[0]) + 1
                return nuevo_legajo
            except Exception:
                print('ERROR 1: al tratar de generar nuevo legajo')


    def guardarEmpleado(self, empleado):

        with ConexionBaseDatos().obtener_conexion() as conn:

            cur = conn.cursor()
            id_tipo_empleado = empleado.get_tipo_empleado()
            atributos = empleado.atributos()
            try:
                cur.execute('insert into empleados (legajo, nombre, apellido, sueldo_basico, id_tipo_empleado) values (?,?,?,?,?)', tuple(empleado.atributos()[0:4]))
                cur.execute(f'insert into {self.ref_sub_tabla[id_tipo_empleado]} (legajo, {self.col_sub_tabla[id_tipo_empleado]}) values (?,?)', (id_tipo_empleado, atributos[5]))
                return True
            except Exception as e:
                print('ERROR 2: al guardar empleado')
                print(e)
                return False


