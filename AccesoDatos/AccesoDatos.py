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
        1 : 'dias_trabajados_obreros',
        2 : 'presentismo_administrativos',
        3 : 'ventas_vendedores'
    } # mapeo de tablas adyacentes a la tabla general de empleados

    col_sub_tabla = {
        1 : 'cant_dias_trabajados',
        2 : 'presentismo',
        3 : 'ventas'
    } # mapeo de las columnas de las tablas adyacentes a la tabla general de empleados

    def generar_legajo(self):

        with ConexionBaseDatos().obtener_conexion() as conn:

            cur = conn.cursor()
            try:
                cur.execute('select max(legajo) from empleados')
                nuevo_legajo = int(cur.fetchone()[0])
                return nuevo_legajo + 1
            except Exception:
                print('ERROR 1: al tratar de generar nuevo legajo')


    def guardarEmpleado(self, empleado):

        with ConexionBaseDatos().obtener_conexion() as conn:

            cur = conn.cursor()
            secondary = conn.cursor()

            id_tipo_empleado = empleado.get_tipo_empleado()
            atributos = empleado.atributos()
            especialidad = atributos[5]

            sub_tabla = self.ref_sub_tabla[id_tipo_empleado]
            col_tabla = self.col_sub_tabla[id_tipo_empleado]

            try:
                cur.execute('insert into empleados (legajo, nombre, apellido, sueldo_basico, id_tipo_empleado) values (?,?,?,?,?)', atributos[0:5])
                secondary.execute(f'insert into {sub_tabla} (legajo, {col_tabla}) values (?,?)', (empleado.get_legajo(), especialidad))
                return True
            except Exception as e:
                print('ERROR 2: al guardar empleado')
                print(str(e))
    
    def buscarEmpleado(self, legajo):

        with ConexionBaseDatos().obtener_conexion() as conn:

            cur = conn.cursor()
            secondary = conn.cursor()

            try:
                cur.execute('select * from empleados where legajo=?', (legajo,))

                if (datos_empleado_row := cur.fetchone()) is None:
                    return None, None
                
                datos_empleado = list(datos_empleado_row)

                sub_tabla = self.ref_sub_tabla[datos_empleado[4]]
                col_tabla = self.col_sub_tabla[datos_empleado[4]]

                secondary.execute(f'select {col_tabla} from {sub_tabla} where legajo=?', (legajo,))
                quinto_campo = secondary.fetchone()

                empleado = datos_empleado[0:4]
                empleado.append(quinto_campo[0])

                return tuple(empleado), datos_empleado[4]

            except TypeError as e:
                print('Error 5, hay un problema con el walrus')
                print(str(e))
        
            except Exception as e:
                print('ERROR 3: al buscar empleado')
                print(str(e))
                return None, None
    
    def eliminarEmpleado(self, legajo):
        
        with ConexionBaseDatos().obtener_conexion() as conn:
            
            cur = conn.cursor()
            secondary = conn.cursor() # cursor secundario para realizar consultas sobre las tablas adyacentes a la tabla general de empleados segun tipo

            try:
                cur.execute(f'delete from {self.ref_sub_tabla[self.buscarEmpleado(legajo)[1]]} where legajo=?', (legajo,))
                secondary.execute('delete from empleados where legajo=?', (legajo,))
                return True
            except Exception as e:
                print('ERROR 4: al eliminar empleado')
                print(str(e))
                return False
    
    def generadorDeEmpleados(self):
        
        with ConexionBaseDatos().obtener_conexion() as conn:
            
            cur = conn.cursor() # cursor primario sobre la tabla general de empleados
            secondary = conn.cursor() # cursor secundario para realizar consultas sobre las tablas adyacentes a la tabla general de empleados segun tipo

            cur.execute('Select * from empleados')
            
            while True:

                if (empleado_row := cur.fetchone()) is None:
                    break

                legajo, nombre, apellido, sueldoBase, tipo_empleado = empleado_row
                secondary.execute(f'select * from {self.ref_sub_tabla[tipo_empleado]} where legajo=?', (legajo,))
                especialidad = secondary.fetchone()[1]
                datos_empleado = (int(legajo), nombre, apellido, float(sueldoBase), especialidad)
                yield datos_empleado, tipo_empleado
        
