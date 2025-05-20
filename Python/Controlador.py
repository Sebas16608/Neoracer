class Carrito:
    def __init__(self):
        self.estado = "Detenido"

    def avanzar(self):
        self.estado = "Avanzar"
        return "El carrito está avanzando"

    def retroceder(self):
        self.estado = "Retroceder"
        return "El carrito está retrocediendo"

    def izquierda(self):
        self.estado = "Izquierda"
        return "El carrito gira a la izquierda"

    def derecha(self):
        self.estado = "Derecha"
        return "El carrito gira a la derecha"

    def piloto(self):
        self.estado = "Piloto Automático"
        return "Se activó el piloto automático"