import sys
from PyQt5.QtWidgets import QApplication 
from load.load_MenuPrincipal import MenuPrincipal  

def main():
    app = QApplication(sys.argv)
    
    ventana = MenuPrincipal()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()