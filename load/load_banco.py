from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

from estructuras.lineales.banco import Banco


class LoadBanco(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi("ui/banco.ui", self)

        self.banco = Banco()

        self.btn_turno.clicked.connect(self.turno)
        self.btn_atender.clicked.connect(self.atender)
        self.btn_cerrar.clicked.connect(self.cerrar)

    def turno(self):

        mensaje = self.banco.agregarCliente()

        self.lbl_mensaje.setText(mensaje)

        # Solo mostrar el siguiente turno si el banco sigue abierto
        if not self.banco.banco_cerrado:
            self.txt_cliente.setText(str(self.banco.turno))

        self.txt_lista_espera.setPlainText(
            self.banco.mostrarCola()
        )

    def atender(self):

        mensaje = self.banco.atenderCliente()

        self.lbl_mensaje.setText(mensaje)

        self.txt_lista_espera.setPlainText(
            self.banco.mostrarCola()
        )

        self.lbl_cant_atendidos.setText(
            str(self.banco.clientes_atendidos)
        )

        self.lbl_promedio.setText(
            f"{self.banco.promedio():.2f} seg"
        )

    def cerrar(self):

        mensaje = self.banco.cerrarBanco()

        self.lbl_mensaje.setText(mensaje)

        # Ya NO se cierra la ventana