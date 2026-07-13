import datetime

class Cliente:
    def __init__(self, turno):
        self.turno = turno
        self.hora_ingreso = datetime.datetime.now()

    def __str__(self):
        # Esto hace que cuando tu Queue ejecute 'printQueue', 
        # se renderice el texto de esta manera automáticamente.
        return f"Turno {self.turno}"