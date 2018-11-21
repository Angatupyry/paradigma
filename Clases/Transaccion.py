from abc import ABCMeta, abstractmethod

import Datos.Bd as bd1


class Transaccion(metaclass=ABCMeta):

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
    def __init__(self, nro_transaccion, fecha, monto, cuenta_cliente):
        super().__init__(nro_transaccion, fecha, monto, cuenta_cliente)

    def realizarTransaccion(self, monto, cuenta_bancaria):
        self.monto = monto * -1
        self.cuenta_cliente = cuenta_bancaria

    def aumentarCuentaTransferida(self, monto, cuenta_bancaria):
        self.monto = monto
        self.cuenta_cliente = cuenta_bancaria


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
