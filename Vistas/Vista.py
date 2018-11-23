from Framework.Util import encontrar_valor
from Formularios.ClienteForm import *
bgC = "black"
p_pri = "700x400+150+100"
p_sec = "500x300+250+180"


class PanelPrincipal(Frame):
    """Panel principal que contiene el menu con las llamadas a las funciones
    del programa"""
    __vista_actual = None

    def __init__(self, panel_master):
        Frame.__init__(self, panel_master)
        self.__panel_master = panel_master
        self.__vista_actual = PanelLogin(panel_master)
        self.inicializar()
        self.pack()

    def inicializar(self):
        self.__panel_master.geometry(p_pri)
        self.__panel_master.title("MENU PRINCIPAL")
        self.__panel_master.protocol("WM_DELETE_WINDOW", "onexit")
        self.__panel_master.resizable(0, 0)
        self.__panel_master.config(bg=bgC)
        menubar = Menu(self.__panel_master)
        self.__panel_master.config(menu=menubar)

        # Menú Cliente
        menu_cliente = Menu(menubar, tearoff=0)
        menu_cliente.add_command(label="Agregar cliente", command=self.add_cliente)
        menu_cliente.add_command(label="Eliminar cliente", command=self.del_cliente)
        menu_cliente.add_command(label="Listar clientes", command=self.listar_cliente)
        menu_cliente.add_command(label="Agregar contacto a cliente", command=self.edit_cliente)
        menubar.add_cascade(label="Clientes", menu=menu_cliente)

class PanelLogin(PanedWindow):
    """Panel de login"""
    user = None
    password = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()
        self.grab_set()  # deshabilita las otras ventanas hasta que esta se destruya

    def inicializar(self):
        self.__panel_master.geometry(p_pri)
        self.__panel_master.title("MENU Login")
        self.__panel_master.protocol("WM_DELETE_WINDOW", "onexit")
        self.__panel_master.resizable(0, 0)
        self.__panel_master.config(bg=bgC)
        Label(self, text="Usuario").grid(row=1, column=1)
        Label(self, text="Contraseña: ").grid(row=2, column=1)
        Button(self, text="Login", command=self.login).grid(row=3, column=2)

        self.get_user()
        self.get_password()

    def get_user(self):
        if not self.user:
            self.user = Entry(master=self, textvariable=StringVar())
            self.user.grid(row=1, column=2)
            return self.user

    def get_password(self):
        if not self.password:
            self.password = Entry(master=self, textvariable=StringVar(), show="•")
            self.password.grid(row=2, column=2)
        return self.password

