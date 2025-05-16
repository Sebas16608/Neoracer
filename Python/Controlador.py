def izquiera():
    return "Girar a la izquierda"

def derecha():
    return "Girar a la derecha"

def recto():
    return "Debe seguir recto"

def atras():
    return "Debe retroceder"


carrito = True

#servira para hacer un boton
while carrito:
    print("Que deseas hacer? \n 1. Encender \n 2. Apagar")
    opcion = int(input(""))

    if opcion == 1:
        print("Encendiendo... \n")
    
    elif opcion == 2:
        print("Okay bye... ")
        break

    else:
        print("opcion incorrecta")
        break