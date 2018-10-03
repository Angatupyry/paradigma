from abc import ABCMeta

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