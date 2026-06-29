from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from load.load_interfaz import LoadInterfaz 
from load.load_stack import DialogoPila
from load.load_convercion import LoadInterfazPila

class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/MenuPrincipal.ui', self)
        
        # Conectar acción del menú
        self.actionLista_Enlazada.triggered.connect(self.abrir_interfaz)
        self.actionPila_2.triggered.connect(self.abrir_stack)
        self.actionconvercion_infija_posfija.triggered.connect(self.abrir_convercion)
        
    def abrir_interfaz(self):
        self.interfaz = LoadInterfaz()
        self.interfaz.exec()

    def abrir_stack(self):
        self.stack = DialogoPila()
        self.stack.exec()

    def abrir_convercion(self):
        self.convercion = LoadInterfazPila()
        self.convercion.exec()
    
    
