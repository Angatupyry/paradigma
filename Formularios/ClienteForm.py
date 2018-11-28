from tkinter import *
from tkinter import messagebox
import Datos.Bd as bd
from Clases.Persona import Cliente
from Framework.Util import encontrar_valor


class AddCliente(PanedWindow):
    cedula_entry = None
    nombre_entry = None
    apellido_entry = None
    direccion_entry = None
    ruc_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master = panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        Label(self, text="Ingrese datos del Cliente").grid(row=1, column=2)
        Label(self, text="Cédula*: ").grid(row=2, column=1)
        Label(self, text="Nombre*: ").grid(row=3, column=1)
        Label(self, text="Apellido*: ").grid(row=4, column=1)
        Label(self, text="Dirección: ").grid(row=5, column=1)
        Label(self, text="Ruc: ").grid(row=6, column=1)
        Button(self, text="GUARDAR", command=self.a_cli).grid(row=7, column=3)

        self.get_cedula_entry()
        self.get_nombre_entry()
        self.get_apellido_entry()
        self.get_direccion_entry()
        self.get_ruc_entry()

    def get_cedula_entry(self):
        if not self.cedula_entry:
            self.cedula_entry = Entry(master=self, width=20)
            self.cedula_entry.grid(row=2, column=2)
        return self.cedula_entry

    def get_nombre_entry(self):
        if not self.nombre_entry:
            self.nombre_entry = Entry(master=self, width=20)
            self.nombre_entry.grid(row=3, column=2)
        return self.nombre_entry

    def get_apellido_entry(self):
        if not self.apellido_entry:
            self.apellido_entry = Entry(master=self, width=20)
            self.apellido_entry.grid(row=4, column=2)
        return self.apellido_entry

    def get_direccion_entry(self):
        if not self.direccion_entry:
            self.direccion_entry = Entry(master=self, width=20)
            self.direccion_entry.grid(row=5, column=2)
        return self.direccion_entry

    def get_ruc_entry(self):
        if not self.ruc_entry:
            self.ruc_entry = Entry(master=self, width=20)
            self.ruc_entry.grid(row=6, column=2)
        return self.ruc_entry

    def a_cli(self):
        try:
            ced = self.get_cedula_entry().get()
            nom = self.get_nombre_entry().get()
            ape = self.get_apellido_entry().get()
            dre = self.get_direccion_entry().get()
            ruc = self.get_ruc_entry().get()

            bd.clientes.append(Cliente(ced, nom, ape, dre, ruc))
            messagebox.showinfo("Informacion", "Cliente agregado")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Error", e)