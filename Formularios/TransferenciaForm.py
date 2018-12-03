from tkinter import *
from tkinter import messagebox
import Datos.Bd as bd
from Clases.CuentaBancaria import CuentaBancaria
from Clases.Transaccion import Transferencia
from Framework.Util import encontrar_valor


class AddTransferencia(PanedWindow):
    nro_transaccion = None
    fecha = None
    monto = None
    cuenta_nro = None
    cuenta_destino = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        Label(self, text="Ingrese datos del Depósito", ).grid(row=1, column=2)
        Label(self, text="Nro. de Cuenta*: ").grid(row=2, column=1)
        Label(self, text="Nro. de Cuenta destino*: ").grid(row=3, column=1)
        Label(self, text="Nro. de transacción*: ").grid(row=4, column=1)
        Label(self, text="Fecha: ").grid(row=5, column=1)
        Label(self, text="Monto*: ").grid(row=6, column=1)
        Button(self, text="GUARDAR", command=self.transferir).grid(row=7, column=2)

        self.get_cuenta_nro_entry()
        self.get_cuenta_destino_nro_entry()
        self.get_nro_transaccion_entry()
        self.get_fecha_entry()
        self.get_monto_entry()

    def get_cuenta_nro_entry(self):
        if not self.cuenta_nro:
            self.cuenta_nro = Entry(master=self, width=20)
            self.cuenta_nro.grid(row=2, column=2)
        return self.cuenta_nro

    def get_cuenta_destino_nro_entry(self):
        if not self.cuenta_destino:
            self.cuenta_destino = Entry(master=self, width=20)
            self.cuenta_destino.grid(row=3, column=2)
        return self.cuenta_destino

    def get_nro_transaccion_entry(self):
        if not self.nro_transaccion:
            self.nro_transaccion = Entry(master=self, width=20)
            self.nro_transaccion.grid(row=4, column=2)
        return self.nro_transaccion

    def get_fecha_entry(self):
        if not self.fecha:
            self.fecha = Entry(master=self, width=20)
            self.fecha.grid(row=5, column=2)
        return self.fecha

    def get_monto_entry(self):
        if not self.monto:
            self.monto = Entry(master=self, width=20)
            self.monto.grid(row=6, column=2)
        return self.monto


    def transferir(self):
        ctacte_origen = encontrar_valor(bd.ctacteBancarias, "numero_cuenta", self.get_cuenta_nro_entry().get())
        ctacte_destino = encontrar_valor(bd.ctacteBancarias, "numero_cuenta", self.get_cuenta_destino_nro_entry().get())
        if ctacte_origen is not None and ctacte_destino is not None:
            nro_transaccion = self.get_nro_transaccion_entry().get()
            fecha = self.get_fecha_entry().get()
            monto = self.get_monto_entry().get()
            transferencia_origen = Transferencia(nro_transaccion, fecha, int(monto), ctacte_origen.numero_cuenta)
            transferencia_destino = Transferencia(nro_transaccion, fecha, int(monto), ctacte_destino.numero_cuenta)
            # Instancia de la cuenta bancaria para consultar el saldo
            cuenta_cliente = CuentaBancaria(ctacte_origen.numero_cuenta, ctacte_origen.cedula_cliente)
            saldo_actual = cuenta_cliente.obtener_saldo()

            if saldo_actual < transferencia_origen.monto:
                messagebox.showinfo("Informacion", "No cuenta con suficiente monto, el sobregiro no está permitido.")
            else:
                transferencia_origen.realizarTransaccion(transferencia_origen.monto, ctacte_origen.numero_cuenta)
                transferencia_destino.aumentarCuentaTransferida(monto, ctacte_destino.numero_cuenta)
                bd.transacciones.append(transferencia_origen)
                bd.transacciones.append(transferencia_destino)
                self.destroy()
        else:
            messagebox.showinfo("Informacion", "No existe una cuenta bancaria con ese número de cuenta")
