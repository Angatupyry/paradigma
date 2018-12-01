from tkinter import *
from tkinter import messagebox
import Datos.Bd as bd
from Clases.CuentaBancaria import CuentaBancaria
from Clases.Transaccion import Extraccion
from Framework.Util import encontrar_valor


class AddExtraccion(PanedWindow):
    nro_transaccion = None
    fecha = None
    monto = None
    cuenta_nro = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        Label(self, text="Ingrese datos de la extracción", ).grid(row=1, column=2)
        Label(self, text="Nro. de Cuenta*: ").grid(row=2, column=1)
        Label(self, text="Nro. de transacción*: ").grid(row=3, column=1)
        Label(self, text="Fecha: ").grid(row=4, column=1)
        Label(self, text="Monto*: ").grid(row=5, column=1)
        Button(self, text="GUARDAR", command=self.extraer).grid(row=6, column=2)

        self.get_cuenta_nro_entry()
        self.get_nro_transaccion_entry()
        self.get_fecha_entry()
        self.get_monto_entry()

    def get_cuenta_nro_entry(self):
        if not self.cuenta_nro:
            self.cuenta_nro = Entry(master=self, width=20)
            self.cuenta_nro.grid(row=2, column=2)
        return self.cuenta_nro

    def get_nro_transaccion_entry(self):
        if not self.nro_transaccion:
            self.nro_transaccion = Entry(master=self, width=20)
            self.nro_transaccion.grid(row=3, column=2)
        return self.nro_transaccion

    def get_fecha_entry(self):
        if not self.fecha:
            self.fecha = Entry(master=self, width=20)
            self.fecha.grid(row=4, column=2)
        return self.fecha

    def get_monto_entry(self):
        if not self.monto:
            self.monto = Entry(master=self, width=20)
            self.monto.grid(row=5, column=2)
        return self.monto

    def extraer(self):
        ctacte = encontrar_valor(bd.ctacteBancarias, "numero_cuenta", self.get_cuenta_nro_entry().get())
        if ctacte is not None:
            # Diccionario para inicializar el objeto
            nro_transaccion = self.get_nro_transaccion_entry()
            fecha = self.get_fecha_entry()
            monto = self.get_monto_entry().get()
            extraccion = Extraccion(nro_transaccion.get(), fecha.get(), int(monto), ctacte.numero_cuenta)
            # Instancia de la cuenta bancaria para consultar el saldo
            cuenta_cliente = CuentaBancaria(ctacte.numero_cuenta, ctacte.cedula_cliente)
            saldo_actual = cuenta_cliente.obtener_saldo()
            if saldo_actual < int(extraccion.monto):
                messagebox.showinfo("Informacion", "La cuenta no tiene suficiente saldo")
            else:
                extraccion.realizarTransaccion(extraccion.monto, ctacte.numero_cuenta)
                bd.transacciones.append(extraccion)
                messagebox.showinfo("Informacion", "Extracción Realizada")
                self.destroy()
        else:
            messagebox.showinfo("Informacion", "No existe cuenta banciaria")
