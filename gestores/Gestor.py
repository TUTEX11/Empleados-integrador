from entidades.Obrero import Obrero
from entidades.Administrativo import Administrativo
from entidades.Vendedor import Vendedor
from AccesoDatos.AccesoDatos import AccesoDatosEmpleados

class Gestor:

    _instance = None  # Atributo de clase para mantener la única instancia
    lista_paralela = []

    empleados = {
        1: Obrero,
        2: Administrativo,
        3: Vendedor
    } # mapeo para la creacion de los distintos tipos de empleado

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
        nuevo_legajo = AccesoDatosEmpleados().generar_legajo()
        nombre, apellido, sueldoBase, especialidad, tipo_empleado = datos
        empleado = self.empleados[tipo_empleado](nuevo_legajo, nombre, apellido, sueldoBase, especialidad)
        return AccesoDatosEmpleados().guardarEmpleado(empleado)

    def buscarEmpleado(self, legajo):
        datos_empleado, tipo_empleado = AccesoDatosEmpleados().buscarEmpleado(legajo)
        if datos_empleado:
            empleado = self.empleados[tipo_empleado](*datos_empleado)
            self.lista_paralela.append(empleado)
            return empleado
        return None
    
    def eliminar(self, empleado):
        if (resultado := AccesoDatosEmpleados().eliminarEmpleado(empleado.get_legajo())):
            self.lista_paralela.remove(empleado)
        return resultado

    def generarEmpleados(self):
        for valores_empleados in AccesoDatosEmpleados().generadorDeEmpleados():
            datos, tipo = valores_empleados
            empleado = self.empleados[tipo](*datos)
            yield empleado

    def calcularTotalSueldos(self):
        return sum(empleado.calcularSueldo() for empleado in self.generarEmpleados())
    
    def reportePorTipo(self):
        return AccesoDatosEmpleados().reporteCantEmpleadosPorTipo()
    
    def devolverEmpleadoLista(self, index):
        return self.lista_paralela[index]

    def limpiarListaParalela(self):
        self.lista_paralela.clear()
    
    def getMaxPageCount(self):
        return AccesoDatosEmpleados().getMaxPageCount()

    def generarPaginaEmpleados(self, paginaActual):
        self.limpiarListaParalela()
        offset = paginaActual * 10
        datos_empleados = AccesoDatosEmpleados().generarEmpleadosPagina(offset)
        for datos in datos_empleados:
            empleado = self.empleados[datos[5]](*datos[:5])
            self.lista_paralela.append(empleado)
        return self.lista_paralela
        