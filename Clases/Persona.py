from abc import ABCMeta

from Clases import Contacto
from Clases.Contacto import *


class Persona(metaclass=ABCMeta):
    """Clase padre que permite crear un objeto del tipo persona."""

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

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        return dict(cedula=input_entero_r("Ingrese cédula"),
                    nombre=input_alpha_r("Ingrese Nombre").title(),
                    apellido=input_alpha_r("Ingrese Apellido").title(),
                    direccion=input_alpha("Ingrese Dirección"))

    prompt_init = staticmethod(prompt_init)


# ------------------------------------------------------------------
class Empleado(Persona):
    """Clase extendida de Persona que detalla al empleado"""
    cant_empleado = 0

    def __init__(self, cedula, nombre, apellido, direccion=None, contacto=None, salario=0):
        super().__init__(cedula, nombre, apellido, direccion, contacto)
        self.salario = salario
        self.__class__.cant_empleado += 1

    def actualizarSalario(self, salario):
        self.salario = salario

    def prompt_init(self):
        parent_init = Persona.promp_init()
        datos = Contacto.prompt_init
        contacto = Contacto(**datos)
        salario = input_entero_r("Ingrese Salario")
        parent_init.update({"Contacto": contacto,
                            "Salario": salario})

        prompt_init = staticmethod(self.prompt_init)


# ---------------------------------------------------------------------
class Cliente(Persona):
    """Clase que hereda de persona que detalla a un cliente"""
    cant_cliente = 0

    def __init__(self, cedula, nombre, apellido, direccion, contacto=None, ruc=None,
                 cuentas_bancarias = None):
        super().__init__(cedula, nombre, apellido, direccion, contacto)
        self.ruc = ruc
        self.cuentas_bancarias = []
        self.cuentas_bancarias.append(cuentas_bancarias)
        self.__class__.cant_cliente += 1

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        #TODO contacto no se puede instanciar, crear métodos   de contactos
        parent_init = Persona.prompt_init()
        datos = {"hhh","fff","asfd"} #Contacto.prompt_init()
        #contacto = Contacto(**datos)
        ruc = input_alpha("Ingrese Ruc")
        parent_init.update({"contacto": datos,
                            "ruc": ruc})
        return parent_init

    prompt_init = staticmethod(prompt_init)
