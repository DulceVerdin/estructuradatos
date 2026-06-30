
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


#PDF, EXPLICACION, PROMTS, EVIDENCIA