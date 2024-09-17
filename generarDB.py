from sqlite3 import connect

def run():
    with connect('Empleados.db') as conn:

        cursor = conn.cursor()

        tipo_empleado = '''
        create table if not exists tipo_empleado (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        denominacion TEXT
        )
        '''

        empleados = '''
        create table if not exists empleados (
        legajo INTEGER PRIMARY KEY,
        nombre TEXT,
        apellido TEXT,
        sueldo_basico REAL,
        id_tipo_empleado INTEGER,
        FOREIGN KEY (id_tipo_empleado) REFERENCES tipo_empleado(id)
        )
        '''

        dias_trabajados_obreros = '''
        create table if not exists dias_trabajados_obreros (
        legajo INTEGER PRIMARY KEY,
        cant_dias_trabajados INTEGER,
        FOREIGN KEY (legajo) REFERENCES empleados(legajo)
        )
        '''

        ventas_vendedores = '''
        create table if not exists ventas_vendedores (
        legajo INTEGER PRIMARY KEY,
        ventas REAL,
        FOREIGN KEY (legajo) REFERENCES empleados(legajo)
        )
        '''

        presentismo_administrativos = '''
        create table if not exists presentismo_administrativos (
        legajo INTEGER PRIMARY KEY,
        presentismo INTEGER CHECK (presentismo = 0 or presentismo = 1),
        FOREIGN KEY (legajo) REFERENCES empleados(legajo)
        )
        '''

        '''
        try:
            cursor.execute(empleados)
            cursor.execute(dias_trabajados_obreros)
            cursor.execute(ventas_vendedores)
            cursor.execute(presentismo_administrativos)
        except Exception as e:
            print(str(e))
        '''
        


        
        with open('empleados.csv', 'r') as archivo:
            for linea in archivo:
                datos = linea.strip().split(';')
                tipo_empleado, legajo, nombre, apellido, sueldo_basico = int(datos[0]), int(datos[1]), datos[2], datos[3], float(datos[4])
                actividad = None
                if datos[5] in ('true', 'false'):
                    actividad = 1 if datos[5] == 'true' else 0
                elif tipo_empleado == 1:
                    actividad = int(datos[5])
                else:
                    actividad = float(datos[5])
                
                try:
                    cursor.execute('insert into empleados (legajo, nombre, apellido, sueldo_basico, id_tipo_empleado) values (?,?,?,?,?)', (legajo, nombre, apellido, sueldo_basico, tipo_empleado))

                    if tipo_empleado == 1:
                        cursor.execute('insert into dias_trabajados_obreros (legajo, cant_dias_trabajados) values (?,?)', (legajo, actividad))
                    elif tipo_empleado == 2:
                        cursor.execute('insert into presentismo_administrativos (legajo, presentismo) values (?,?)', (legajo, actividad))
                    else:
                        cursor.execute('insert into ventas_vendedores (legajo, ventas) values (?,?)', (legajo, actividad))
                except Exception as e:
                    print(str(e))

        
        




if __name__ == '__main__':
    run()