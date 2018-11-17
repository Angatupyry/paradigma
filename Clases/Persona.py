from abc import ABCMeta

from Clases import Contacto
from Clases.Contacto import *


class Persona(metaclass=ABCMeta):

    def __init__(self, cedula, nombre, apellido, direccion=None, contacto=None):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.contactos = []
        self.contactos.append(contacto)

    def add_contacto(self, contacto):
        self.contactos.append(contacto)

    def editar_contacto(self, contacto_viejo, contacto_nuevo):
        self.borrar_contacto(contacto_viejo)
        self.add_contacto(contacto_nuevo)

    def borrar_contacto(self, contacto):
        self.contactos.remove(contacto)


# ---------------------------CLASE EMPLEADO---------------------------------------
class Empleado(Persona):
    cant_empleado = 0

    def __init__(self, cedula, nombre, apellido, direccion=None, contacto=None, salario=0):
        super().__init__(cedula, nombre, apellido, direccion, salario)
        self.salario = salario
        self.__class__.cant_empleado += 1

    def actualizarSalario(self, salario):
        self.salario = salario


# -----------------------------CLASE CLIENTE----------------------------------------
class Cliente(Persona):
    cant_cliente = 0

    def __init__(self, cedula, nombre, apellido, direccion, contacto=None, ruc=None,
                 cuentas_bancarias=None):
        super().__init__(cedula, nombre, apellido, direccion, ruc)
        self.ruc = ruc
        self.cuentas_bancarias = []
        self.cuentas_bancarias.append(cuentas_bancarias)
        self.__class__.cant_cliente += 1
