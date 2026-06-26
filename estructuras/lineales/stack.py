from estructuras.lineales.nodo import Node

class Stack(object):
    def __init__(self):
        self.top = None

    def push(self, data):
        
        nuevo = Node(data)
        nuevo.next = self.top
    
        self.top = nuevo

    def pop(self):
        if self.top is None:
            return None

        valor = self.top.data
        self.top = self.top.next

        # Paso 4: Retornar el valor extraído (como dice la flecha verde: 'return valor')
        return valor

    def top_of_stack(self):
        # Verificar si la pila no tiene elementos
        if self.top is None:
            return None
        
        # Retorna el valor del nodo en la cima pero SIN quitarlo de la pila
        return self.top.data

    def print_stack(self):
        # Verificar si está vacía
        if self.top is None:
            return None
            
    
        temp = self.top
        print("--- Cima de la Pila ---")
        while temp is not None:
            print(f"[ {temp.data} ]")
            temp = temp.next
        print("-----------------------")