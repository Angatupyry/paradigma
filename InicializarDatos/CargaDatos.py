from pickle import dump
from datetime import datetime, date
from Clases.Banco import *
from Clases.Persona import *
from Clases.CuentaBancaria import CuentaBancaria
from Clases.Transaccion import Deposito


def inicializar_datos():
    """Datos precargados en el sistema"""
    path = "/home/fierro/Desktop/paradigma/Datos"
    #path = "/home/cba/Escritorio/paradigma/Datos"  # CBA

    # Clientes
    bd.clientes.append(Cliente(3828622, "Ariel", "Curtido", "Asunción"))
    bd.clientes.append(Cliente(2, "César", "Rolón", "Capiatá"))
    f = abrir(path + "/clientes", "wb")
    dump(bd.clientes, f)
    f.close()

    # Empleado
    bd.empleados.append(Empleado(1, "Juan", "Pérez", "Asunción",None,2000000))
    bd.empleados.append(Empleado(2, "Rodrigo", "Aquino", "Capiatá",None,4000000))
    f = abrir(path + "/empleados", "wb")
    dump(bd.empleados, f)
    f.close()

    # CtacteBancaroas
    bd.ctacteBancarias.append(CuentaBancaria(800, 2))
    bd.ctacteBancarias.append(CuentaBancaria(900, 1))
    f = abrir(path + "/ctacteBancarias", "wb")
    dump(bd.ctacteBancarias, f)
    f.close()

    # Transacciones
    bd.transacciones.append(Deposito(10, datetime.now(), 45000, 800))
    bd.transacciones.append(Deposito(9, datetime.now(), 45000,800))
    bd.transacciones.append(Deposito(11, datetime.now(), 45000, 900))
    f = abrir(path + "/transacciones", "wb")
    dump(bd.transacciones, f)
    f.close()
