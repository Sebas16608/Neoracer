from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tecnologia")
def tecno():
    return render_template("tecno.html")

@app.route("/APIs")
def api():
    return render_template("api.html")

@app.route("/Neoracer")
def neo():
    return render_template("neo.html")

@app.route("/Funcionamiento")
def funcion():
    return render_template("funcion.html")

@app.route("/piloto-automatico")
def piloto():
    return render_template("piloto.html")

@app.route("/De-que-servirá")
def futuro():
    return render_template("futuro.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)