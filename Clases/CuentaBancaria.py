import Datos.Bd as bd1

from Framework.Util import encontrar_valor_array


class CuentaBancaria:
    def __init__(self, numero_cuenta, cedula_cliente, transacciones=None):
        self.numero_cuenta = numero_cuenta
        self.cedula_cliente = cedula_cliente
        self.transacciones = []
        self.transacciones.append(transacciones)

    def obtener_saldo(self):
        transacciones = encontrar_valor_array(bd1.transacciones, "cuenta_cliente", self.numero_cuenta)
        if transacciones.__len__() > 0:
            saldo = 0
            for transaccion in transacciones:
                saldo += int(transaccion.monto)
            return saldo
        else:
            return -1
