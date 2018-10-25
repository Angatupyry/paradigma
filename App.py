from Framework.AppUtil import AppUtil
from InicializarDatos.CargaDatos import inicializar_datos

if __name__ == "__main__":
    inicializar_datos()
    app = AppUtil()
    app.menu()

