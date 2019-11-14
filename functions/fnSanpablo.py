import csv
import re
import time
import numpy as np
from matplotlib import cm
from collections import defaultdict
import matplotlib.pyplot as plt

import csv
import re
import time
import numpy as np
from collections import defaultdict


route = '/home/larva/mysite/static/ext/sanpablo/'

#----------- Contamos las categorias de SanPablo --------------------
def countCatsSan(nombreArchivo):
    columns = defaultdict(list)
    catList = []
    with open(route + nombreArchivo, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for (k,v) in row.items():
                columns[k].append(v)

    for col in columns['categoria']:
        catList.append(col)

    catList = list(dict.fromkeys(catList))
    return len(catList)

#----------- Contamos los Items de SanPablo --------------------
def countItemsSan(nombreArchivo):
    #Esta funcion devuelve la cantidad de productos de un archivo csv
    with open(route + nombreArchivo, 'r', encoding='utf-8') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        #Filtramos de celdas en blanco
        filterList = list(filter(None, lines))
        return len(filterList)

#----------- Contamos las marcas de SanPablo --------------------

def countMarcasSan(nombreArchivo):
    columns = defaultdict(list)
    catList = []

    with open(route + nombreArchivo, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for (k,v) in row.items():
                columns[k].append(v)

    for col in columns['fabricante']:
        catList.append(col)

    catList = list(dict.fromkeys(catList))
    return len(catList)