# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tasarimim.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(608, 327)
        MainWindow.setStyleSheet("font: italic 8pt \"Impact\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.basla = QtWidgets.QPushButton(self.centralwidget)
        self.basla.setGeometry(QtCore.QRect(200, 190, 191, 91))
        self.basla.setStyleSheet("font: Normal 14pt \"Impact\";")
        self.basla.setObjectName("basla")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 70, 531, 121))
        self.label.setStyleSheet("font: italic 11pt \"Impact\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 20, 181, 51))
        self.label_2.setStyleSheet("background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(145, 72, 218, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"Viner Hand ITC\";")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 608, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.basla.setText(_translate("MainWindow", "B A Ş L A"))
        self.label.setText(_translate("MainWindow", " Karışık verilmiş harflerden doğru kelimeyi bulun. \n"
" Ne kadar hızlı cevap verirseniz o kadar yüksek puan alırısnız.\n"
" Doğru cevaplar 30 saniye içinde verilmezse puan alamazsınz.\n"
"Yanlış cevaplar 30 saniye içinde verilmişse 5, Verilmemişse 10 puan kaybedersiniz!"))
        self.label_2.setText(_translate("MainWindow", "           PALABRAS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

