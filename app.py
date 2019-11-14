from flask import Flask, render_template, flash, redirect, flash, url_for, session, request, logging, Response
from flask import send_file, request, url_for
import pandas as pd
import dash
import plotly
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import json

from flask_wtf import FlaskForm
from wtforms import DateField
from wtforms import StringField
from wtforms.validators import DataRequired
from datetime import date

#PANDAS
from funciones.linio import totalProductosLinio, totalMarcasLinio, totalCategoriasLinio
from funciones.sanpablo import totalProductosSanpablo, totalMarcasSanpablo, totalCategoriasSanpablo
from funciones.claroshop import totalProductosClaro, totalMarcasClaro, totalCategoriasClaro
from funciones.liverpool import totalProductosLiverpool, totalMarcasLiverpool, totalCategoriasLiverpool
from funciones.mercadoLibre import totalProductosMercadoLibre, totalMarcasMercadoLibre, totalCategoriasMercadoLibre

#DASH
from funciones.visual import create_plot

import json, datetime, csv, re
from datetime import datetime, date, timedelta
from collections import defaultdict
from flask_mysqldb import MySQL
from functools import wraps
from flask_wtf import Form
from wtforms import DateField
from wtforms.fields.html5 import DateField
from wtforms.fields.html5 import DateTimeField
from datetime import date

import time
import calendar
import codecs

app = Flask(__name__, static_folder='ext')
app.secret_key='secret123'

class TestForm(FlaskForm):
    startdate = DateField('Start Date',default=date.today)
    enddate = DateField('End Date',default=date.today)

    def validate_on_submit(self):
        result = super(TestForm, self).validate()
        if (self.startdate.data>self.enddate.data):
            return False
        else:
            return result

# MySQL configurations
app.config['MYSQL_USER'] = 'larva'
app.config['MYSQL_PASSWORD'] = 'nomelose'
app.config['MYSQL_DB'] = 'larva$categorias'
app.config['MYSQL_HOST'] = 'larva.mysql.pythonanywhere-services.com'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#Inicializar MySQL
mysql = MySQL(app)

#User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']

        #Create cursor
        cur = mysql.connection.cursor()

        #Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            data = cur.fetchone()
            password = data['password']

            #Comparamos passwords
            if password_candidate == 'larv4project-3!':
                session['logged_in'] = True
                return redirect(url_for('dashboard'))
            else:
                error = 'Contraseña incorrecta'
                return render_template('login.html', error=error)
            #Cerramos conexion
            cur.close()
        else:
            error = 'Usuario invalido'
            return render_template('login.html', error=error)

    return render_template('login.html')

#Si estamos logeados
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap

# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    return redirect(url_for('login'))

#D3 js
@app.route('/')
def index():
    return render_template('index.html')

#-------- FECHA -------------#
def getFecha():
	#Traemos la fecha
		x = datetime.now() - timedelta(days=1)
		dia = str(x.strftime("%d"))
		mes = str(x.strftime("%m"))
		anio = str(x.year)
		date = dia + '-' + mes + '-' + anio
		return date

def getDat():
	#Traemos la fecha
		x = datetime.now()
		dia = str(x.strftime("%d"))
		mes = str(x.strftime("%m"))
		anio = str(x.year)
		date = dia + '-' + mes + '-' + anio
		return date

#Para la sección de descuentos
@app.route('/dashboard', methods=['post','get'])
@is_logged_in
def dashboard():

    #De Claroshop
    noItemsC = totalProductosClaro()
    noCatsC = totalMarcasClaro()
    noMarcasC = totalCategoriasClaro()

    #De Linio
    noProdLinio = totalProductosLinio()
    marcasLinio = totalMarcasLinio()
    catLinio = totalCategoriasLinio()

    #De Liverpool
    noItemsLiver = totalProductosLiverpool()
    noCatsLiver = totalMarcasLiverpool()
    noMarcasLiver = totalCategoriasLiverpool()

    #De SanPablo
    noItemsSan = totalProductosSanpablo()
    noCatsSan = totalMarcasSanpablo()
    noMarcasSan = totalCategoriasSanpablo()

    #De Mercado Libre
    noItemsMer = totalProductosMercadoLibre()
    noCatsMer = totalMarcasMercadoLibre()
    noMarcasMer = totalCategoriasMercadoLibre()

    #Para el encabezado
    fecha = getFecha()

    #bar = create_plot()

    return render_template('dashboard.html', fecha = fecha, noProdLinio = noProdLinio, catLinio = catLinio, marcasLinio = marcasLinio,
                                             noItemsC = noItemsC, noCatsC = noCatsC, noMarcasC = noMarcasC,
                                             noItemsLiver = noItemsLiver, noCatsLiver = noCatsLiver, noMarcasLiver = noMarcasLiver,
                                             noItemsSan = noItemsSan, noCatsSan = noCatsSan, noMarcasSan = noMarcasSan,
                                             noItemsMer = noItemsMer, noCatsMer = noCatsMer, noMarcasMer = noMarcasMer)


