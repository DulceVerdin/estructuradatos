from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.queue import Queue

class LoadInterfazQueue(QDialog):
    def __init__(self):
        super().__init__()
        # Cargar el archivo .ui
        self.ui = uic.loadUi('ui/interfazQueve.ui', self)

        # Instancia de la cola
        self.cola = Queue()

        # Conectar botones a métodos
        self.btn_enqueue.clicked.connect(self.enqueue)
        self.btn_dequeue.clicked.connect(self.dequeue)
        self.btn_fristqueue.clicked.connect(self.firstQueue)
        self.btn_lastqueue.clicked.connect(self.lastQueue)
        self.btn_printqueve.clicked.connect(self.printQueue)
        self.btn_isempty.clicked.connect(self.isEmpty)

    def enqueue(self):
        dato = self.txt_dato.text()
        if dato.strip() == "":
            self.lbl_resultado.setText("Debes ingresar un valor.")
            return
        self.cola.enqueue(dato)
        self.lbl_resultado.setText(self.cola.resultado)
        self.txt_dato.clear()

    def dequeue(self):
        eliminado = self.cola.dequeue()
        self.lbl_resultado.setText(self.cola.resultado)

    def firstQueue(self):
        primero = self.cola.firstQueue()
        self.lbl_resultado.setText(self.cola.resultado)

    def lastQueue(self):
        ultimo = self.cola.lastQueue()
        self.lbl_resultado.setText(self.cola.resultado)

    def printQueue(self):
        contenido = self.cola.printQueue()
        self.lbl_resultado.setText(contenido)

    def isEmpty(self):
        if self.cola.isEmpty():
            self.lbl_resultado.setText("La cola está vacía.")
        else:
            self.lbl_resultado.setText("La cola tiene elementos.")