#!/usr/bin/env python
#-*- coding:utf-8 -*-

import csv

from PyQt4 import QtGui, QtCore

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.model = QtGui.QStandardItemModel(self)

        self.tableView = QtGui.QTableView(self)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.pushButtonLoad = QtGui.QPushButton(self)
        self.pushButtonLoad.setText("Load Csv File!")
        self.pushButtonLoad.clicked.connect(self.loadCsv)

        self.pushButtonWrite = QtGui.QPushButton(self)
        self.pushButtonWrite.setText("Write Csv File!")
        self.pushButtonWrite.clicked.connect(self.writeCsv)

        self.layoutVertical = QtGui.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.tableView)
        self.layoutVertical.addWidget(self.pushButtonLoad)
        self.layoutVertical.addWidget(self.pushButtonWrite)

    def loadCsv(self, fileName):
        path = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '', 'CSV(*.csv)')
        if not path.isEmpty():
            with open(path, "rb") as fileInput:
                for row in csv.reader(fileInput, delimiter=';'):    
                    items = [
                        QtGui.QStandardItem(field)
                        for field in row
                    ]
                    self.model.appendRow(items)

    def writeCsv(self):
        path = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV(*.csv)')
        if not path.isEmpty():
            with open(path, "wb") as fileOutput:
                writer = csv.writer(fileOutput, delimiter=';')
                for rowNumber in range(self.model.rowCount()):
                    fields = [
                        self.model.data(
                            self.model.index(rowNumber, columnNumber),
                            QtCore.Qt.DisplayRole
                        )
                        for columnNumber in range(self.model.columnCount())
                    ]
                    writer.writerow(fields)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.show()

    sys.exit(app.exec_())