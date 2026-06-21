import sys
from PyQt5.QtWidgets import QApplication
from load.load_MenuPrincipal import MenuPrincipal  # Ajusta la ruta si es necesario

def main():
    # 1. PASO CRUCIAL: Crear la aplicación primero pasándole los argumentos del sistema
    app = QApplication(sys.argv)
    
    # 2. PASO SECUNDARIO: Instanciar tu ventana principal una vez que existe app
    ventana = MenuPrincipal()
    ventana.show()
    
    # 3. Mantener la aplicación corriendo en bucle hasta que se cierre
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()