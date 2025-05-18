class carrito:
    def __init__(self):
        self.estado = "Detenido"

    def avanzar(self):
        self.estado = "Avanzar"
        return "El carrito avanzar"
    def retroceder(self):
        self.estado = "Retroceder"
        return "El carrito retrocede"
    def izquierda(self):
        self.estado = "Izquierda"
        return "El carrito gira a la izquierda"
    def derecha(self):
        self.estado = "Derecha"
        return "El carrito gira a la derecha"



x = True

while x:
    print("Elija una opcion \n1. Encender\n 2. Piloto automatico\n 3. \n")
    opcion = int(input("-> "))

    while opcion not in (1, 2, 3, 4):
        print("Opcion no valida, vuelva a intentarlo \n")

        opcion = int(input("-> "))

    if opcion == 1:
        print("Presione ")