from estructuras.lineales.queue import Queue

class TrabajoImpresion:
    consecutivo_global = 1

    def __init__(self, usuario, documento, paginas):
        self.usuario = usuario
        self.documento = documento
        self.paginas = paginas
        self.consecutivo = TrabajoImpresion.consecutivo_global
        TrabajoImpresion.consecutivo_global += 1

    def __str__(self):
        return f"[{self.consecutivo}] {self.usuario} - {self.documento} ({self.paginas} pág.)"


class GestorImpresion:
    def __init__(self):
        self.cola = Queue()

    def agregar_trabajo(self, usuario, documento, paginas):
        if not usuario or not documento or paginas < 1:
            return "Error: Datos inválidos."
        trabajo = TrabajoImpresion(usuario, documento, paginas)
        self.cola.enqueue(trabajo)
        return f"Trabajo agregado: {trabajo}"

    def consultar_frente(self):
        if self.cola.isEmpty():
            return "No hay trabajos en la cola."
        return f"Frente: {self.cola.firstQueue()}"

    def imprimir_siguiente(self):
        if self.cola.isEmpty():
            return "No hay trabajos pendientes."
        trabajo = self.cola.dequeue()
        return f"Imprimiendo: {trabajo}"

    def listar_trabajos(self):
        return self.cola.printQueue()

    def estado(self):
        if self.cola.isEmpty():
            return "Cola vacía."
        return f"Pendientes: {self.cola.printQueue()}"