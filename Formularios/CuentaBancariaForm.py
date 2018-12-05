from functools import reduce
from tkinter import *
from tkinter import messagebox
import Datos.Bd as bd
from Clases.CuentaBancaria import CuentaBancaria
from Clases.Transaccion import Extraccion, Deposito
from Framework.Util import encontrar_valor


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
                if messagebox.askyesno("Procesar", "Procesar solicitud?"):
                    val = encontrar_valor(bd.ctacteBancarias, "numero_cuenta", self.get_cuenta_nro_entry().get())
                    if val is not None:
                        self.calc(val)
        except:
            messagebox.showerror("Infor", "No existe Número de cuenta")

    # Funcion que calcula los valores para procesar una solicitud
    def calc(self, dato):
        montos = self.generador(dato)
        suma_montos = self.calc_monto(montos)
        messagebox.showinfo("Resultado", "Cliente: " + str(suma_montos))
        self.destroy()

    # Utilizamos la funcion reduce para sumar todos los elementos de una lista
    # --------------Parte equivalente a programacion funcional----------------
    def calc_monto(self, lista):
        return reduce(self.sumar, lista)

    def generador(self, dato):
        for transacciones in dato.transacciones:
                yield transacciones.monto

    def sumar(self, x, y):
        return x + y

