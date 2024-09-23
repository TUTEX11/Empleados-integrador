from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, legajo, nombre, apellido, basico) -> None:
        self._Legajo = legajo
        self._Nombre = nombre
        self._Apellido = apellido
        self._SueldoBasico = basico

    # Getters
    def get_legajo(self):
        return self._Legajo

    def get_nombre(self):
        return self._Nombre

    def get_apellido(self):
        return self._Apellido

    def get_sueldo_basico(self):
        return self._SueldoBasico

    # Setters
    def set_legajo(self, legajo):
        self._Legajo = legajo

    def set_nombre(self, nombre):
        self._Nombre = nombre

    def set_apellido(self, apellido):
        self._Apellido = apellido

    def set_sueldo_basico(self, basico):
        self._SueldoBasico = basico

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def calcularSueldo(self):
        pass

    @abstractmethod
    def atributos(self):
        pass

    
