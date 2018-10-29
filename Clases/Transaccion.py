from abc import ABCMeta, abstractmethod
import Datos.Bd as bd1

from Framework.Util import input_entero_r, encontrar_valor, input_alpha_r


class Transaccion(metaclass=ABCMeta):
    """clase que permite realizar las transacciones de las cuentas"""

    def __init__(self, nro_transaccion, fecha, cuenta_cliente,
                 monto):
        self.numero_transaccion = nro_transaccion
        self.fecha = fecha
        self.cuenta_cliente = cuenta_cliente
        self.monto = monto

    @abstractmethod
    def realizarTransaccion(self, monto, cuenta_bancaria):
        pass


class Deposito(Transaccion):
    def __init__(self, nro_transaccion, fecha, cuenta_cliente, monto):
        super().__init__(nro_transaccion, fecha, cuenta_cliente, monto)

    def realizarTransaccion(self, monto, cuenta_bancaria):
        self.monto = monto
        self.cuenta_cliente = cuenta_bancaria

    def prompt_init():
        """Hola"""
        return dict(nro_transaccion=input_entero_r("Ingrese nro. transaccion: "),
                    fecha=input_entero_r("Ingrese Fecha:"),
                    cuenta_cliente=input_entero_r("Ingrese cuenta cliente:"),
                    monto=input_entero_r("Ingrese Monto:"))

    prompt_init = staticmethod(prompt_init)

class Transferencia(Transaccion):
    pass


class Extraccion(Transaccion):
    pass


class Reversible(Deposito):
    def revertir(self):
        pass

    pass
