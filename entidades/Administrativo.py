from entidades.Empleado import Empleado


class Administrativo(Empleado):
    def __init__(self, legajo, nombre, apellido, basico, presentismo) -> None:
        super().__init__(legajo, nombre, apellido, basico)
        self._tipo_empleado = 2
        self._Presentismo = presentismo
    
    def get_tipo_empleado(self):
        return self._tipo_empleado
    
    def set_tipo_empleado(self, tipo_empleado):
        self._tipo_empleado = tipo_empleado
    
    def get_presentismo(self):
        return self._Presentismo
    
    def set_presentismo(self, presentismo):
        self._Presentismo = presentismo
    
    def calcularSueldo(self):
        basico, presentismo = self.get_sueldo_basico(), self.get_presentismo()
        return ((basico * 1.13) if (presentismo == 1) else basico)
    
    def __str__(self):
        return f'{"Administrativo":<15} Legajo: {self.get_legajo():<7} Nombre: {self.get_nombre():<16} Apellido: {self.get_apellido():<12} Sueldo Básico:${self.get_sueldo_basico():<10} Presentismo: {self.get_presentismo():<5}'
    
    def atributos(self):
        return tuple(vars(self).values())