
'''
from estructuras.lineales.stack import Node
from estructuras.lineales.lista_enlazada_simple import LinkedList

class ConvertidorExpresiones:
    def __init__(self):
        self.pila = Node (LinkedList())

    def prioridad(self, operador):
        if operador == '$':   # Potencia
            return 3
        if operador in ('*', '/'):
            return 2
        if operador in ('+', '-'):
            return 1
        return 0
    
    def infija_a_posfija(self, expresion):
        salida = []
        for token in expresion:
            if token.isalnum():
                salida.append(token)
            elif token == '(':
                self.pila.pila_agregar(token)
            elif token == ')':
                while not self.pila.is_empty() and self.pila.pila_tope() != '(':
                    salida.append(self.pila.pila_eliminar())
                self.pila.pila_eliminar()
            else:
                while (not self.pila.is_empty() and 
                       self.prioridad(self.pila.pila_tope()) >= self.prioridad(token)):
                    salida.append(self.pila.pila_eliminar())
                self.pila.pila_agregar(token)

        while not self.pila.is_empty():
            salida.append(self.pila.pila_eliminar())

        return " ".join(salida)


'''
'''
from estructuras.lineales.stack import Stack

class ConvertidorExpresiones:
    def __init__(self):
        self.pila = Stack()

    def prioridad(self, operador):
        if operador == '$':   # Potencia
            return 3
        if operador in ('*', '/'):
            return 2
        if operador in ('+', '-'):
            return 1
        return 0
    
    def infija_a_posfija(self, expresion):
        salida = []
        for token in expresion:
            if token.isalnum():
                salida.append(token)
            elif token == '(':
                self.pila.push(token)
            elif token == ')':
                while not self.pila.is_empty() and self.pila.top_of_stack() != '(':
                    salida.append(self.pila.pop())
                self.pila.pop()  # eliminar '('
            else:
                while (not self.pila.is_empty() and 
                       self.prioridad(self.pila.top_of_stack()) >= self.prioridad(token)):
                    salida.append(self.pila.pop())
                self.pila.push(token)

        while not self.pila.is_empty():
            salida.append(self.pila.pop())

        return " ".join(salida)

'''
from estructuras.lineales.stack import Stack

class ConvertidorExpresiones:
    def __init__(self):
        self.pila = Stack()

    def prioridad(self, operador):
        if operador == '$':   
            return 3
        if operador in ('*', '/'):
            return 2
        if operador in ('+', '-'):
            return 1
        return 0
    
    def infija_a_posfija(self, expresion):
        salida = []
        for token in expresion:
            # === MODIFICACIÓN: Ignorar espacios en blanco ===
            if token == ' ':
                continue
            # ===============================================
            
            if token.isalnum():
                salida.append(token)
            elif token == '(':
                self.pila.push(token)
            elif token == ')':
                while not self.pila.is_empty() and self.pila.top_of_stack() != '(':
                    salida.append(self.pila.pop())
                self.pila.pop() # eliminar 'I'
            else:
                while (not self.pila.is_empty() and 
                       self.prioridad(self.pila.top_of_stack()) >= self.prioridad(token)):
                    salida.append(self.pila.pop())
                self.pila.push(token)

        while not self.pila.is_empty():
            salida.append(self.pila.pop())

        return " ".join(salida)

    def evaluar_posfija(self, expresion_posfija):
        # 1. Aseguramos que la pila esté vacía antes de iniciar
        while not self.pila.is_empty():
            self.pila.pop()

        # 2. Separamos la expresión por espacios
        tokens = expresion_posfija.split()

        for token in tokens:
            if token.isdigit():
                # Si es un dígito, lo convertimos a entero y lo apilamos
                self.pila.push(int(token))
            else:
                # Es un operador. Extraemos los dos últimos elementos.
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
                    # Usamos división clásica
                    resultado = izquierdo / derecho
                elif token == '$':
                    resultado = izquierdo ** derecho
                else:
                    raise ValueError(f"Operador no soportado: {token}")

                # Apilamos el resultado parcial
                self.pila.push(resultado)

        # 3. Al final, el único valor restante en la pila es el resultado
        return self.pila.pop()