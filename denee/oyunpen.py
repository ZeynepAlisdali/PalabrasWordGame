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
        MainWindow.resize(601, 321)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: Normal 15pt \"Impact\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 6, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("font: Normal 15pt \"Impact\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 8, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: Normal 15pt \"Impact\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setStyleSheet("font: Normal 15pt \"Impact\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 7, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setStyleSheet("font: Normal 15pt \"Impact\";")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 11, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.zaman = QtWidgets.QLabel(self.centralwidget)
        self.zaman.setStyleSheet("font: italic 10pt \"Impact\";")
        self.zaman.setObjectName("zaman")
        self.horizontalLayout_6.addWidget(self.zaman)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 14, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setStyleSheet("font: Normal 15pt \"Impact\";")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 10, 1, 1)
        self.basla = QtWidgets.QPushButton(self.centralwidget)
        self.basla.setStyleSheet("font: Normal 12pt \"Impact\";")
        self.basla.setObjectName("basla")
        self.gridLayout.addWidget(self.basla, 2, 0, 1, 1)
        self.kelime = QtWidgets.QLineEdit(self.centralwidget)
        self.kelime.setObjectName("kelime")
        self.gridLayout.addWidget(self.kelime, 1, 0, 1, 15)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("font: Normal 15pt \"Impact\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 9, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 13, 1, 1)
        self.durumtext = QtWidgets.QLabel(self.centralwidget)
        self.durumtext.setStyleSheet("font: Normal 10pt \"Impact\";\n"
"text-decoration: underline;")
        self.durumtext.setObjectName("durumtext")
        self.gridLayout.addWidget(self.durumtext, 2, 3, 1, 10)
        self.bitir = QtWidgets.QPushButton(self.centralwidget)
        self.bitir.setStyleSheet("font: Normal 12pt \"Impact\";")
        self.bitir.setObjectName("bitir")
        self.gridLayout.addWidget(self.bitir, 2, 14, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: Normal 15pt \"Impact\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: Normal 15pt \"Impact\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(120, 50, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setStyleSheet("font: Normal 15pt \"Impact\";")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(100, 50, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 12, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 21))
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
        self.label_4.setText(_translate("MainWindow", "A"))
        self.label_6.setText(_translate("MainWindow", "R"))
        self.label_3.setText(_translate("MainWindow", "L"))
        self.label_5.setText(_translate("MainWindow", "B"))
        self.label_9.setText(_translate("MainWindow", "*"))
        self.zaman.setText(_translate("MainWindow", "   Her  kelime\n"
"        için 30 \n"
" saniyeniz var"))
        self.label_8.setText(_translate("MainWindow", "S"))
        self.basla.setText(_translate("MainWindow", "B A Ş L A !"))
        self.kelime.setText(_translate("MainWindow", "Başlaya tıkladıktan sonra bu kutucuğa tahmininizi girip enter tuşuna basın"))
        self.label_7.setText(_translate("MainWindow", "A"))
        self.durumtext.setText(_translate("MainWindow", "Başla botununa bastınınızda ilk kelime için süreniz başlar"))
        self.bitir.setText(_translate("MainWindow", "Bitir"))
        self.label.setText(_translate("MainWindow", "P"))
        self.label_2.setText(_translate("MainWindow", "A"))
        self.label_10.setText(_translate("MainWindow", "*"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

