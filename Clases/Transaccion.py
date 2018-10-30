from abc import ABCMeta, abstractmethod

import Datos.Bd as bd1
import Framework.AppUtil

from Framework.Util import input_entero_r, encontrar_valor, input_alpha_r


class Transaccion(metaclass=ABCMeta):
    """clase que permite realizar las transacciones de las cuentas"""

    def __init__(self, nro_transaccion, fecha, monto, cuenta_cliente):
        self.nro_transaccion = nro_transaccion
        self.fecha = fecha
        self.monto = monto
        self.cuenta_cliente = cuenta_cliente

    def realizarTransaccion(self, monto, cuenta_bancaria):
        pass


class Deposito(Transaccion):
    def __init__(self, nro_transaccion, fecha, monto, cuenta_cliente):
        super().__init__(nro_transaccion, fecha, monto, cuenta_cliente)

    def realizarTransaccion(self, monto, cuenta_bancaria):
        self.monto = monto
        self.cuenta_cliente = cuenta_bancaria

    def revertir(self):
        a = Deposito(self.nro_transaccion, self.fecha, self.monto * -1, self.cuenta_cliente)
        bd1.transacciones.append(a)

    def prompt_init():
        return dict(nro_transaccion=input_entero_r("Ingrese nro. transaccion: "),
                    fecha=input_entero_r("Ingrese Fecha:"),
                    monto=input_entero_r("Ingrese Monto:"))

    prompt_init = staticmethod(prompt_init)


class Transferencia(Transaccion):
    pass


class Extraccion(Transaccion):
    pass


class Reversible(metaclass=ABCMeta):
    def revertir(self):
        pass

    pass

# TODO MÉTODOS LISTAR PARA TODAS LAS CLASES.
# TODO TRANSACCIONES, AGREGAR TIPOS QUE FALTAN.
# TODO AGREGAR UN MENÚ PARA CONTACTOS, DESDE MENÚ CLIENTES.
# TODO IMPRIMIR OBJETOS.
# TODO AGREGAR VARIABLES CONSTANTES PARA LA CONTABILIDAD
# TODO VOLVER EN TODOS LOS MENÚS.
# TODO MENÚ EMPLEADO, SET SALARIO.
