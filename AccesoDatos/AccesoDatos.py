from sqlite3 import *
from os import path


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
                cur.execute(self.default_query_reader('consulta2.sql'))
                return cur.fetchone()[0]
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
                tipo_empleado = datos_empleado[4]

                sub_tabla = self.ref_sub_tabla[tipo_empleado]
                col_tabla = self.col_sub_tabla[tipo_empleado]

                secondary.execute(f'select {col_tabla} from {sub_tabla} where legajo=?', (legajo,))
                quinto_campo = secondary.fetchone()[0]

                empleado = datos_empleado[0:4]
                empleado.append(quinto_campo)

                return tuple(empleado), tipo_empleado

            except TypeError as e:
                print('Error 5, hay un problema con el walrus')
                print(str(e))
                return None, None
        
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
            
            cur = conn.cursor()
            try:
                cur.execute(self.default_query_reader('consulta1.sql'))
                
                while True:

                    if (empleado_row := cur.fetchone()) is None:
                        break

                    legajo, nombre, apellido, sueldoBase, tipo_empleado, especialidad = empleado_row
                    datos_empleado = (int(legajo), nombre, apellido, float(sueldoBase), especialidad)
                    yield datos_empleado, tipo_empleado
            except Exception as e:
                print('ERROR 5: al generador de empleados')
                print(str(e))
    
    def reporteCantEmpleadosPorTipo(self):
        
        with ConexionBaseDatos().obtener_conexion() as conn:

            cur = conn.cursor()
            
            try:
                cur.execute(self.default_query_reader('consulta3.sql'))
                reporte = {}
                while True:

                    if (datos_row := cur.fetchone()) is None:
                        break
                    tipo_empleado, cant_empleados = datos_row
                    reporte[tipo_empleado] = cant_empleados

                return reporte
            except Exception as e:
                print('ERROR 6: al reporte de empleados por tipo')
                print(str(e))
        
    
    def default_query_reader(self, filename):

        current_dir = path.dirname(path.abspath(__file__))
        file_path = path.join(current_dir, filename)

        with open(file_path, 'r') as file:
            return file.read()
    
    def generarEmpleadosPagina(self, offset):
        with ConexionBaseDatos().obtener_conexion() as conn:
            cur = conn.cursor()
            query = self.default_query_reader('consulta4.sql')
            try:
                cur.execute(query, (10, offset))
                return cur.fetchall()
            except Exception as e:
                print('ERROR 7: En la paginacion de empleados')
                print(str(e))

    def getMaxPageCount(self):
        with ConexionBaseDatos().obtener_conexion() as conn:
            cur = conn.cursor()
            query = self.default_query_reader('consulta5.sql')
            try:
                cur.execute(query)
                return cur.fetchone()[0]
            except Exception as e:
                print('ERROR 8: En la cuenta maxima de paginas')
                print(str(e))
