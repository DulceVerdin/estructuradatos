from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.stack import Stack
from estructuras.lineales.lista_enlazada_simple import (
    PushElemento,
    PopElemento,
    TopOfStackElemento, 
    MostrarPila
)

class DialogoPila(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/interfazPila.ui', self)

        self.pila = Stack()

        # Conexión de botones (AJUSTA nombres si cambian en tu .ui)
        self.btn_push.clicked.connect(self.push)
        self.btn_pop.clicked.connect(self.pop)
        self.btn_top.clicked.connect(self.top)
        self.btn_print.clicked.connect(self.mostrar)

    def push(self):
        texto = self.txt_dato.text().strip()

        if texto:
            accion = PushElemento(self.pila)
            accion.ejecutar(texto)

            self.lbl_resultado.setText(f"Elemento '{texto}' agregado a la pila.")
            self.txt_dato.clear()
        else:
            self.lbl_resultado.setText("Ingrese un valor válido.")

    def pop(self):
        accion = PopElemento(self.pila)
        accion.ejecutar()
        self.lbl_resultado.setText(accion.resultado)

    def top(self):
        accion = TopOfStackElemento(self.pila)
        accion.ejecutar()
        self.lbl_resultado.setText(accion.resultado)

    def mostrar(self):
        accion = MostrarPila(self.pila)
        accion.ejecutar()
        self.lbl_resultado.setText(accion.resultado)