#-------- SECCION DESCARGA DE ARCHIVOS -------------#

@app.route('/getMercadoCSV/')
@is_logged_in
def getMercadoCSV():
    date = getFecha()
    nombre = 'mercadolibre-' + date + '.csv'
    return send_file('/home/larva/crawler/mercado/' + nombre, attachment_filename='mercadoLibre.csv')

@app.route('/getLinioCSV/')
@is_logged_in
def getLinioCSV():
    date = getFecha()
    nombre = 'linio-' + date + '.csv'
    return send_file('/home/larva/crawler/linio/' + nombre, attachment_filename='linio.csv')

@app.route('/getClaroshopCSV/')
@is_logged_in
def getClaroshopCSV():
    date = getFecha()
    nombre = 'claroshop-' + date + '.csv'
    route = '/home/larva/crawler/claroshop/' + nombre
    return send_file(route, attachment_filename='claroshop.csv')

@app.route('/getLiverpoolCSV')
@is_logged_in
def getLiverpoolCSV():
    nombre = 'Liverpool.csv'
    return send_file('/home/larva/mysite/static/ext/liverpool/'+ nombre, attachment_filename='Liverpool.csv')

@app.route('/getSanpabloCSV')
@is_logged_in
def getSanpabloCSV():
    date = getFecha()
    #/home/larva/crawler/sanpablo
    nombre = 'sanpablo-' + date + '.csv'
    return send_file('/home/larva/crawler/sanpablo/'+ nombre, attachment_filename='sanpablo.csv')

# ------------ ANALISIS CON PANDAS ------------ #

@app.route('/mercadolibre', methods=['GET', 'POST'])
@is_logged_in
def mercadoDetail():
    noItemsMer = totalProductosMercadoLibre()
    noCatsMer = totalMarcasMercadoLibre()
    noMarcasMer = totalCategoriasMercadoLibre()
    return render_template('mercado.html', noItemsMer = noItemsMer, noCatsMer = noCatsMer, noMarcasMer = noMarcasMer)

# Sección Claro Shop
@app.route('/claroshop')
@is_logged_in
def claroDetail():
    totalClaro = totalProductosClaro()
    marcasClaro = totalMarcasClaro()
    catsClaro = totalCategoriasClaro()
    return render_template('claroshop.html', totalClaro = totalClaro, marcasClaro = marcasClaro, catsClaro = catsClaro)

#Sección Linio
@app.route('/linio')
@is_logged_in
def linioDetail():
    totalLinio = totalProductosLinio()
    marcasLinio = totalMarcasLinio()
    catsLinio = totalCategoriasLinio()
    return render_template('linio.html', totalLinio = totalLinio, marcasLinio = marcasLinio, catsLinio = catsLinio)

#Sección Sanpablo
@app.route('/sanpablo', methods=['GET', 'POST'])
@is_logged_in
def sanpabloDetail():
    totalP = totalProductosSanpablo()
    totalM = totalMarcasSanpablo()
    totalC = totalCategoriasSanpablo()
    return render_template('sanpablo.html', totalP = totalP, totalM = totalM, totalC = totalC)

#Sección Liverpool
@app.route('/liverpool')
@is_logged_in
def liverpoolDetail():
    totalLiver = totalProductosLiverpool()
    marcasLiver = totalMarcasLiverpool()
    catsLiver = totalCategoriasLiverpool()
    return render_template('liverpool.html', totalLiver = totalLiver, marcasLiver = marcasLiver, catsLiver = catsLiver)

#--------------- Para la sección de descuentos con DASH --------------------------
if __name__ == '__main__':
    app.debug = True
    app.run()