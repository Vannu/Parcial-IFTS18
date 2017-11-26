#!/usr/bin/env python

import csv
from flask import Flask, render_template, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
from forms import LoginForm, RegistrarForm, Consulta_Cliente, Consulta_Producto
import archivo


app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'un string que funcione como llave'

#------------------------  VALIDACION DEL ARCHIVO  -----------------

'''Pruebas de datos inexistentes'''
'''Que campo cantidad inavalida de campos'''
'''Que campo CODIGO no contenga campos vacios'''
'''Que campo CANTIDAD no contenga una valor entero'''
'''Que campo PRECIO no contenga un valor decimal'''
 

class CSVError(Exception):
    pass


class  validarCSV():

    def leerCSV(self):

        try:
            csvfile = open('farmacia.csv', 'r')
        except FileNotFoundError:
            raise CSVError(" Archivo no encontrado")

        archivoCSV = csv.DictReader(csvfile)
        rows = list(archivoCSV)

        for row in rows:
                     
                if len(row) != 5:
                        raise CSVError(" Verifique el número de columnas del archivo")

                if row["CODIGO"] == '':
                        raise CSVError(" El campo CODIGO esta vacio")
                
                cantidad = float(row["CANTIDAD"])
                if not cantidad.is_integer():
                        raise CSVError(" El campo CANTIDAD no contiene números enteros")
                
                try:
                    precio = float(row["PRECIO"])
                except:
                    raise CSVError(" El campo PRECIO no contiene valores decimales")

        return rows



#-------------------------  INDEX  ---------------------
# Pagina de inicio "FARMA", con menu de ingresar y crear nuevo usuario

@app.route('/')
def index():
    return render_template('index.html')


#------------------------   ERRORES  ---------------------
# Pagina de inicio "FARMA", con menu de ingresar y crear nuevo usuario
#pagina de resultados no encontrado
@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_interno(e):
    return render_template('500.html'), 500


#------------------------- LOGIN -----------------------
#pagina para logear usuario y se valida su nombre y contraseña.
#Si accede con exito, se les da la bienvenida al usuario y se visualizara un nuevo menu.
#El menu contendra: Base de Datos, productos por cliente, cliente por productos, mejroes clientes, prouctos mas vendidos y la opcion de deslogearse.


@app.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        with open('usuarios') as archivo:
            archivo_csv = csv.reader(archivo)
            registro = next(archivo_csv)
            while registro:
                if formulario.usuario.data == registro[0] and formulario.password.data == registro[1]:
                    session['username'] = formulario.usuario.data
                    return render_template('farmasoft.html', formulario=formulario, username=session.get('username'))
                registro = next(archivo_csv, None)
            else:
                flash('Revisá nombre de usuario y contraseña')
                return redirect(url_for('ingresar'))
    return render_template('login.html', formulario=formulario, username=session.get('username'))


#----------------------- REGISTRACION - NUEVO USUARIO  -----------------------
#Al crear nuevo usuario se redirecciona a la pagina de ingreso

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    formulario = RegistrarForm()
    if formulario.validate_on_submit():
        if formulario.password.data == formulario.password_check.data:
            try:
                with open('usuarios', 'a+') as archivo:
                    archivo_csv = csv.writer(archivo)
                    registro = [formulario.usuario.data, formulario.password.data]
                    archivo_csv.writerow(registro)
                flash('Usuario creado correctamente')
                return redirect(url_for('ingresar'))
            except FileNotFoundError:
                return 'No se encuentra el archivo CSV de Usuarios'
        else:
            flash('Las passwords no matchean')
    return render_template('registrar.html', form=formulario)


#------------------------ PAGINA DE BIENVENIDA DEL USUARIO -------------------------

#pagina de inicio, ya logeado
@app.route('/ingresar',methods=['GET' , 'POST'])
def farmasoft(): 
    if session.get("username"):    
        return render_template('farmasoft.html', username = session.get('username'))
    return redirect(url_for('login'))


