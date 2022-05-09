from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/inicio')
def home():
    return render_template("inicio.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")


