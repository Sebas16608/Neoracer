from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("main.html")

@app.route('/informacion')
def info():
    return render_template("info.html")


app.run(host="0.0.0.0", port="3000", debug=True)