import csv
import re
import time
import numpy as np
from collections import defaultdict

#----------- Contamos las marcas de Claroshop --------------------
def countMarcas(nombreArchivo):
    columns = defaultdict(list)
    marList = []
    with open('/home/larva/mysite/static/ext/' + nombreArchivo, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for (k,v) in row.items():
                columns[k].append(v)

    for col in columns['marca']:
        marList.append(col)

    marList = list(dict.fromkeys(marList))
    return len(marList)

#----------- Contamos las categorias de Claroshop --------------------
def countCats(nombreArchivo):
    columns = defaultdict(list)
    catList = []
    with open('/home/larva/mysite/static/ext/' + nombreArchivo, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for (k,v) in row.items():
                columns[k].append(v)

    for col in columns['categoria']:
        catList.append(col)

    catList = list(dict.fromkeys(catList))
    return len(catList)

#----------- Contamos los Items de Claroshop --------------------
def countItems(nombreArchivo):
    #Esta funcion devuelve la cantidad de productos de un archivo csv
    with open('/home/larva/mysite/static/ext/' + nombreArchivo, 'r', encoding='utf-8') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        #Filtramos de celdas en blanco
        filterList = list(filter(None, lines))
        return len(filterList)