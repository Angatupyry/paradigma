from tkinter import *
from tkinter import messagebox
from datetime import datetime
from Clases.Persona import Cliente, Empleado
import Datos.Bd as bd
from Vistas import Vista

bgC = "black"
fgC = "black"
bgBC = "white"
p_sal_pri = "700x400+150+100"
p_sal_sec = "500x300+250+180"

def list_datos(datos):
    """Genera una ventana que muestra los datos de una lista con scrollbar"""
    ventana = Tk()
    ventana.title("Lista")
    ventana.resizable(0, 0)
    ventana.geometry(p_sal_sec)

    Label(ventana, text="Detalle de los datos", ).pack()

    def colocar_scrollbar(listbox, scrollbar):
        scrollbar.config(command=listbox.yview)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox.pack(side=LEFT, fill=Y)

    frame1 = Frame(ventana, bd=5, height=600, width=350)
    frame1.pack()
    #700x400+150+100
    scroll1 = Scrollbar(frame1)
    list1 = Listbox(frame1, width=70, height=20)
    list1.pack()
    colocar_scrollbar(list1, scroll1)

    def cargarlistbox(lista, listbox):
        ind, largo = 0, len(lista)
        while ind < largo:
            listbox.insert(END, lista[ind])
            ind += 1
    #ventana.focus_set()
    #ventana.grab_set()
    #OBS: trate de crear un focus permanente en esta ventana para tener que
    #cerrarla para seguir usando el programa pero no logre hacerlo
    ventana.overrideredirect(1)
    cargarlistbox(datos, list1)
    ventana.mainloop()


def list_cliente():
    """Genera una lista con los datos de los clientes"""
    datos = ['------======DETALLE CLIENTES======------']
    bucle = 1
    for cli in bd.clientes:
        datos.append("{}- Cédula: {}".format(bucle, cli.cedula))
        datos.append("     Nombre: {}".format(cli.nombre))
        datos.append("     Apellido: {}".format(cli.apellido))
        datos.append("     Dirección: {}".format(cli.direccion))
        datos.append("     Ruc: {}".format(cli.ruc))
        datos.append("")
        datos.append("")
        bucle += 1
    list_datos(datos)