from entidades.Obrero import Obrero
from entidades.Administrativo import Administrativo
from entidades.Vendedor import Vendedor
from AccesoDatos.AccesoDatos import AccesoDatosEmpleados

class Gestor:
    
    def __init__(self) -> None:
        self.empleados = {
        1 : Obrero,
        2 : Administrativo,
        3 : Vendedor
    }

    def guardarEmpleado(self, datos):
        n_legajo = AccesoDatosEmpleados().generar_legajo()
        nombre, apellido, sueldoBase, cuarto_campo, tipo_empleado = datos
        empleado = self.empleados[tipo_empleado](n_legajo, nombre, apellido, sueldoBase, cuarto_campo)
        print(empleado.atributos())
        resultado = AccesoDatosEmpleados().guardarEmpleado(empleado)
        return resultado

    def buscarEmpleado(self, legajo):
        datos_empleado, tipo_empleado = AccesoDatosEmpleados().buscarEmpleado(legajo)
        if datos_empleado:
            empleado = self.empleados[tipo_empleado](*datos_empleado)
            return empleado
        return None

            