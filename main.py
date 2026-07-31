import sys
from PyQt5 import QtWidgets
from load.load_MenuPrincipal import MenuPrincipal



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # Creamos la instancia de tu Menú Principal
    ventana = MenuPrincipal()
    ventana.show()
    
    sys.exit(app.exec_())