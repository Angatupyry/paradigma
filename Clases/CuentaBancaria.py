import Datos.Bd as bd1

from Framework.Util import input_entero_r, encontrar_valor, input_alpha_r


class CuentaBancaria:
    def __init__(self, numero_cuenta, cedula_cliente, transacciones=None):
        self.numero_cuenta = numero_cuenta
        self.cedula_cliente = cedula_cliente
        self.transacciones = []
        self.transacciones.append(transacciones)

    def obtener_saldo(self):
        saldo = 0
        if self.transacciones:
            for transaccion in self.transacciones:
                saldo += transaccion.monto
        return saldo

    def prompt_init():
        """Hola"""
        return dict(numero_cuenta=input_entero_r("Ingrese nro. de Cuenta: "),
                    cedula_cliente=encontrar_valor(bd1.clientes, "cedula",
                                                   input_alpha_r("Ingrese Cédula del cliente")))

    prompt_init = staticmethod(prompt_init)
