from Formularios.DepositoForm import AddDeposito
from Formularios.ExtraccionForm import AddExtraccion
from Formularios.TransferenciaForm import AddTransferencia
from Framework.Util import encontrar_valor
from Formularios.ClienteForm import *
from Framework.VistaUtil import list_cliente, list_transacciones

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
        self.__panel_master.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.__panel_master.resizable(0, 0)
        self.__panel_master.config(bg=bgC)
        menubar = Menu(self.__panel_master)
        self.__panel_master.config(menu=menubar)

        # Menú Cliente
        menu_cliente = Menu(menubar, tearoff=0)
        menu_cliente.add_command(label="Agregar cliente", command=self.add_cliente)
        menu_cliente.add_command(label="Listar clientes", command=self.listar_cliente)
        menubar.add_cascade(label="Clientes", menu=menu_cliente)

        # Depósito
        menu_deposito = Menu(menubar, tearoff=0)
        menu_deposito.add_command(label="Depósito", command=self.add_deposito)
        menu_deposito.add_command(label="Revertir Depósito", command=self.add_deposito)

        # Transacciones
        menu_transacciones = Menu(menubar, tearoff=0)
        menu_transacciones.add_cascade(label="Depósito", menu=menu_deposito)
        menu_transacciones.add_command(label="Extracción", command=self.add_extraccion)
        menu_transacciones.add_command(label="Transferencia", command=self.add_transferencia)
        menu_transacciones.add_command(label="Listar Transacciones", command=self.listar_transacciones)
        menubar.add_cascade(label="Transacciones", menu=menu_transacciones)

        # Salir
        menu_opciones = Menu(menubar, tearoff=0)
        menu_opciones.add_command(label="Cerrar Sesión", command=self.cerrar_sesion)
        menu_opciones.add_command(label="Salir", command=self.salir)
        menubar.add_cascade(label="Opciones", menu=menu_opciones)

    def on_exit(self):
        if messagebox.askyesno("Salir", "¿Desea salir de la aplicación?"):
            self.destroy = self.destroy()
            self.salir()

    def cerrar_sesion(self):
        self.limpiar()
        self.__vista_actual = PanelLogin(self.__panel_master)

    def salir(self):
        exit()

    def limpiar(self):
        if self.__vista_actual:
            self.__vista_actual.destroy()

    def add_cliente(self):
        self.limpiar()
        form = AddCliente(self.__panel_master)
        self.__vista_actual = form

    def add_deposito(self):
        self.limpiar()
        form = AddDeposito(self.__panel_master)
        self.__vista_actual = form

    def add_extraccion(self):
        self.limpiar()
        form = AddExtraccion(self.__panel_master)
        self.form = form
        self.__vista_actual = self.form

    def add_transferencia(self):
        self.limpiar()
        form = AddTransferencia(self.__panel_master)
        self.form = form
        self.__vista_actual = self.form

    def listar_cliente(self):
        list_cliente()

    def listar_transacciones(self):
        list_transacciones()


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
        self.__panel_master.title("Login")
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

    def login(self):
        val = encontrar_valor(bd.usuarios, "user", self.user.get())
        if val is not None:
            messagebox.showinfo("", "Login exitoso.")
            self.destroy()
