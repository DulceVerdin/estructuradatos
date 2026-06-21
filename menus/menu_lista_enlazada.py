class AgregarInicio:
    def __init__(self, lista):
        self.lista = lista
        self.elemento = ""

    def ejecutar(self, elemento):
        self.elemento = elemento
        self.lista.insert_at_beginning(elemento)


class AgregarFinal:
    def __init__(self, lista):
        self.lista = lista
        self.elemento = ""

    def ejecutar(self, elemento):
        self.elemento = elemento
        self.lista.insert_at_end(elemento)


class BuscarElemento:
    def __init__(self, lista):
        self.lista = lista
        self.resultado = ""

    def ejecutar(self, elemento):
        encontrado = self.lista.search(elemento)
        if encontrado:
            self.resultado = f"Elemento '{elemento}' encontrado en la lista."
        else:
            self.resultado = f"Elemento '{elemento}' no encontrado."


class MostrarLista:
    def __init__(self, lista):
        self.lista = lista
        self.resultado = ""

    def ejecutar(self):
        temp = self.lista.head
        nodos = []
        while temp is not None:
            nodos.append(f"[{temp.data}]")
            temp = temp.next
        
        if nodos:
            self.resultado = "Head -> " + " -> ".join(nodos) + " -> Tail"
        else:
            self.resultado = "La lista está vacía."


class EliminarPrimerElemento:
    def __init__(self, lista):
        self.lista = lista
        self.resultado = ""

    def ejecutar(self):
        eliminado = self.lista.delete_at_beginning()
        if eliminado is not None:
            self.resultado = f"Elemento '{eliminado}' eliminado del inicio."
        else:
            self.resultado = "La lista está vacía. Nada que eliminar."


class EliminarUltimoElemento:
    def __init__(self, lista):
        self.lista = lista
        self.resultado = ""

    def ejecutar(self):
        eliminado = self.lista.delete_at_end()
        if eliminado is not None:
            self.resultado = f"Elemento '{eliminado}' eliminado del final."
        else:
            self.resultado = "La lista está vacía. Nada que eliminar."