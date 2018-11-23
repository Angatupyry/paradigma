from tkinter import *
from tkinter import messagebox
import Datos.Bd as bd
from Clases.Persona import Cliente
from Framework.Util import encontrar_valor


class AddCliente(PanedWindow):
    cedula_entry = None
    nombre_entry = None
    apellido_entry = None

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

