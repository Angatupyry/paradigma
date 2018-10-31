from abc import ABCMeta, abstractmethod

from Framework.Util import *


class Contacto(metaclass=ABCMeta):
    """Clase que contiene los contactos de las personas"""

    def __init__(self, cedula_cliente):
        self.cedula_cliente = cedula_cliente
        pass

    @abstractmethod
    def agregar(self):
        pass

    @abstractmethod
    def borrar(self):
        pass

    @abstractmethod
    def modificar(self):
        pass


class Telefono(Contacto):
    def __init__(self, cedula_cliente, telefono = None):
        super().__init__(self, cedula_cliente)
        self.telefono = telefono

    def agregar(self):
        #Telefono.prompt_init()
        #Falta implementar
        pass

    def borrar(self):
        pass

    def modificar(self):
        pass

    def prompt_init():
        return dict(telefono=input_entero_r("Nro. teléfono: "))

    prompt_init = staticmethod(prompt_init)


class RedSocial(Contacto):
    pass


class Email(Contacto):
    pass