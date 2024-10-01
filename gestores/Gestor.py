from entidades.Obrero import Obrero
from entidades.Administrativo import Administrativo
from entidades.Vendedor import Vendedor
from AccesoDatos.AccesoDatos import AccesoDatosEmpleados

class Gestor:

    _instance = None  # Atributo de clase para mantener la única instancia

    empleados = {
        1: Obrero,
        2: Administrativo,
        3: Vendedor
    }

    def __new__(cls):
        # Verifica si ya existe una instancia, si no la crea
        if cls._instance is None:
            cls._instance = super(Gestor, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        # Solo inicializará una vez
        if not hasattr(self, 'initialized'):
            self.initialized = True  # Marca que ya fue inicializada

    def guardarEmpleado(self, datos):
        n_legajo = AccesoDatosEmpleados().generar_legajo()
        nombre, apellido, sueldoBase, cuarto_campo, tipo_empleado = datos
        empleado = self.empleados[tipo_empleado](n_legajo, nombre, apellido, sueldoBase, cuarto_campo)
        resultado = AccesoDatosEmpleados().guardarEmpleado(empleado)
        return resultado

    def buscarEmpleado(self, legajo):
        datos_empleado, tipo_empleado = AccesoDatosEmpleados().buscarEmpleado(legajo)
        if datos_empleado:
            empleado = self.empleados[tipo_empleado](*datos_empleado)
            return empleado
        return None
    
    def eliminar(self, empleado):
        resultado = AccesoDatosEmpleados().eliminarEmpleado(empleado.get_legajo())
        return resultado

    '''
    def calcularTotalSueldos(self):
        total = 0
        for empleado in self.buscarTodosEmpleados():
            total += empleado.calcularSueldo()
        return total
    
    def buscarTodosEmpleados(self):
        empleados = []
        for tipo_empleado, clase_empleado in self.empleados.items():
            empleados_del_tipo = AccesoDatosEmpleados().buscarEmpleadosPorTipo(tipo_empleado)
            empleados.extend([clase_empleado(*datos_empleado) for datos_empleado in empleados_del_tipo])
        return empleados
    '''
    
    
