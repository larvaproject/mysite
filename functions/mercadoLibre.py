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

df = pd.read_csv(r'/home/larva/crawler/mercado/mercadolibre-' + date + '.csv', encoding = "utf-8")

#1.- Contamos cuantos productos tiene Mercado Libre
def totalProductosMercadoLibre():
   return len(df['nombre'])

#2.- Cuantas marcas tiene Mercado Libre
def totalMarcasMercadoLibre():
    return len(df['marca'].value_counts())

#3.- Cuantas categorias tiene Mercado Libre
def totalCategoriasMercadoLibre():
    return len(df['categoria'].value_counts())