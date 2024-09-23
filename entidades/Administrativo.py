from entidades.Empleado import Empleado


class Administrativo(Empleado):
    def __init__(self, legajo, nombre, apellido, basico, presentismo) -> None:
        super().__init__(legajo, nombre, apellido, basico)
        self._tipo_empleado = 2
        self._Presentismo = presentismo
    
    def get_tipo_empleado(self):
        return self._diasTrabajados
    
    def set_tipo_empleado(self, tipo_empleado):
        self._tipo_empleado = tipo_empleado
    
    def get_presentismo(self):
        return self._Presentismo
    
    def set_presentismo(self, presentismo):
        self._Presentismo = presentismo
    
    def calcularSueldo(self):
        return self.get_sueldo_basico() * 1.13 if self.get_presentismo() else self.get_sueldo_basico()
    
    def __str__(self):
        return f'Administrativo  Legajo: {self.get_legajo()}  Nombre: {self.get_nombre():<12}  Apellido: {self.get_apellido():<10} Sueldo Basico: {self.get_sueldo_basico()} $ Presentismo: {self.get_presentismo()}'
    
    def atributos(self):
        return tuple(vars(self).values())