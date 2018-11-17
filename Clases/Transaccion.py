from abc import ABCMeta, abstractmethod

import Datos.Bd as bd1

from Framework.Util import input_entero_r


class Transaccion(metaclass=ABCMeta):
    """clase que permite realizar las transacciones de las cuentas"""

    def __init__(self, nro_transaccion, fecha, monto, cuenta_cliente):
        self.nro_transaccion = nro_transaccion
        self.fecha = fecha
        self.monto = monto
        self.cuenta_cliente = cuenta_cliente

    @abstractmethod
    def realizarTransaccion(self, monto, cuenta_bancaria):
        pass


class Deposito(Transaccion):
    def __init__(self, nro_transaccion, fecha, monto, cuenta_cliente):
        super().__init__(nro_transaccion, fecha, monto, cuenta_cliente)

    def realizarTransaccion(self, monto, cuenta_bancaria):
        self.monto = monto
        self.cuenta_cliente = cuenta_bancaria

    def revertir(self):
        d = Deposito(self.nro_transaccion, self.fecha, self.monto * -1, self.cuenta_cliente)
        bd1.transacciones.append(d)


class Transferencia(Transaccion):
    pass


class Extraccion(Transaccion):
    def __init__(self, nro_transaccion, fecha, monto, cuenta_cliente):
        super().__init__(nro_transaccion, fecha, monto, cuenta_cliente)

    def realizarTransaccion(self, monto, cuenta_bancaria):
        self.monto = monto * -1
        self.cuenta_cliente = cuenta_bancaria


class Reversible(metaclass=ABCMeta):
    def revertir(self):
        pass

    pass
