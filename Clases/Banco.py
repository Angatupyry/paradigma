from abc import ABCMeta


class Empresa(metaclass=ABCMeta):
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion


class Banco(Empresa):
    def __init__(self, nombre, direccion):
        super().__init__(nombre, direccion)
