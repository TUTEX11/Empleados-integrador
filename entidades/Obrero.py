from entidades.Empleado import Empleado

class Obrero(Empleado):
    def __init__(self, legajo, nombre, apellido, basico, diasTrabajados) -> None:
        super().__init__(legajo, nombre, apellido, basico)
        self._tipo_empleado = 1
        self._diasTrabajados = int(diasTrabajados)
    
    def get_tipo_empleado(self):
        return self._tipo_empleado
    
    def set_tipo_empleado(self, tipo_empleado):
        self._tipo_empleado = tipo_empleado
    
    def get_diasTrabajados(self):
        return self._diasTrabajados
    
    def set_diasTrabajados(self, diasTrabajados):
        self._diasTrabajados = diasTrabajados
    
    def calcularSueldo(self):
        basico, diasTrabajados = self.get_sueldo_basico(), self.get_diasTrabajados()
        return ((diasTrabajados / 20) * basico)
    
    def __str__(self):
        return f'{"Obrero":<15} Legajo: {self.get_legajo():<7} Nombre: {self.get_nombre():<16} Apellido: {self.get_apellido():<12} Sueldo Básico:${self.get_sueldo_basico():<10} Días Trabajados: {self.get_diasTrabajados():<5}'

    def atributos(self):
        return tuple(vars(self).values())