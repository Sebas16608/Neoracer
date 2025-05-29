from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)

boostrap = Bootstrap(app)

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

@app.route('/')
def home():
    return render_template("base.html")

@app.route('/informacion')
def info():
    return render_template("info.html")

@app.route('/controlador')
def controlador():
    return render_template("controlador.html")


app.run(host="0.0.0.0", port="1995", debug=True)