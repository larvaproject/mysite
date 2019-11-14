import pandas as pd

#Leemos el archivo
df = pd.read_csv(r'/home/larva/mysite/static/ext/liverpool/Liverpool.csv', encoding = "utf-8")

#1.- Contamos cuantos productos tiene Linio
def totalProductosLiverpool():
   return len(df)

#2.- Cuantas marcas tiene la tienda
def totalMarcasLiverpool():
    return len(df['marca'].value_counts())

#3.- Cuantas categorias tiene Linio
def totalCategoriasLiverpool():
    return len(df['categoria'].value_counts())