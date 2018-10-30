from pickle import dump

from Clases.Banco import *
from Clases.Persona import *
from Clases.CuentaBancaria import CuentaBancaria
from Clases.Transaccion import Deposito


def inicializar_datos():
    """Datos precargados en el sistema"""
    path = "/home/fierro/Desktop/paradigma/Datos"
    #path = "/home/cba/Escritorio/paradigma/Datos"  # CBA

    # Clientes
    a = Cliente(3828622, "Ariel", "Curtido", "Asunción")
    bd.clientes.append(a)
    bd.clientes.append(Cliente(2, "César", "Rolón", "Capiatá"))
    bd.clientes.append(Cliente(3, "Tamara", "Ocampos", "Fdo. de la Mora", None, "111111111-1"))
    bd.clientes.append(Cliente(4, "Arnaldo", "Perez", "Asunción", None, "222222222-2"))
    bd.clientes.append(Cliente(5, "Adrian", "Recalde", "Villa Elisa"))
    f = abrir(path + "/clientes", "wb")
    dump(bd.clientes, f)
    f.close()

    # CtacteBancaroas
    bd.ctacteBancarias.append(CuentaBancaria(800, 2))
    f = abrir(path + "/ctacteBancarias", "wb")
    dump(bd.ctacteBancarias, f)
    f.close()

    # Transacciones
    bd.transacciones.append(Deposito(10, 34, 45000, 800))
    bd.transacciones.append(Deposito(9, 34, 45000,800 ))
    f = abrir(path + "/transacciones", "wb")
    dump(bd.transacciones, f)
    f.close()