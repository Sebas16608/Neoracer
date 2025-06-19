from flask import Flask, request, render_template, render_template

app = Flask(__name__)

@app.route("/Index")
def inicio():
    return render_template("index.html")