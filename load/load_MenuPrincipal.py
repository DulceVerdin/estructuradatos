
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from load.load_interfaz import LoadInterfaz 
from load.load_stack import DialogoPila
from load.load_convercion import LoadInterfazPila
from load.load_queue import LoadInterfazQueue
from load.load_banco import LoadBanco
from load.load_imprecion import   LoadColaImpresion
from load.load_binarytree import LoadEvaluadorArbol


class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/MenuPrincipal.ui', self)
        
        # Conectar acción del menú
        self.actionLista_Enlazada.triggered.connect(self.abrir_interfaz)
        self.actionPila_2.triggered.connect(self.abrir_stack)
        self.actionconvercion_infija_posfija.triggered.connect(self.abrir_convercion)
        self.actionQueue.triggered.connect(self.abrir_queue)
        self.actionBanco.triggered.connect(self.abrir_banco)
        self.actionGestor_de_impresion.triggered.connect(self.abrir_impresion)
        self.actionbinarytree.triggered.connect(self.abrir_evaluador_arbol)
        
    def abrir_interfaz(self):
        self.interfaz = LoadInterfaz()
        self.interfaz.exec()

    def abrir_stack(self):
        self.stack = DialogoPila()
        self.stack.exec()

    def abrir_convercion(self):
        self.convercion = LoadInterfazPila()
        self.convercion.exec()

    def abrir_queue(self):
        self.queue = LoadInterfazQueue()
        self.queue.exec()

    def abrir_banco(self):
      self.banco = LoadBanco()
      self.banco.exec()
    
    def abrir_evaluador_arbol(self):
        self.evaluador_arbol = LoadEvaluadorArbol()
        self.evaluador_arbol.exec()

    def abrir_impresion(self):
        self.impresion = LoadColaImpresion()
        self.impresion.exec()







        