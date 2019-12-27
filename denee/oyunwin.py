# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oyunwin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(663, 308)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(100, 155, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.harflabel = QtWidgets.QLabel(self.centralwidget)
        self.harflabel.setStyleSheet("font: Normal 12pt \"Impact\";")
        self.harflabel.setObjectName("harflabel")
        self.gridLayout.addWidget(self.harflabel, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(140, 155, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.zaman = QtWidgets.QLabel(self.centralwidget)
        self.zaman.setStyleSheet("font: italic 11pt \"Impact\";")
        self.zaman.setObjectName("zaman")
        self.horizontalLayout_6.addWidget(self.zaman)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 3, 1, 1)
        self.kelime = QtWidgets.QLineEdit(self.centralwidget)
        self.kelime.setObjectName("kelime")
        self.gridLayout.addWidget(self.kelime, 1, 0, 1, 3)
        self.tahmin = QtWidgets.QPushButton(self.centralwidget)
        self.tahmin.setStyleSheet("font: Normal 12pt \"Impact\";")
        self.tahmin.setObjectName("tahmin")
        self.gridLayout.addWidget(self.tahmin, 1, 3, 1, 1)
        self.durumtext = QtWidgets.QLabel(self.centralwidget)
        self.durumtext.setStyleSheet("font: italic 9pt \"Impact\";\n"
"text-decoration: underline;")
        self.durumtext.setObjectName("durumtext")
        self.gridLayout.addWidget(self.durumtext, 2, 0, 1, 3)
        self.bitir = QtWidgets.QPushButton(self.centralwidget)
        self.bitir.setStyleSheet("font: Normal 10pt \"Impact\";")
        self.bitir.setObjectName("bitir")
        self.gridLayout.addWidget(self.bitir, 2, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 663, 21))
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
        self.harflabel.setText(_translate("MainWindow", "harfler"))
        self.zaman.setText(_translate("MainWindow", "   Her  kelime\n"
"        için 30 \n"
" saniyeniz var"))
        self.tahmin.setText(_translate("MainWindow", "Tahmin Et !"))
        self.durumtext.setText(_translate("MainWindow", "durum\n"
" çubuğu \n"
" texti"))
        self.bitir.setText(_translate("MainWindow", "Bitir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

