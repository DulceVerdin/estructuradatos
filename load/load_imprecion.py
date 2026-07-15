from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic
from estructuras.lineales.cola_imprecion import GestorImpresion

class LoadColaImpresion(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("ui/impresion.ui", self)
        self.gestor = GestorImpresion()

        # Conectar botones
        self.btn_agregar.clicked.connect(self.agregar_trabajo)
        self.btn_imprimir.clicked.connect(self.imprimir_siguiente)
        self.btn_consultar.clicked.connect(self.consultar_frente)

    def agregar_trabajo(self):
        usuario = self.txt_usuario.text().strip()
        documento = self.txt_documento.text().strip()
        try:
            paginas = int(self.txt_paginas.text())
        except ValueError:
            self.lbl_mensajes.setText("Error: número de páginas inválido.")
            return

        resultado = self.gestor.agregar_trabajo(usuario, documento, paginas)
        self.lbl_mensajes.setText(resultado)
        self.actualizar_tabla()

    def imprimir_siguiente(self):
        resultado = self.gestor.imprimir_siguiente()
        self.lbl_mensajes.setText(resultado)
        self.actualizar_tabla()

    def consultar_frente(self):
        resultado = self.gestor.consultar_frente()
        self.lbl_mensajes.setText(resultado)

    def actualizar_tabla(self):
        trabajos = self.gestor.listar_trabajos()
        self.tbl_trabajos.clear()
        self.tbl_trabajos.setRowCount(0)
        if trabajos == "La cola está vacía.":
            self.lbl_total.setText("0 trabajos pendientes")
            return

        elementos = trabajos.split(" -> ")
        self.tbl_trabajos.setRowCount(len(elementos))
        for i, elem in enumerate(elementos):
            self.tbl_trabajos.setItem(i, 0, self.ui.tbl_trabajos.item(i, 0))
            self.tbl_trabajos.setItem(i, 0, self.tbl_trabajos.item(i, 0))
            self.tbl_trabajos.setItem(i, 0, self.tbl_trabajos.item(i, 0))
        self.lbl_total.setText(f"{len(elementos)} trabajos pendientes")