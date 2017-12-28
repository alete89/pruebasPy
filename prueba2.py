#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys, csv

from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    def __init__(self, rows, columns):
        QtGui.QWidget.__init__(self)
        
        self.table = QtGui.QTableWidget(rows, columns, self)

        # Buttons
        self.buttonOpen = QtGui.QPushButton('Open', self)
        self.buttonSave = QtGui.QPushButton('Save', self)
        self.buttonOpen.clicked.connect(self.handleOpen)
        self.buttonSave.clicked.connect(self.handleSave)

        # Layout
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.table)
        layout.addWidget(self.buttonOpen)
        layout.addWidget(self.buttonSave)

    def handleSave(self):
        path = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV(*.csv)')
        if not path.isEmpty():
            with open(unicode(path), 'wb') as stream:
                writer = csv.writer(stream, delimiter=';')
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

    def handleOpen(self):
        path = QtGui.QFileDialog.getOpenFileName(
                self, 'Open File', '', 'CSV(*.csv)')
        if not path.isEmpty():
            with open(unicode(path), 'rb') as stream:
                self.table.setRowCount(0)
                self.table.setColumnCount(0)
                for rowdata in csv.reader(stream, delimiter=';'):
                    row = self.table.rowCount()
                    self.table.insertRow(row)
                    self.table.setColumnCount(len(rowdata))
                    for column, data in enumerate(rowdata):
                        item = QtGui.QTableWidgetItem(data.decode('utf8'))
                        self.table.setItem(row, column, item)

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = Window(0, 0)
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())