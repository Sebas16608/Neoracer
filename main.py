from flask import Flask, request, render_template, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/informacion")
def info():
    return render_template("info.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)