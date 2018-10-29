import Datos.Bd as bd
from Clases.Persona import Cliente
from Clases.CuentaBancaria import CuentaBancaria
from Clases.Transaccion import Deposito
from Framework.Util import *


class AppUtil:
    def __init__(self):
        cargar_datos()

    # Cliente
    def add_cliente(self):
        cls_()
        bd.clientes.append(Cliente(**Cliente.prompt_init()))
        print("-------CREAR CUENTA BANCARIA-------")
        cuenta = CuentaBancaria(**CuentaBancaria.prompt_init())

    def inactivar_cliente(self):
        dato = encontrar_valor(bd.clientes, "cedula", input_alpha_r("Ingrese numero de cedula "))
        if dato:
            self.inactivar(bd.clientes, dato)

    def listar_clientes(self):
        self.listar_datos(bd.clientes)

    # Cuenta Bancaria
    def add_cuenta_bancaria(self):
        """Agregar una cuenta bancaria para un cliente."""
        cls_()
        cliente = encontrar_valor(bd.clientes, "cedula", input_alpha_r("Cédula cliente:"))
        if cliente is not None:
            ctacte = CuentaBancaria(input_entero_r("Ingrese número de cuenta"), cliente.cedula)
            bd.ctacteBancarias.append(ctacte)
        else:
            print("Cliente no encontrado")

    def obtener_saldo(self):
        cls_()
        cuentabancaria = encontrar_valor(bd.ctacteBancarias, "numero_cuenta", input_alpha_r("Ingrese número de cuenta"))
        if cuentabancaria is not None:
            print(cuentabancaria.obtener_saldo())
        else:
            print("No existe cuenta")

    # Depósito
    def new_deposito(self):
        bd.transacciones.append(Deposito.prompt_init())

    # Funciones
    def inactivar(self, lista, dato):
        if lista:
            resp = input_option("Desea eliminar el dato?", ("si", "no"))
            if resp == "si":
                lista.remove(dato)
                print("Cliente Inactivado")
            else:
                print("Petición Cancelada")
        else:
            print("No se enonctró")

    def listar_datos(self, lista, pausar=True):
        """Permiste listar datos de distintas clases, el valor booleano
        sirve para imprimir sin pasusas"""
        if lista:
            print()
            cont = 1
            for val in lista:
                print(("-----------------=={}==-----------------".format(cont)))
                # val.mostrar_datos()
                print_objeto(val)
                print()
                if (cont % 5) is 0:
                    if pausar:
                        input("Presione enter para continuar...")
                cont += 1
            if pausar:
                input("Presione enter para volver al menu...")
        else:
            input("\nSin datos. \nPresione enter para continuar...")

    # Menú
    def menu(self):
        """Menú principal"""
        while True:
            cls()
            print("-----------------------------------------------------------")
            print("--------------------MENU--PRINCIPAL------------------------")
            print()
            for key in list(self.o_principal.keys()):
                print(("{} - {}".format(key, self.o_principal[key]["t"])))
            print()
            opcion = input_range("Ingrese una opción", 1, self.o_principal.__len__())
            self.o_principal[int(opcion)]["f"](self)

    def salir(self):
        exit()

    def menu_list(self, text, dic):
        """Presenta el menu con las o_principal"""
        while True:
            cls()
            print(("\n------------------{}--------------------------\n".
                   format("MENÚ --" + text)))
            for key in list(dic.keys()):
                print(("{} - {}".format(key, dic[key]["t"])))
            print()
            opcion = input_range("Ingrese una opción", 1, dic.__len__())
            dic[int(opcion)]["f"](self)

    def menu_clientes(self):
        self.menu_list("CLIENTES", self.array_clientes)

    def menu_cuentas(self):
        self.menu_list("CUENTAS_BANCARIAS", self.o_cuentas)

    def menu_transacciones(self):
        self.menu_list("TRANSACCIONES", self.o_transacciones)

    def menu_deposito(self):
        self.menu_list("DEPOSITO", self.o_deposito)

    # arrays de menús
    array_clientes = {}
    array_clientes[1] = {"t": "Agregar cliente", "f": add_cliente}
    array_clientes[2] = {"t": "Inactivar cliente", "f": inactivar_cliente}
    array_clientes[3] = {"t": "Listar clientes", "f": listar_clientes}
    array_clientes[4] = {"t": "Volver", "f": menu}
    array_clientes[5] = {"t": "Salir", "f": salir}

    o_cuentas = {}
    o_cuentas[1] = {"t": "Agregar Cuenta", "f": add_cuenta_bancaria}
    o_cuentas[2] = {"t": "Consultar Saldo", "f": obtener_saldo}
    o_cuentas[3] = {"t": "Salir", "f": salir}

    o_principal = {}
    o_principal[1] = {"t": "Menú de Clientes", "f": menu_clientes}
    o_principal[2] = {"t": "Menú de Cuentas Bancarias", "f": menu_cuentas}
    o_principal[3] = {"t": "Menú de Transacciones", "f": menu_transacciones}

    o_transacciones = {}
    o_transacciones[1] = {"t": "Depósito", "f": menu_deposito}

    o_deposito = {}
    o_deposito[1] = {"t": "Nuevo Depósito", "f": new_deposito}
    o_deposito[2] = {"t": "Salir", "f": salir}
