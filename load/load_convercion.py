'''
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.convercion import ConvertidorExpresiones

class LoadInterfazPila(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/untitled.ui', self)

        self.convertidor = ConvertidorExpresiones()

        # Conectar botón de conversión
        self.btn_convertir.clicked.connect(self.convertir_infija_a_posfija)
        
    def convertir_infija_a_posfija(self):
        expresion_infija = self.txt_exprecion.text()  # corregido
        if not expresion_infija.strip():
            self.lbl_resultado.setText("Ingrese una expresión válida.")
            return
        
        try:
            resultado_posfija = self.convertidor.infija_a_posfija(expresion_infija)
            self.lbl_resultado.setText(resultado_posfija)
        except Exception as e:
            self.lbl_resultado.setText(f"Error: {str(e)}")
'''
'''
def evaluar_posfija(self, expresion_posfija):
        # 1. Aseguramos que la pila esté vacía antes de iniciar
        while not self.pila.is_empty():
            self.pila.pop()

        # 2. Separamos la expresión por espacios (tu método anterior lo dejó así)
        tokens = expresion_posfija.split()

        for token in tokens:
            if token.isdigit():
                # Si es un dígito, lo convertimos a entero y lo apilamos
                self.pila.push(int(token))
            else:
                # Es un operador. Extraemos los dos últimos elementos.
                # REGLA DE ORO: El primer pop() es el operando DERECHO, el segundo es el IZQUIERDO.
                derecho = self.pila.pop()
                izquierdo = self.pila.pop()

                # Realizamos la operación matemática sin usar eval()
                if token == '+':
                    resultado = izquierdo + derecho
                elif token == '-':
                    resultado = izquierdo - derecho
                elif token == '*':
                    resultado = izquierdo * derecho
                elif token == '/':
                    # Usamos división normal (o // si tu profesor exige enteros)
                    resultado = izquierdo / derecho
                elif token == '$':
                    resultado = izquierdo ** derecho
                else:
                    raise ValueError(f"Operador no soportado: {token}")

                # Apilamos el resultado parcial para seguir evaluando
                self.pila.push(resultado)

        # 3. Al final, el único valor restante en la pila es el resultado final
        return self.pila.pop()
'''
'''
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.convercion import ConvertidorExpresiones

class LoadInterfazPila(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/untitled.ui', self)

        self.convertidor = ConvertidorExpresiones()

        # Conectar botón de conversión
        self.btn_convertir.clicked.connect(self.convertir_infija_a_posfija)
        
    def convertir_infija_a_posfija(self):
        expresion_infija = self.txt_exprecion.text() 
        
        if not expresion_infija.strip():
            self.lbl_resultado.setText("Ingrese una expresión válida.")
            return
        
        try:
            # 1. Convertimos a posfija
            resultado_posfija = self.convertidor.infija_a_posfija(expresion_infija)
            
            # 2. Evaluamos la expresión posfija obtenida
            resultado_evaluacion = self.convertidor.evaluar_posfija(resultado_posfija)
            
            # 3. Mostramos ambos resultados en la interfaz
            # \n se usa para poner el resultado en la línea de abajo
            texto_salida = f"Posfija: {resultado_posfija}\nResultado: {resultado_evaluacion}"
            self.lbl_resultado2.setText(texto_salida)
            
        except Exception as e:
            self.lbl_resultado2.setText(f"Error: {str(e)}")
'''
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