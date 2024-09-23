from entidades.Empleado import Empleado


class Vendedor(Empleado):
    def __init__(self, legajo, nombre, apellido, basico, ventas) -> None:
        super().__init__(legajo, nombre, apellido, basico)
        self._tipo_empleado = 3
        self._Ventas = ventas
    
    def get_tipo_empleado(self):
        return self._diasTrabajados
    
    def set_tipo_empleado(self, tipo_empleado):
        self._tipo_empleado = tipo_empleado
    
    def get_ventas(self):
        return self._Ventas
    
    def set_ventas(self, ventas):
        self._Ventas = ventas
    
    def calcularSueldo(self):
        return self.get_sueldo_basico() + (self.get_ventas() * 0.01)
    
    def __str__(self):
        return f'Vendedor  Legajo: {self.get_legajo()}  Nombre: {self.get_nombre():<12}  Apellido: {self.get_apellido():<10} Sueldo Basico: {self.get_sueldo_basico()} $ Ventas: {self.get_ventas()} $'
    
    def atributos(self):
        return tuple(vars(self).values())