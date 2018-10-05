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