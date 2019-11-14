from datetime import datetime, date, timedelta
import pandas as pd

def getFecha():
	#Traemos la fecha
		x = datetime.now() - timedelta(days=1)
		dia = str(x.strftime("%d"))
		mes = str(x.strftime("%m"))
		anio = str(x.year)
		date = dia + '-' + mes + '-' + anio
		return date

#Leemos el archivo
date = getFecha()
nombre = 'linio-' + date + '.csv'
df = pd.read_csv(r'/home/larva/crawler/linio/' + nombre, encoding = "utf-8")

#1.- Contamos cuantos productos tiene Linio
def totalProductosLinio():
   return len(df)

#2.- Cuantas marcas tiene la tienda
def totalMarcasLinio():
    return len(df['marca'].value_counts())

#3.- Cuantas categorias tiene Linio
def totalCategoriasLinio():
    return len(df['categoria'].value_counts())