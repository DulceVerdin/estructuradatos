from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.nodo import Node
from estructuras.lineales.convercion import ConvertidorExpresiones

class LoadInterfazPila(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/untitled.ui', self)

        # Ya no usamos LinkedList, solo la pila
        self.operaciones = Node([])  
        self.convertidor = ConvertidorExpresiones()

        # Conectar botón de conversión
        self.btn_convertir.clicked.connect(self.convertir_infija_a_posfija)
        
    def convertir_infija_a_posfija(self):
        expresion_infija = self.txt_exprecion.text()
        if not expresion_infija.strip():
            self.lbl_resultado.setText("Ingrese una expresión válida.")
            return
        
        try:
            resultado_posfija = self.convertidor.infija_a_posfija(expresion_infija)
            self.lbl_resultado.setText(resultado_posfija)
        except Exception as e:
            self.lbl_resultado.setText(f"Error: {str(e)}")