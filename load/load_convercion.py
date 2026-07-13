from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.convercion import ConvertidorExpresiones

class LoadInterfazPila(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/untitled.ui', self)

        self.convertidor = ConvertidorExpresiones()

        # Conexión de los botones individuales
        self.btn_convertir.clicked.connect(self.convertir_infija_a_posfija)
        self.btn_evaluar.clicked.connect(self.evaluar_expresion)
        
    def convertir_infija_a_posfija(self):
        expresion_infija = self.txt_exprecion.text() 
        
        if not expresion_infija.strip():
            self.lbl_resultado.setText("Inválida")
            return
        
        try:
            # 1. Convierte la expresión
            resultado_posfija = self.convertidor.infija_a_posfija(expresion_infija)
            
            # 2. Muestra SOLO la cadena posfija al lado de "Expresion posfija:"
            self.lbl_resultado.setText(resultado_posfija)
            
            # Limpia el resultado de abajo para esperar el botón "Evaluar"
            self.lbl_resultado2.setText("")
            
        except Exception as e:
            self.lbl_resultado.setText(f"Error")

    def evaluar_expresion(self):
        # Lee la expresión posfija que ya está en la etiqueta del medio
        expresion_posfija = self.lbl_resultado.text()
        
        # Validaciones de control por si presionan evaluar antes de convertir
        if not expresion_posfija.strip() or expresion_posfija in ("0", "Inválida", "Error"):
            self.lbl_resultado2.setText("Primero convierta.")
            return

        try:
            # 1. Evalúa usando la pila matemáticamente
            resultado_evaluacion = self.convertidor.evaluar_posfija(expresion_posfija)
            
            # 2. Muestra SOLO el número final en la etiqueta de abajo
            self.lbl_resultado2.setText(str(resultado_evaluacion))
            
        except Exception as e:
            self.lbl_resultado2.setText(f"Error al evaluar")