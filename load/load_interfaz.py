from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from menus.menu_lista_enlazada import (
    AgregarInicio, AgregarFinal, BuscarElemento,
    MostrarLista, EliminarPrimerElemento, EliminarUltimoElemento
)
from estructuras.lineales.lista_enlazada_simple import LinkedList

class LoadInterfaz(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/interfaz.ui', self)
        self.lista = LinkedList()

        # Conectar botones
        self.btn_agregarI.clicked.connect(self.agregar_inicio)
        self.btn_agregarf.clicked.connect(self.agregar_final)
        self.btn_imprimir.clicked.connect(self.imprimir)
        self.btn_buscar.clicked.connect(self.buscar)
        self.btn_eliminari.clicked.connect(self.eliminar_inicio)
        self.btn_eliminarf.clicked.connect(self.eliminar_final)

    def agregar_inicio(self):
        texto = self.txt_dato.text().strip()
        if texto:
            accion = AgregarInicio(self.lista) 
            accion.ejecutar(texto)
            self.lbl_resultado.setText(f"Elemento '{accion.elemento}' agregado al inicio.")
            self.txt_dato.clear() 
        else:
            self.lbl_resultado.setText("Por favor, ingrese un valor válido.")

    def agregar_final(self):
        texto = self.txt_dato.text().strip()
        if texto:
            accion = AgregarFinal(self.lista)
            accion.ejecutar(texto)
            self.lbl_resultado.setText(f"Elemento '{accion.elemento}' agregado al final.")
            self.txt_dato.clear()
        else:
            self.lbl_resultado.setText("Por favor, ingrese un valor válido.")

    def imprimir(self):
        accion = MostrarLista(self.lista)
        accion.ejecutar()
        self.lbl_resultado.setText(accion.resultado)

    def buscar(self):
        texto = self.txt_dato.text().strip()
        if texto:
            accion = BuscarElemento(self.lista)
            accion.ejecutar(texto)
            self.lbl_resultado.setText(accion.resultado)
        else:
            self.lbl_resultado.setText("Ingrese el elemento que desea buscar.")

    def eliminar_inicio(self):
        accion = EliminarPrimerElemento(self.lista)
        accion.ejecutar()
        self.lbl_resultado.setText(accion.resultado)

    def eliminar_final(self):
        accion = EliminarUltimoElemento(self.lista)
        accion.ejecutar()
        self.lbl_resultado.setText(accion.resultado)