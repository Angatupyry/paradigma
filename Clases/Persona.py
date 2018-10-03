from abc import ABCMeta
from Clases.Contacto import *
#TODO MÉTODO PROM_INIT_
class Persona(metaclass=ABCMeta):

    def __init__(self, cedula, nombre, apellido, direccion = None, contacto = None):
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
 #------------------------------------------------------------------
class Empleado(Persona):
    """Clase extendida de Persona que detalla al empleado"""
    cant_empleado = 0

    def __init__(self, cedula, nombre, apellido, direccion = None, contacto = None, salario = 0):
        super().__init__(cedula, nombre, apellido, direccion, contacto)
        self.salario = salario
        self.__class__.cant_empleado +=1

# -------------------------------------------------------------------
class Revertidor(Empleado):
    def revertir_transaccion(self):
        pass

#-------------------------------------------------------------------
class Jefe(Empleado):
    """Clase extendida de la clase Empleado"""
    cant_jefe = 0

    def __init__(self, cedula, nombre, apellido, direccion, contacto = None, salario = 0):
        Empleado.__init__(cedula, nombre, apellido, direccion, contacto)
        self.__class__.cant_jefe +=1

    def revertir_transaccion(self):
        pass
#---------------------------------------------------------------------
class Cliente(Persona):
    """Clase que hereda de persona que detalla a un cliente"""
    cant_cliente = 0
    def __init__(self, cedula, nombre, apellido, direccion, contacto = None, ruc = None):
        super().__init__(cedula, nombre, apellido, direccion, contacto)
        self.ruc = ruc
        self.__class__.cant_cliente += 1