#-----------------------  BASE DE DATOS -------------------------
#pagina que muesta una lista de la base de datos de FarmaSoft 
@app.route('/tabla',methods=['GET' , 'POST'])
def tabla(): 
    if session.get("username"):       
        try:
            rows = validarCSV().leerCSV()
        except CSVError as error:
            return render_template('errorCSV.html', error = error)  
        header=['CODIGO', 'PRODUCTO', 'CLIENTE', 'CANTIDAD', 'PRECIO']
        clientes = archivo.cargar_archivo("farmacia.csv")
        return render_template('tabla.html', header = header, clientes = clientes, username = session.get('username'))                
    return redirect(url_for('login'))



#-------------------- CONSULTAS ----------------------------
#Consulta de productos mas vendidos
@app.route('/productos_mas_vendidos',methods=['GET' , 'POST'])
def pmv():
    if session.get("username"):       
        try:
            rows = validarCSV().leerCSV()
        except CSVError as error:
            return render_template('errorCSV.html', error = error)  
        header=['CODIGO', 'PRODUCTO', 'CANTIDAD DE PRODUCTOS']               
        nproductos = archivo.nproductos("farmacia.csv")
        return render_template("pmv.html", header = header, nproductos = nproductos, username = session.get('username'))
    return redirect(url_for('login'))



#-------------------- CONSULTAS ----------------------------
#Consulta de los mejores clientes
@app.route('/mejores_clientes',methods=['GET' , 'POST'])
def cmg():
    if session.get("username"):       
        try:
            rows = validarCSV().leerCSV()
        except CSVError as error:
            return render_template('errorCSV.html', error = error)  
        header=['CODIGO', 'CLIENTE', 'TOTAL GASTADO']         
        nclientes = archivo.nclientes("farmacia.csv")
        return render_template("cmg.html", header = header, nclientes = nclientes, username = session.get('username'))
    return redirect(url_for('login'))



#-------------------- CONSULTAS ----------------------------
#Consulta de productos por cliente
@app.route('/productos_por_clientes',methods=['GET' , 'POST'])
def pxc():
    if session.get("username"):       
        try:
            rows = validarCSV().leerCSV()
        except CSVError as error:
            return render_template('errorCSV.html', error = error)  
        header=['CODIGO', 'PRODUCTO', 'CLIENTE']               
        formulario = Consulta_Cliente()
        listado_clientes= archivo.lista_clientes()
        clientes = archivo.productos_por_clientes(formulario.cliente.data)
        if formulario.validate_on_submit():
            if formulario.cliente.data in listado_clientes:
                if len(formulario.cliente.data) <= 3:
                        flash('Ingrese más de tres caracteres')                      
            return render_template("pxc.html", header = header, formulario = formulario, tablaclientes = clientes)
        return render_template ("pxc.html", header = header, formulario = formulario, tablaclientes = clientes, username = session.get('username'))
    return redirect(url_for('login'))



#-------------------- CONSULTAS ----------------------------
#Consulta de cliente por productos 
@app.route('/clientes_por_productos',methods=['GET' , 'POST'])
def cxp():
    if session.get("username"):       
        try:
            rows = validarCSV().leerCSV()
        except CSVError as error:
            return render_template('errorCSV.html', error = error)  
        header=['CODIGO', 'PRODUCTO', 'CLIENTE']                
        formulario = Consulta_Producto()
        listado_productos= archivo.lista_productos()
        productos = archivo.clientes_por_productos(formulario.producto.data)
        if formulario.validate_on_submit():
            if formulario.producto.data in listado_productos:
                    if len(formulario.producto.data) <= 3:
                        flash('Ingrese más de tres caracteres')             
            return render_template("cxp.html", header = header, formulario = formulario, tablaproductos = productos)         
        return render_template ("cxp.html", header = header, formulario = formulario, tablaproductos = productos, username = session.get('username'))
    return redirect(url_for('login'))



#-------------------- DESLOGEARSE ----------------------------
# cerrar sesion 
@app.route('/logout')
def logout():
    if session.get("username"):
        session.pop('username')
        return redirect('/ingresar')
    else:
        return redirect('/ingresar')


if __name__ == "__main__":
   app.run(debug=True)
