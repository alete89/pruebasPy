#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
el parámetro delimiter=';' está seteado así porque la configuración internacional de windows
usa ';' por defecto como separador de columnas en un CSV. Tras unificar criterios ese caracter
se puede cambiar por ',' o el que nosotros elijamos.
'''
import sys, csv

COLUMN_DELIMITER = ';'

def SaveCSV(path, dataset, header):
    with open(unicode(path), 'wb') as stream:
        writer = csv.writer(stream, delimiter=COLUMN_DELIMITER)
        writer.writerow(header)
        for row in range(len(dataset)):
            rowdata = []
            for column in range(len(dataset[0])):
                item = dataset[row][column]
                if item is not None:
                    rowdata.append(unicode(item).encode('utf8'))
                else:
                    rowdata.append('')
            writer.writerow(rowdata)

def getDataFromCsv(path):
    dataSet = []
    with open(unicode(path), 'rb') as stream:
        reader = csv.reader(stream, delimiter=COLUMN_DELIMITER)
        reader.next()
        for rowdata in reader:
            dataSet.append(rowdata)
    return dataSet

def dataFilter(dataset, columna, valor):
    # ejemplo de query para tener en cuenta qué/cómo necesito poder filtrar
    # SELECT DISTINCT SubMenu,Coordenada FROM TablaDeSecuencias where Menu="unmenu" and SubMenu is not null order by Coordenada
    filteredDataSet = []
    for rowdata in dataset:
        if rowdata[columna] == valor:
            filteredDataSet.append(rowdata)
    return filteredDataSet

def getHeader(path):
    with open(unicode(path), 'rb') as stream:
            reader = csv.reader(stream, delimiter=COLUMN_DELIMITER)
            header = reader.next()
            return header

def sortDataSet(dataset, column, invertido=False):
    sortedDataSet = sorted(dataset, key=lambda col: col[column], reverse=invertido)
    return sortedDataSet