from functools import reduce
from tkinter import *
from tkinter import messagebox
import Datos.Bd as bd
from Clases.CuentaBancaria import CuentaBancaria
from Clases.Transaccion import Extraccion, Deposito
from Framework.Util import encontrar_valor, encontrar_valor_array


class CuentaBancariaForm(PanedWindow):
    cuenta_nro = None
    cedula_cliente = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        Label(self, text="Cuenta Bancaria", ).grid(row=1, column=2)
        Label(self, text="Nro. de Cuenta*: ").grid(row=2, column=1)
        Button(self, text="Ver Saldo", command=self.procesar).grid(row=6, column=2)

        self.get_cuenta_nro_entry()

    def get_cuenta_nro_entry(self):
        if not self.cuenta_nro:
            self.cuenta_nro = Entry(master=self, width=20)
            self.cuenta_nro.grid(row=2, column=2)
        return self.cuenta_nro

    def procesar(self):
        try:
            if self.get_cuenta_nro_entry().get() != "":
                if messagebox.askyesno("Procesar", "¿Consultar Saldo?"):
                    val = encontrar_valor_array(bd.transacciones, "cuenta_cliente", self.get_cuenta_nro_entry().get())
                    if val is not None:
                        self.obtener_saldo(val)
        except:
            messagebox.showerror("Infor", "No existe Número de cuenta")

    def obtener_saldo(self, dato):
        saldos = self.generador(dato)
        suma_montos = self.sumar_montos(saldos)
        messagebox.showinfo("Resultado", "El saldo de la cuenta es de: " + str(suma_montos))
        self.destroy()

    # Funcional
    # Reduce suma todos los elementos de una lista mediante el método "sumar"
    def sumar_montos(self, lista):
        return reduce(self.sumar, lista)

    def generador(self, dato):
        for transacciones in dato:
            yield transacciones.monto

    def sumar(self, x, y):
        return x + y
