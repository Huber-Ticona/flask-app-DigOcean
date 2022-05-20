from flask import Blueprint, render_template, session , request, redirect , url_for
import pymysql
auth_bp = Blueprint('auth_bp', __name__ ,static_folder='static', template_folder='templates')


@auth_bp.route('/login' ,methods = ['GET', 'POST'])
def login():

    if request.method == 'POST':
        nombre = request.form['nombre_usuario']
        contra = request.form['contraseña']

        print(nombre)

        #VALIDAR CUENTA EN DB 
        miConexion = pymysql.connect( host='153.92.7.201',
            user= 'roothuber', passwd= '' , db='htproyect_test' )
        try:
            with miConexion.cursor() as cursor:
        
                sql = "select * from usuario"
                cursor.execute( sql )
                consulta = cursor.fetchall()

                print(consulta)
                return render_template('contacto.html')

               
        finally:
            miConexion.close()

    return render_template('login.html' )
        

@auth_bp.route('/logout')
def logout():
    return "<p>hola productos<p>"