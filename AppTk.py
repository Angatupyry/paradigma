import tkinter as tk
from Vistas.Vista import PanelPrincipal
from InicializarDatos.CargaDatos import inicializar_datos

inicializar_datos()
root = tk.Tk()
vista_principal = PanelPrincipal(root)
root.mainloop()
root.destroy()