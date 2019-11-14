from datetime import datetime, date, timedelta
import pandas as pd
import time

def getFecha():
	#Traemos la fecha
		x = datetime.now() - timedelta(days=1)
		dia = str(x.strftime("%d"))
		mes = str(x.strftime("%m"))
		anio = str(x.year)
		date = dia + '-' + mes + '-' + anio
		return date

date = getFecha()
df = pd.read_csv(r'/home/larva/crawler/sanpablo/sanpablo-' + date + '.csv', encoding = "utf-8")

#1.- Contamos cuantos productos tiene San Pablo
def totalProductosSanpablo():
   return len(df['nombre'])

#2.- Cuantas marcas tiene San Pablo
def totalMarcasSanpablo():
    return len(df['fabricante'].value_counts())

#3.- Cuantas categorias tiene San Pablo
def totalCategoriasSanpablo():
    return len(df['categoria'].value_counts())