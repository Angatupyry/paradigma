import os
from pickle import load, dump

import Datos.Bd as bd

#path = "/home/fierro/Desktop/paradigma/Datos"
path = "/home/cba/Escritorio/paradigma/Datos"  # CBA

def cls():
    """Permite limpiar la consola de python para que sea mas comodo usarla"""
    os.system("clear")


def cls_():
    """Permite limpiar la consola de python para que sea mas comodo usarla
       Muestra un mensaje"""
    cls()
    print("\n\n--==Ingrese datos (Campos con * son obligatorios)==--\n")

def input_range(text, men, may):
    """ Solicita un valor entero dentro de un rango y se devuelve
        Se introduce el texto a mostrar y el rango de valor minimo y maximo"""
    while True:
        valor = input("{} ({}-{}) *: ".format(text, men, may))
        try:
            valor = int(valor)
            if (valor <= may and valor >= men):
                return valor
            else:
                raise ValueError
        except ValueError:
            pass

def input_option(text, opciones):
    """Solicita un valor, debe estar presente en la lista de opciones"""
    text += " ({})*: ".format(", ".join(opciones))
    val = input(text)
    while val.lower() not in opciones:
        val = input(text)
    return val.lower()

def input_entero(text):
    while True:
        valor = input("{}: ".format(text))
        try:
            valor = int(valor)
            return valor
        except ValueError:
            if(valor is ""):
                return  None

def input_entero_r(text):
    """ Solicita un valor entero y lo devuelve. (es requerido)
        Mientras el valor ingresado no sea entero, vuelve a solicitarlo. """
    while True:
        valor = input("{} *: ".format(text))
        try:
            valor = int(valor)
            return valor
        except ValueError:
            pass

def input_alpha(text):
    """ Solicita una cadena"""
    while True:
        valor = input("{}: ".format(text))
        try:
            return valor
        except ValueError:
            pass

def input_alpha_r(text):
    """ Solicita una cadena (requerido)"""
    while True:
        valor = input("{} *: ".format(text))
        try:
            if valor is not "":
                return valor
            else:
                raise (ValueError)
        except ValueError:
            pass

def abrir(path, modo):
    """Recibe una direccion y modo de apertura de archivo/fichero
    y retorna el archivo"""
    try:
        f = open(path,modo)
    except:
        print("Verifique, no se pudo encontrar el archivo "+path)
    else:
        return f

def cargar(f):
    """Recibe un fichero con un objeto serializado, retorna el objeto"""
    try:
        obj = load(f)
    except:
        return []
    else:
        return obj

def encontrar_valor(lista, identificador, text):
    for val in lista:
        existe = getattr(val, identificador)
        if str(existe) == text:
            return val

    return print("Cliente no encontrado")

def guardar_datos():
    f1 = abrir(path + "/empleados", "wb")
    dump(bd.empleados, f1)
    f1.close()

    f1 = abrir(path + "/clientes", "wb")
    dump(bd.clientes, f1)
    f1.close()

    f1 = abrir(path + "/transacciones", "wb")
    dump(bd.transacciones, f1)
    f1.close()

def cargar_datos():
    #f1 = abrir(path + "/empleados", "rb")
    #dump(bd.empleados, f1)
    #f1.close()

    f1 = abrir(path + "/clientes", "rb")
    bd.clientes = cargar(f1)
    f1.close()

    #f1 = abrir(path + "/transacciones", "rb")
    #dump(bd.transacciones, f1)
    #f1.close()

def print_objeto(objeto):
    objeto = vars(objeto)
    for dato in objeto:
        if objeto[dato] is not None and objeto[dato] != [None] and objeto[dato] != "":
            print(dato[0].upper() + dato[1:] + ":", objeto[dato])