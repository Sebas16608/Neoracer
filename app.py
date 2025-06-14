from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

boostrap = Bootstrap(app)

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