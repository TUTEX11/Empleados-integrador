from entidades.Empleado import Empleado


class Vendedor(Empleado):
    def __init__(self, legajo, nombre, apellido, basico, ventas) -> None:
        super().__init__(legajo, nombre, apellido, basico)
        self._tipo_empleado = 3
        self._Ventas = ventas
    
    def get_tipo_empleado(self):
        return self._tipo_empleado
    
    def set_tipo_empleado(self, tipo_empleado):
        self._tipo_empleado = tipo_empleado
    
    def get_ventas(self):
        return self._Ventas
    
    def set_ventas(self, ventas):
        self._Ventas = ventas
    
    def calcularSueldo(self):
        basico, ventas = self.get_sueldo_basico(), self.get_ventas()
        return (basico + (ventas * 0.01))
    
    def __str__(self):
        return f'{"Vendedor":<15} Legajo: {self.get_legajo():<7} Nombre: {self.get_nombre():<16} Apellido: {self.get_apellido():<12} Sueldo Básico:${self.get_sueldo_basico():<10} Ventas:${self.get_ventas():<5}'

    def atributos(self):
        return tuple(vars(self).values())