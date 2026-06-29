from estructuras.lineales.nodo import Node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data):
        # Paso 1: Crear un nuevo nodo con el dato proporcionado
        new_node = Node(data)

        # Paso 2: Verificar si la lista está vacía
        if self.head is None and self.tail is None:
            # Si la lista está vacía, el nuevo nodo se convierte en la cabeza y la cola
            self.head = new_node
            self.tail = new_node
        else:
            # Si la lista no está vacía, el nuevo nodo apunta a la cabeza actual
            new_node.next = self.head
            # Luego, la cabeza se actualiza para ser el nuevo nodo
            self.head = new_node
    
    def insert_at_end(self, data):
        # Paso 1: Crear un nuevo nodo con el dato proporcionado
        new_node = Node(data)

        # Paso 2: Verificar si la lista está vacía
        if self.head is None and self.tail is None:
            # Si la lista está vacía, el nuevo nodo se convierte en la cabeza y la cola
            self.head = new_node
            self.tail = new_node
        else:
            # Si la lista no está vacía, el nodo actual de la cola apunta al nuevo nodo
            self.tail.next = new_node
            # Luego, la cola se actualiza para ser el nuevo nodo
            self.tail = new_node

    def delete_at_beginning(self):
        # Caso 1: La lista está vacía
        if self.head is None:
            return None

        data_eliminado = self.head.data

        # Caso 2: La lista tiene un solo elemento
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # Caso 3: La lista tiene dos o más elementos
            self.head = self.head.next

        return data_eliminado

    def delete_at_end(self):
        # Caso 1: La lista está vacía
        if self.head is None:
            return None

        data_eliminado = self.tail.data

        # Caso 2: La lista tiene un solo elemento
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return data_eliminado

        # Caso 3: La lista tiene dos o más elementos
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next

        temp.next = None
        self.tail = temp

        return data_eliminado

    def search(self, data):
        # Paso 1: Iniciar un nodo temporal en la cabeza de la lista
        temp = self.head
        # Paso 2: Recorrer la lista mientras el nodo temporal no sea None
        while temp is not None:
            # Paso 3: Comparar el dato del nodo temporal con el dato buscado
            if temp.data == data:
                # Paso 4: Si se encuentra el dato, retornar True
                return True
            else:
                # Paso 5: Si no se encuentra el dato, avanzar al siguiente nodo
                temp = temp.next
        # Paso 6: Si se recorre toda la lista sin encontrar el dato, retornar False        
        return False

    def print_linked_list(self):
        temp = self.head
        print("Head ->", end="")
        while temp is not None:
            print(f" {temp.data} ->", end="")
            temp = temp.next
        print("<- Tail")

#--------Pila-------


class PushElemento:
    def __init__(self, pila):
        self.pila = pila
        self.elemento = ""

    def ejecutar(self, elemento):
        self.elemento = elemento
        self.pila.push(elemento)


class PopElemento:
    def __init__(self, pila):
        self.pila = pila
        self.resultado = ""

    def ejecutar(self):
        eliminado = self.pila.pop()
        if eliminado is not None:
            self.resultado = f"Elemento '{eliminado}' extraído de la pila."
        else:
            self.resultado = "La pila está vacía. Nada que extraer (Stack Underflow)."


class TopOfStackElemento:
    def __init__(self, pila):
        self.pila = pila
        self.resultado = ""

    def ejecutar(self):
        cima = self.pila.top_of_stack()
        if cima is not None:
            self.resultado = f"El elemento en la cima (Top) es: '{cima}'"
        else:
            self.resultado = "La pila está vacía. No hay elementos en la cima."


class MostrarPila:
    def __init__(self, pila):
        self.pila = pila
        self.resultado = ""

    def ejecutar(self):
        if self.pila.top is None:
            self.resultado = "La pila está vacía."
            return

        temp = self.pila.top
        cajas = []
        # Recorremos la pila de forma vertical para el reporte
        while temp is not None:
            cajas.append(f"[ {temp.data} ]")
            temp = temp.next
        
        # Unimos las cajas con saltos de línea para mantener la estética visual de una pila
        self.resultado = "--- Cima de la Pila ---\n" + "\n".join(cajas) + "\n-----------------------"
        