import Datos.Bd as bd
from Clases.Persona import Cliente, Telefono, Empleado
from Clases.CuentaBancaria import CuentaBancaria
from Clases.Transaccion import Deposito, Reversible, Extraccion
from Framework.Util import *


class AppUtil:
    def __init__(self):
        # Abre los archivos binarios pickle
        cargar_datos()

    # Cliente
    def add_cliente(self):
        cls_()
        bd.clientes.append(Cliente(**Cliente.prompt_init()))

    def inactivar_cliente(self):
        dato = encontrar_valor(bd.clientes, "cedula", input_alpha_r("Ingrese numero de cedula "))
        if dato:
            self.inactivar(bd.clientes, dato)

    def listar_clientes(self):
        self.listar_datos(bd.clientes)

    # Empleado
    def add_empleado(self):
        cls_()
        bd.empleados.append(Empleado(**Empleado.prompt_init()))

    def inactivar_empleado(self):
        dato = encontrar_valor(bd.empleados, "cedula", input_alpha_r("Ingrese número de cédula "))
        if dato:
            self.inactivar(bd.empleados, dato)

    def listar_empleado(self):
        self.listar_datos(bd.empleados)

    def actualizar_salario(self):
        e = encontrar_valor(bd.empleados, "cedula", input_alpha_r("Ingrese número de cédula: "))
        if e:
            salario_nuevo = input_entero_r("Ingrese nuevo salario")
            e.actualizarSalario(salario_nuevo)
        else:
            print("No se encuentra empleado")

    # Cuenta Bancaria
    def add_cuenta_bancaria(self):
        """Agregar una cuenta bancaria para un cliente."""
        # Debe existir un cliente para agregar una cuenta bancaria.
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

    # Transacciones
    def listar_transacciones(self):
        self.listar_datos(bd.transacciones)

    # Depósito
    def new_deposito(self):
        """Realizar un depósito a una cuenta bancaria"""
        cls_()
        ctacte = encontrar_valor(bd.ctacteBancarias, "numero_cuenta", input_alpha_r("Nro Cuenta:"))
        if ctacte is not None:
            deposito = Deposito.prompt_init()
            deposito.update({"cuenta_cliente": ctacte.numero_cuenta})
            add_deposito = Deposito(**deposito)
            transferencia = encontrar_valor(bd.transacciones, "nro_transaccion", add_deposito.nro_transaccion)
            if transferencia is None:
                bd.transacciones.append(add_deposito)
            else:
                print("Ya existe una transacción con ese número.")
        else:
            print("No existe una cuenta bancaria con ese número de cuenta")

    def revertir(self):
        deposito = encontrar_valor(bd.transacciones, "nro_transaccion", input_entero_r("Número de transacción:"))
        if deposito is not None:
            deposito.revertir()
            print("Transacción: " + str(deposito.nro_transaccion) + " revertido")
        else:
            print("No se encontró ningún depósito con ese número de transacción")

    # Extracción
    def extraer(self):
        cls_()
        ctacte = encontrar_valor(bd.ctacteBancarias, "numero_cuenta", input_alpha_r("Nro Cuenta:"))
        if ctacte is not None:
            #Diccionario para inicializar el objeto
            dic_ext = Extraccion.prompt_init()
            dic_ext.update({"cuenta_cliente": ctacte.numero_cuenta})
            extraccion = Extraccion(**dic_ext)
            #Instancia de la cuenta bancaria para consultar el saldo
            cuenta_cliente = CuentaBancaria(ctacte.numero_cuenta, ctacte.cedula_cliente)
            saldo_actual = cuenta_cliente.obtener_saldo()
            if saldo_actual < extraccion.monto:
                print("No cuenta con suficiente monto, el sobregiro no está permitido")
            else:
                extraccion.realizarTransaccion(extraccion.monto, ctacte.numero_cuenta)
                bd.transacciones.append(extraccion)
        else:
            print("No existe una cuenta bancaria con ese número de cuenta")

    # Funciones Úitles
    def inactivar(self, lista, dato):
        if lista:
            resp = input_option("¿Desea eliminar el dato?", ("si", "no"))
            if resp == "si":
                lista.remove(dato)
                print("Dato eliminado")
            else:
                print("Petición Cancelada")
        else:
            print("Dato no encontrado")

    def listar_datos(self, lista, pausar=True):
        """Permiste listar datos de distintas clases, el valor booleano
        sirve para imprimir sin pasusas"""
        if lista:
            print()
            cont = 1
            for val in lista:
                print(("-----------------=={}==-----------------".format(cont)))
                print_objeto(val)
                print()
                if (cont % 5) is 0:
                    if pausar:
                        input("Presione enter para continuar...")
                cont += 1
            if pausar:
                input("Presione enter para volver al menú...")
        else:
            input("\nSin datos. \nPresione enter para continuar...")

    # Menú Principal
    def menu(self):
        """Menú principal"""
        while True:
            cls()
            print("-----------------------------------------------------------")
            print("--------------------MENÚ--PRINCIPAL------------------------")
            print()
            for key in list(self.o_principal.keys()):
                print(("{} - {}".format(key, self.o_principal[key]["t"])))
            print()
            opcion = input_range("Ingrese una opción", 1, self.o_principal.__len__())
            self.o_principal[int(opcion)]["f"](self)

    def salir(self):
        exit()

    def menu_list(self, text, dic):
        """Presenta el menú con las opciones principales"""
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
        self.menu_list("CLIENTES", self.o_clientes)

    def menu_empleados(self):
        self.menu_list("CLIENTES", self.o_empleados)

    def menu_cuentas(self):
        self.menu_list("CUENTAS_BANCARIAS", self.o_cuentas)

    def menu_transacciones(self):
        self.menu_list("TRANSACCIONES", self.o_transacciones)

    def menu_deposito(self):
        self.menu_list("DEPOSITO", self.o_deposito)

    o_principal = {}
    o_principal[1] = {"t": "Menú de Clientes", "f": menu_clientes}
    o_principal[2] = {"t": "Menú de Empleados", "f": menu_empleados}
    o_principal[3] = {"t": "Menú de Cuentas Bancarias", "f": menu_cuentas}
    o_principal[4] = {"t": "Menú de Transacciones", "f": menu_transacciones}

    o_clientes = {}
    o_clientes[1] = {"t": "Agregar cliente", "f": add_cliente}
    o_clientes[2] = {"t": "Inactivar cliente", "f": inactivar_cliente}
    o_clientes[3] = {"t": "Listar clientes", "f": listar_clientes}
    o_clientes[4] = {"t": "Volver", "f": menu}
    o_clientes[5] = {"t": "Salir", "f": salir}

    o_empleados = {}
    o_empleados[1] = {"t": "Agregar empleado", "f": add_empleado}
    o_empleados[2] = {"t": "Inactivar empleado", "f": inactivar_empleado}
    o_empleados[3] = {"t": "Listar empleado", "f": listar_empleado}
    o_empleados[4] = {"t": "Actualizar Salario", "f": actualizar_salario}
    o_empleados[5] = {"t": "Volver", "f": menu}
    o_empleados[6] = {"t": "Salir", "f": salir}

    o_cuentas = {}
    o_cuentas[1] = {"t": "Agregar Cuenta", "f": add_cuenta_bancaria}
    o_cuentas[2] = {"t": "Consultar Saldo", "f": obtener_saldo}
    o_cuentas[3] = {"t": "Volver", "f": menu}
    o_cuentas[4] = {"t": "Salir", "f": salir}

    o_transacciones = {}
    o_transacciones[1] = {"t": "Depósito", "f": menu_deposito}
    o_transacciones[2] = {"t": "Extracción", "f": extraer}
    o_transacciones[3] = {"t": "Listar transacciones", "f": listar_transacciones}
    o_transacciones[4] = {"t": "Volver", "f": menu}

    o_deposito = {}
    o_deposito[1] = {"t": "Nuevo Depósito", "f": new_deposito}
    o_deposito[2] = {"t": "Revertir Depósito", "f": revertir}
    o_deposito[3] = {"t": "Volver", "f": menu}
    o_deposito[4] = {"t": "Salir", "f": salir}
