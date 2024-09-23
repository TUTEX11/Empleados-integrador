from entidades.Empleado import Empleado

class Obrero(Empleado):
    def __init__(self, legajo, nombre, apellido, basico, diasTrabajados) -> None:
        super().__init__(legajo, nombre, apellido, basico)
        self._tipo_empleado = 1
        self._diasTrabajados = diasTrabajados
    
    def get_tipo_empleado(self):
        return self._diasTrabajados
    
    def set_tipo_empleado(self, tipo_empleado):
        self._tipo_empleado = tipo_empleado
    
    def get_diasTrabajados(self):
        return self._diasTrabajados
    
    def set_diasTrabajados(self, diasTrabajados):
        self._diasTrabajados = diasTrabajados
    
    def calcularSueldo(self):
        return (self.get_diasTrabajados() / 20) * self.get_sueldo_basico()
    
    def __str__(self):
        return f'Obrero  Legajo: {self.get_legajo()}  Nombre: {self.get_nombre():<12}  Apellido: {self.get_apellido():<10} Sueldo Basico: {self.get_sueldo_basico()} $ Dias Trabajados: {self.get_diasTrabajados()}'
    
    def atributos(self):
        return tuple(vars(self).values())