from datetime import datetime
from estructuras.lineales.queue import Queue

class Banco:

    def __init__(self):
        self.cola = Queue()
        self.turno = 1
        self.clientes_atendidos = 0
        self.tiempo_total = 0
        self.banco_cerrado = False   

    def agregarCliente(self):

        # Verificar si el banco está cerrado
        if self.banco_cerrado:
            return "El banco está cerrado.\nAún hay clientes por atender."

        cliente = {
            "turno": self.turno,
            "hora": datetime.now()
        }

        self.cola.enqueue(cliente)

        mensaje = f"""Cliente agregado.

Turno: {self.turno}
Hora de entrada: {cliente["hora"].strftime("%H:%M:%S")}"""

        self.turno += 1

        return mensaje

    def atenderCliente(self):

        if self.cola.isEmpty():
            return "No hay clientes en la cola."

        cliente = self.cola.dequeue()

        hora_salida = datetime.now()

        espera = (hora_salida - cliente["hora"]).seconds

        self.clientes_atendidos += 1
        self.tiempo_total += espera

        mensaje = f"""Cliente atendido.

Turno: {cliente["turno"]}
Hora de entrada: {cliente["hora"].strftime("%H:%M:%S")}
Hora de salida: {hora_salida.strftime("%H:%M:%S")}
Tiempo de espera: {espera} segundos"""

        # Si el banco ya estaba cerrado y este era el último cliente
        if self.banco_cerrado and self.cola.isEmpty():

            mensaje += f"""

Todos los clientes fueron atendidos.

Clientes atendidos: {self.clientes_atendidos}
Tiempo promedio de espera: {self.promedio():.2f} segundos"""

        return mensaje

    def mostrarCola(self):

        if self.cola.isEmpty():
            return "No hay clientes en espera."

        texto = ""

        temp = self.cola.lista.head

        while temp:

            texto += f'Turno {temp.data["turno"]} - {temp.data["hora"].strftime("%H:%M:%S")}\n'

            temp = temp.next

        return texto

    def promedio(self):

        if self.clientes_atendidos == 0:
            return 0

        return self.tiempo_total / self.clientes_atendidos

    def cerrarBanco(self):

        # El banco deja de aceptar clientes
        self.banco_cerrado = True

        if not self.cola.isEmpty():

            return """Banco cerrado.


Aún hay clientes por atender."""

        return f"""Banco cerrado.

No hay clientes en espera.

Clientes atendidos: {self.clientes_atendidos}

Tiempo promedio de espera: {self.promedio():.2f} segundos"""