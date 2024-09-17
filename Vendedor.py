from Empleado import Empleado


class Vendedor(Empleado):
    def __init__(self, legajo, nombre, apellido, basico, ventas) -> None:
        super().__init__(legajo, nombre, apellido, basico)
        self._Ventas = ventas
    
    def get_ventas(self):
        return self._Ventas
    
    def set_ventas(self, ventas):
        self._Ventas = ventas
    
    def calcularSueldo(self):
        return self.get_sueldo_basico() + (self.get_ventas() * 0.01)
    
    def __str__(self):
        return f'Vendedor  Legajo: {self.get_legajo()}  Nombre: {self.get_nombre():<12}  Apellido: {self.get_apellido():<10} Sueldo Basico: {self.get_sueldo_basico()} $ Ventas: {self.get_ventas()} $'