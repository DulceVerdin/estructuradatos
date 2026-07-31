from graphviz import Digraph
from estructuras.lineales.stack import Stack
from estructuras.no_lineales.NodeTree import NodeTree
from binarytree import Node as BTNode

class ExpressionTree:
    def __init__(self):
        self.root = None

    def build_expression_tree(self, postfix_expr: str) -> bool:
        """Construye el árbol de expresión a partir de una cadena postfija."""
        stack = Stack()
        tokens = postfix_expr.strip().split()
        operadores = {'+', '-', '*', '/', '^'}

        if not tokens:
            print("Error: La expresión está vacía.")
            return False

        for token in tokens:
            if token not in operadores:
                nodo = NodeTree(token)
                stack.push(nodo)
            else:
                if stack.is_empty():
                    print(f"Error: Expresión postfija inválida. Falta operando para '{token}'.")
                    return False
                
                derecho = stack.top.value if hasattr(stack.top, 'value') else stack.top.data
                stack.pop()

                if stack.is_empty():
                    print(f"Error: Expresión postfija inválida. Faltan operandos para '{token}'.")
                    return False
                
                izquierdo = stack.top.value if hasattr(stack.top, 'value') else stack.top.data
                stack.pop()

                nodo_operador = NodeTree(token)
                nodo_operador.left = izquierdo
                nodo_operador.right = derecho

                stack.push(nodo_operador)

        if stack.is_empty():
            print("Error: No se pudo construir el árbol.")
            return False
        
        self.root = stack.top.value if hasattr(stack.top, 'value') else stack.top.data
        stack.pop()

        if not stack.is_empty():
            print("Error: Expresión postfija mal formada (sobran operandos).")
            self.root = None
            return False

        return True
    def _convertir_a_binarytree(self, node):
        """Convierte recursivamente los nodos a la estructura de binarytree."""
        if node is None:
            return None
        bt_node = BTNode(str(node.value))
        bt_node.left = self._convertir_a_binarytree(node.left)
        bt_node.right = self._convertir_a_binarytree(node.right)
        return bt_node

    def generar_grafico_binarytree(self):
        """Muestra el árbol dibujado en la consola usando binarytree."""
        if self.root is None:
            print("El árbol está vacío. No se puede generar la gráfica.")
            return

        arbol_visual = self._convertir_a_binarytree(self.root)
        print("\n=== ÁRBOL DIBUJADO EN CONSOLA ===")
        print(arbol_visual)
    # --- RECORRIDOS QUE RETORNAN 'STR' ---

    def preorden(self) -> str:
        res = []
        self._preorden(self.root, res)
        return " ".join(res)

    def _preorden(self, node, res):
        if node is not None:
            res.append(str(node.value))
            self._preorden(node.left, res)
            self._preorden(node.right, res)

    def posorden(self) -> str:
        res = []
        self._posorden(self.root, res)
        return " ".join(res)

    def _posorden(self, node, res):
        if node is not None:
            self._posorden(node.left, res)
            self._posorden(node.right, res)
            res.append(str(node.value))

    def inorden_parentizado(self) -> str:
        res = []
        self._inorden_parentizado(self.root, res)
        return "".join(res)

    def _inorden_parentizado(self, node, res):
        if node is not None:
            if node.left is None and node.right is None:
                res.append(str(node.value))
            else:
                res.append("(")
                self._inorden_parentizado(node.left, res)
                res.append(f" {node.value} ")
                self._inorden_parentizado(node.right, res)
                res.append(")")

    # --- GRÁFICA ---

    def generar_grafico(self, nombre_archivo="arbol_expresion"):
        if self.root is None:
            print("El árbol está vacío. No se puede generar la gráfica.")
            return

        dot = Digraph(comment="Árbol de Expresión")
        dot.attr('node', shape='circle', style='filled', color='skyblue', fontname='Arial')

        def agregar_nodos_y_aristas(node):
            if node is not None:
                node_id = str(id(node))
                dot.node(node_id, str(node.value))

                if node.left:
                    left_id = str(id(node.left))
                    dot.node(left_id, str(node.left.value))
                    dot.edge(node_id, left_id)
                    agregar_nodos_y_aristas(node.left)

                if node.right:
                    right_id = str(id(node.right))
                    dot.node(right_id, str(node.right.value))
                    dot.edge(node_id, right_id)
                    agregar_nodos_y_aristas(node.right)

        agregar_nodos_y_aristas(self.root)

        try:
            dot.render(nombre_archivo, format="png", cleanup=True)
            print(f" Gráfica guardada como '{nombre_archivo}.png'.")
        except Exception as e:
            print(f" Nota sobre gráfica: {e}")

    # --- EVALUACIÓN / CÁLCULO DEL RESULTADO ---

    def evaluar(self) -> float:
        """
        Calcula el resultado numérico de la expresión evaluando 
        el árbol de forma recursiva.
        """
        if self.root is None:
            print("El árbol está vacío. No se puede evaluar.")
            return 0.0
        return self._evaluar(self.root)

    def _evaluar(self, node) -> float:
        # Caso base: Si es una hoja (operando), convertimos su valor a número
        if node.left is None and node.right is None:
            return float(node.value)

        # Evaluar recursivamente los subárboles izquierdo y derecho
        izq = self._evaluar(node.left)
        der = self._evaluar(node.right)

        # Aplicar el operador correspondiente
        if node.value == '+':
            return izq + der
        elif node.value == '-':
            return izq - der
        elif node.value == '*':
            return izq * der
        elif node.value == '/':
            if der == 0:
                raise ZeroDivisionError("Error: División entre cero detectada en el árbol.")
            return izq / der
        elif node.value == '^':
            return izq ** der

        raise ValueError(f"Operador no soportado: {node.value}")