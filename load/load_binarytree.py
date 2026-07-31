import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QMessageBox
from estructuras.no_lineales.arbol import ExpressionTree


class LoadEvaluadorArbol(QDialog):

    def __init__(self):
        super().__init__()

        # Ruta dinámica absoluta hacia el archivo .ui
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ui_path = os.path.join(base_dir, "ui", "interfaz_arbol.ui")

        # Cargar la interfaz
        uic.loadUi(ui_path, self)

        # Conectar eventos de los botones de la interfaz
        self.btn_procesar.clicked.connect(self.procesar_expresion)
        self.btn_limpiar.clicked.connect(self.limpiar_campos)
        self.btn_salir.clicked.connect(self.close)

    def procesar_expresion(self):
        expresion = self.txt_input.text().strip()

        if not expresion:
            QMessageBox.warning(
                self, "Atención", "Por favor ingresa una expresión postfija."
            )
            return

        try:
            # 1. Crear instancia del árbol de expresión
            tree = ExpressionTree()

            # 2. Construir el árbol a partir de la expresión postfija ingresada
            exito = tree.build_expression_tree(expresion)

            if not exito:
                QMessageBox.warning(
                    self,
                    "Expresión Inválida",
                    "No se pudo construir el árbol.\nVerifica que la expresión postfija esté bien formada (ejemplo: '3 4 +').",
                )
                return

            # 3. Obtener los recorridos desde la clase ExpressionTree
            inorden = tree.inorden_parentizado()
            preorden = tree.preorden()
            posorden = tree.posorden()

            # 4. Evaluar el resultado numérico
            resultado = tree.evaluar()

            # Formatear a entero si es un número flotante exacto (ej. 7.0 -> 7)
            if isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)

            # 5. Generar la representación gráfica en ASCII usando binarytree
            bt_root = tree._convertir_a_binarytree(tree.root)
            dibujo_arbol = str(bt_root) if bt_root else ""

            # 6. Reflejar los resultados en la interfaz gráfica
            self.lbl_inorden.setText(str(inorden))
            self.lbl_preorden.setText(str(preorden))
            self.lbl_posorden.setText(str(posorden))
            self.lbl_resultado.setText(str(resultado))
            self.txt_tree.setPlainText(dibujo_arbol)

        except ZeroDivisionError as e:
            QMessageBox.critical(self, "Error Matemático", str(e))
        except Exception as e:
            QMessageBox.critical(
                self, "Error", f"Ocurrió un error al procesar:\n{str(e)}"
            )

    def limpiar_campos(self):
        self.txt_input.clear()
        self.lbl_inorden.setText("-")
        self.lbl_preorden.setText("-")
        self.lbl_posorden.setText("-")
        self.lbl_resultado.setText("-")
        self.txt_tree.clear()