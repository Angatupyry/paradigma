from Clases.Persona import *
from Clases.Transaccion import *
from Clases.Banco import *
from pickle import dump


def inicializarDatos():
    """Datos precargados en el sistema"""
    path = "/home/fierro/Desktop/paradigma/Datos"

    cliente = Cliente(22342, "César", "Rolón", "Asunción")
    bd.clientes.append(cliente)
    f = abrir(path, "clientes", "wb")
    dump(bd.clientes, f)
    f.close()
