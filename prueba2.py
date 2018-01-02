#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys, csv

from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    def __init__(self, rows, columns):
        QtGui.QWidget.__init__(self)

        self.currentPath = ''
        self.dataSet = []
        self.table = QtGui.QTableWidget(rows, columns, self)
        self.table.setSortingEnabled(True)

        # Buttons
        self.buttonGetData = QtGui.QPushButton('getdatafromcsv', self)
        self.buttonOpen = QtGui.QPushButton('Open (show all records)', self)
        self.buttonMenu = QtGui.QPushButton('Filtro Menu', self)
        self.buttonSave = QtGui.QPushButton('Save', self)
        self.buttonOpen.clicked.connect(self.getDataFromCsv)
        self.buttonOpen.clicked.connect(self.ShowDataSet)
        self.buttonMenu.clicked.connect(self.menuFilter)
        self.buttonSave.clicked.connect(self.SaveCSV)

        # Layout
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.table)
        layout.addWidget(self.buttonGetData)
        layout.addWidget(self.buttonOpen)
        layout.addWidget(self.buttonMenu)
        layout.addWidget(self.buttonSave)

    def SaveCSV(self):
        path = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV(*.csv)')
        if not path.isEmpty():
            with open(unicode(path), 'wb') as stream:
                writer = csv.writer(stream, delimiter=';')
                writer.writerow(self.getHeader(self.currentPath))
                for row in range(self.table.rowCount()):
                    rowdata = []
                    for column in range(self.table.columnCount()):
                        item = self.table.item(row, column)
                        if item is not None:
                            rowdata.append(
                                unicode(item.text()).encode('utf8'))
                        else:
                            rowdata.append('')
                    writer.writerow(rowdata)

    def getDataFromCsv(self):
        path = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '', 'CSV(*.csv)')
        if not path.isEmpty():
            self.currentPath = path
            with open(unicode(path), 'rb') as stream:
                reader = csv.reader(stream, delimiter=';')
                reader.next()
                for rowdata in reader:
                    self.dataSet.append(rowdata)

    def ShowDataSet(self):
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        for rowdata in self.dataSet:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setColumnCount(len(rowdata))
            for column, data in enumerate(rowdata):
                item = QtGui.QTableWidgetItem(data.decode('utf8'))
                self.table.setItem(row, column, item)
        self.table.setHorizontalHeaderLabels(self.getHeader(self.currentPath))

    def menuFilter(self, columna, valor):
        # SELECT DISTINCT SubMenu,Coordenada FROM TablaDeSecuencias where Menu="unmenu" and SubMenu is not null order by Coordenada


        pass

    def getHeader(self, path):
        with open(unicode(path), 'rb') as stream:
                reader = csv.reader(stream, delimiter=';')
                header = reader.next()
                return header



if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = Window(0, 0)
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())