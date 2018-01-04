#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys, csvdb

from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    def __init__(self, rows, columns):
        QtGui.QWidget.__init__(self)

        self.currentPath = ''
        self.dataSet = []
        self.table = QtGui.QTableWidget(rows, columns, self)
        self.table.setSortingEnabled(True)

        # Buttons
        self.buttonOpen = QtGui.QPushButton('Open', self)
        self.buttonFiltro = QtGui.QPushButton('Filter', self)
        self.buttonOrder = QtGui.QPushButton('Order', self)
        self.buttonSave = QtGui.QPushButton('Save', self)
        
        # Slots and Signals
        self.buttonOpen.clicked.connect(self.load)
        self.buttonOpen.clicked.connect(self.ShowDataSet)

        self.buttonFiltro.clicked.connect(self.filter)
        self.buttonFiltro.clicked.connect(self.ShowDataSet)

        self.buttonOrder.clicked.connect(self.sort)
        self.buttonOrder.clicked.connect(self.ShowDataSet)

        self.buttonSave.clicked.connect(self.save)

        
        # Layout
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.table)
        layout.addWidget(self.buttonOpen)
        layout.addWidget(self.buttonFiltro)
        layout.addWidget(self.buttonOrder)
        layout.addWidget(self.buttonSave)


    def load(self):
        self.currentPath = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '', 'CSV(*.csv)')
        if not self.currentPath.isEmpty():
            self.dataSet = csvdb.getDataFromCsv(self.currentPath)

    def sort(self):
        self.dataSet = csvdb.sortDataSet(self.dataSet,2)

    def filter(self):
        self.dataSet = csvdb.dataFilter(self.dataSet,1,"dini")

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
        self.table.setHorizontalHeaderLabels(csvdb.getHeader(self.currentPath))

    def save(self):
        path = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV(*.csv)')
        if not path.isEmpty():
            csvdb.SaveCSV(path, self.dataSet, csvdb.getHeader(self.currentPath))


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = Window(0, 0)
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())