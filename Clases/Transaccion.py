from abc import ABCMeta


class Transaccion(metaclass=ABCMeta):
    """clase que permite realizar las transacciones de las cuentas"""

    def __init__(self, nro_transaccion, fecha, cuenta_cliente_banco, cuenta_cliente,
                 monto, banco):
        self.numero_transaccion = nro_transaccion
        self.fecha = fecha
        # self.cuenta_cliente_banco = cuenta_cliente_banco
        self.cuenta_cliente = cuenta_cliente
        self.monto = monto
        # self.banco = banco

    def realizarTransaccion(self):
        pass


class Deposito(Transaccion):
    def __init__(self, nro_transaccion, fecha, cuenta_cliente, monto):
        super().__init__(self, nro_transaccion, fecha, cuenta_cliente, monto)

    def realizarTransaccion(self, monto, cuenta_bancaria):
        self.monto = monto
        self.cuenta_cliente = cuenta_bancaria


class Transferencia(Transaccion):
    pass


class Extraccion(Transaccion):
    pass


class Reversible(Deposito):
    def revertir(self):
        pass

    pass
