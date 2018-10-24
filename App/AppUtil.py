from Clases.Persona import Cliente, Empleado
from Framework.Util import *
import Datos.Bd as bd


class AppUtil:
    def __init__(self):
        cargar_datos()

    # Cliente
    def add_cliente(self):
        cls_()
        bd.clientes.append(Cliente(**Cliente.prompt_init()))

    def inactivar_cliente(self):
        dato = encontrar_valor(bd.clientes, "cedula", input_alpha_r("Ingrese numero de cedula "))
        if dato:
            self.inactivar_cliente(bd.clientes, dato)


    # Funciones
    def inactivar_cliente(self, lista, dato):
        if lista:
            resp = input_option("Desea eliminar el dato?", "si", "no")
            if resp == "si":
                lista.remove(dato)
                print("Cliente Inactivado")
            else:
                print("Petición Cancelada")
        else:
            print("No se enonctró")


    # Menú
    def menu(self):
        """Menú principal"""
        while True:
            cls()
            print("-----------------------------------------------------------")
            print("--------------------MENU--PRINCIPAL------------------------")
            print()

    # arrays de menús
    array_clientes = {}
    array_clientes[1] = {"t": "Agregar cliente", "f": add_cliente}
    array_clientes[2] = {"t": "Inactivar cliente", "f": inactivar_cliente}
    array_clientes[3] = {"t": "Listar clientes", "f": listar_clientes}
    array_clientes[4] = {"t": "Volver", "f": menu}
