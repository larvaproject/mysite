import pandas as pd
from datetime import datetime, date, timedelta

def getFecha():
	#Traemos la fecha
		x = datetime.now() - timedelta(days=1)
		dia = str(x.strftime("%d"))
		mes = str(x.strftime("%m"))
		anio = str(x.year)
		date = dia + '-' + mes + '-' + anio
		return date

date = getFecha()
nombre = 'claroshop-' + date + '.csv'

#Leemos el aechivo
df = pd.read_csv(r'/home/larva/crawler/claroshop/' + nombre, encoding = "utf-8")

#1.- Contamos cuantos productos tiene Linio
def totalProductosClaro():
   return len(df['nombre'])

#2.- Cuantas marcas tiene la tienda
def totalMarcasClaro():
    return len(df['marca'].value_counts())

#3.- Cuantas categorias tiene Linio
def totalCategoriasClaro():
    return len(df['categoría'].value_counts())


print(totalProductosClaro())
print(totalMarcasClaro())
print(totalCategoriasClaro())