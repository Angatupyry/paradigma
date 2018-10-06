import os
from calendar import weekday
from datetime import datetime, timedelta
from pickle import load, loads, dump, dumps
from Clases import Contacto
def cls():
    os.system("clear")

def cls():
    os.system("clear")
    print("\n\n Ingrese datos ")
    print("\n\n Ingrese datos ")

def input_range(text, men, may):
    while True:
        valor = input("{} ({}-{}) *: ".format(text, men, may))
        try:
            valor = int(valor)
            if(valor <= may and valor >= men):
                return valor
            else:
                raise(ValueError)
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