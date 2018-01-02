#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys, csv


def SaveCSV(self, path, dataset, header):
    with open(unicode(path), 'wb') as stream:
        writer = csv.writer(stream, delimiter=';')
        writer.writerow(header)
        for row in range(dataset):
            rowdata = []
            for column in range(len(dataset[0])):
                item = dataset[row][column]
                if item is not None:
                    rowdata.append(unicode(item.text()).encode('utf8'))
                else:
                    rowdata.append('')
            writer.writerow(rowdata)

def getDataFromCsv(self, path):
    dataSet = []
    with open(unicode(path), 'rb') as stream:
        reader = csv.reader(stream, delimiter=';')
        reader.next()
        for rowdata in reader:
            dataSet.append(rowdata)
    return dataSet

def dataFilter(self, dataset, columna, valor):
    # SELECT DISTINCT SubMenu,Coordenada FROM TablaDeSecuencias where Menu="unmenu" and SubMenu is not null order by Coordenada
    filteredDataSet = []
    for rowdata in dataset:
        if rowdata[columna] == valor:
            filteredDataSet.append(rowdata)
    return filteredDataSet

def getHeader(self, path):
    with open(unicode(path), 'rb') as stream:
            reader = csv.reader(stream, delimiter=';')
            header = reader.next()
            return header

def sortDataSet(self, dataset, column, invertido=False):
    sortedDataSet = sorted(dataset, key=lambda col: col[column], reverse=invertido)
    return sortedDataSet


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = Window(0, 0)
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())