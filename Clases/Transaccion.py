
class Transaccion:
    """clase que permite realizar las transacciones de las cuentas"""
    def __init__(self, nro_transaccion, fecha, cuenta_cliente_banco, cuenta_cliente,
                 monto, es_cheque, banco):
        self.numero_transaccino = nro_transaccion
        self.fecha = fecha
        self.cuenta_cliente_banco = cuenta_cliente_banco
        self.cuenta_cliente = cuenta_cliente
        self.monto = monto
        self.es_cheque = es_cheque
        self.banco = banco

