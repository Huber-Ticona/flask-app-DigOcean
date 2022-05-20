from flask import Flask, render_template,session,url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy
from api import api_bp
from auth import auth_bp


app = Flask(__name__)
db = SQLAlchemy(app)

app.register_blueprint(api_bp, url_prefix='/')
app.register_blueprint(auth_bp, url_prefix='/')

@app.route('/')
@app.route('/inicio')
def home():
    return render_template("inicio.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")



#if __name__ == '__main__':
    #app.run(debug=True)

