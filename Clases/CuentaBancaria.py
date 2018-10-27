class CuentaBancaria():
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
