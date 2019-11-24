# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\NLP\NLP_Python\NLP_Python\display.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from spell import correction, correctionText

class Ui_SpellingCorrection(object):
    def setupUi(self, SpellingCorrection):
        SpellingCorrection.setObjectName("SpellingCorrection")
        SpellingCorrection.resize(808, 560)
        self.centralwidget = QtWidgets.QWidget(SpellingCorrection)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 80, 93, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 400, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 140, 93, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(450, 20, 341, 221))
        self.listWidget.setObjectName("listWidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 60, 331, 141))
        self.textEdit.setObjectName("textEdit")
        SpellingCorrection.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SpellingCorrection)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 26))
        self.menubar.setObjectName("menubar")
        SpellingCorrection.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SpellingCorrection)
        self.statusbar.setObjectName("statusbar")
        SpellingCorrection.setStatusBar(self.statusbar)

        self.retranslateUi(SpellingCorrection)
        QtCore.QMetaObject.connectSlotsByName(SpellingCorrection)
        self.pushButton_2.clicked.connect(self.quit)
        self.pushButton.clicked.connect(self.showText)
        self.pushButton_3.clicked.connect(self.clear)
         
    def retranslateUi(self, SpellingCorrection):
        _translate = QtCore.QCoreApplication.translate
        SpellingCorrection.setWindowTitle(_translate("SpellingCorrection", "Spelling Correction"))
        self.pushButton.setText(_translate("SpellingCorrection", "Correction"))
        self.pushButton_2.setText(_translate("SpellingCorrection", "Quit"))
        self.pushButton_3.setText(_translate("SpellingCorrection", "Clear"))

    def quit(self):
        exit()
    
    def clear(self):
        self.listWidget.clear()

    def showText(self):
        value = self.textEdit.toPlainText()

        #self.lineEdit.clear()
        self.listWidget.addItem(correctionText(value))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SpellingCorrection = QtWidgets.QMainWindow()
    ui = Ui_SpellingCorrection()
    ui.setupUi(SpellingCorrection)
    SpellingCorrection.show()
    sys.exit(app.exec_())
