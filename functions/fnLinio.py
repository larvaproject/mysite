import csv
import re
import time
import numpy as np
from matplotlib import cm
from collections import defaultdict
import matplotlib.pyplot as plt

#Funcion para extraer el digito del porcentaje y el numero de productos
def countTiemsDiscount(dictLi):
    suma = 0
    for k,v in dictLi.items():
        suma += v
    return suma

#Funcion para extraer el digito del porcentaje
def extractNum(source):
	return int(re.search(r'\-\s(\d*)\W', source).group(1))

def hasNumbers(stringUno):
	return bool(re.search(r'\d', stringUno))

def checkNum(source):
	value = hasNumbers(source)
	numero = 1

	#Si, si tiene numeros o digitos
	if value == True:
		numero = extractNum(source)
	else:
		numero = 0

	return numero

def countCatsLi(archivo):
	columns = defaultdict(list)
	catList = []
	with open(archivo, 'r', encoding='utf-8') as f:
		reader = csv.DictReader(f)
		for row in reader:
			for (k,v) in row.items():
				columns[k].append(v)

	for ori in columns['porcentaje']:
		#ori = cleanNum(ori)
		idNumber = checkNum(ori)
		if idNumber == 10 or idNumber == 15 or idNumber == 20 or idNumber == 30 or idNumber == 50:
			catList.append(idNumber)
	return catList

def CountFrequency(miLista):
	freq = {}
	for item in miLista:
		if (item in freq):
			freq[item] += 1
		else:
			freq[item] = 1
	return freq