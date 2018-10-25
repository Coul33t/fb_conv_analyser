# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import gui_func

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.combobox_conversation = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_conversation.setGeometry(QtCore.QRect(10, 50, 600, 22))
        self.combobox_conversation.setObjectName("combobox_conversation")

        self.pushbutton_folder = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_folder.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.pushbutton_folder.setObjectName("pushbutton_folder")

        self.label_folder_path = QtWidgets.QLabel(self.centralwidget)
        self.label_folder_path.setGeometry(QtCore.QRect(120, 10, 661, 21))
        self.label_folder_path.setObjectName("label_folder_path")

        self.lineedit_beg_year = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_beg_year.setGeometry(QtCore.QRect(80, 100, 51, 22))
        self.lineedit_beg_year.setObjectName("lineedit_beg_year")

        self.label_beg_year = QtWidgets.QLabel(self.centralwidget)
        self.label_beg_year.setGeometry(QtCore.QRect(80, 80, 55, 16))
        self.label_beg_year.setObjectName("label_beg_year")

        self.label_beg_months = QtWidgets.QLabel(self.centralwidget)
        self.label_beg_months.setGeometry(QtCore.QRect(140, 80, 55, 16))
        self.label_beg_months.setObjectName("label_beg_months")

        self.lineedit_beg_month = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_beg_month.setGeometry(QtCore.QRect(140, 100, 51, 22))
        self.lineedit_beg_month.setObjectName("lineedit_beg_month")

        self.label_beg_day = QtWidgets.QLabel(self.centralwidget)
        self.label_beg_day.setGeometry(QtCore.QRect(200, 80, 55, 16))
        self.label_beg_day.setObjectName("label_beg_day")

        self.lineedit_beg_day = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_beg_day.setGeometry(QtCore.QRect(200, 100, 51, 22))
        self.lineedit_beg_day.setObjectName("lineedit_beg_day")

        self.label_beg = QtWidgets.QLabel(self.centralwidget)
        self.label_beg.setGeometry(QtCore.QRect(10, 100, 61, 21))
        self.label_beg.setObjectName("label_beg")

        self.lineedit_end_month = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_end_month.setGeometry(QtCore.QRect(430, 100, 51, 22))
        self.lineedit_end_month.setObjectName("lineedit_end_month")

        self.label_end_year = QtWidgets.QLabel(self.centralwidget)
        self.label_end_year.setGeometry(QtCore.QRect(370, 80, 55, 16))
        self.label_end_year.setObjectName("label_end_year")

        self.label_end_day = QtWidgets.QLabel(self.centralwidget)
        self.label_end_day.setGeometry(QtCore.QRect(490, 80, 55, 16))
        self.label_end_day.setObjectName("label_end_day")

        self.label_end_month = QtWidgets.QLabel(self.centralwidget)
        self.label_end_month.setGeometry(QtCore.QRect(430, 80, 55, 16))
        self.label_end_month.setObjectName("label_end_month")

        self.lineedit_end_year = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_end_year.setGeometry(QtCore.QRect(370, 100, 51, 22))
        self.lineedit_end_year.setObjectName("lineedit_end_year")

        self.lineedit_end_day = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_end_day.setGeometry(QtCore.QRect(490, 100, 51, 22))
        self.lineedit_end_day.setObjectName("lineedit_end_day")

        self.label_end = QtWidgets.QLabel(self.centralwidget)
        self.label_end.setGeometry(QtCore.QRect(330, 100, 21, 21))
        self.label_end.setObjectName("label_end")

        self.combobox_frequency = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_frequency.setGeometry(QtCore.QRect(82, 150, 111, 22))
        self.combobox_frequency.setObjectName("combobox_frequency")

        self.label_frequency = QtWidgets.QLabel(self.centralwidget)
        self.label_frequency.setGeometry(QtCore.QRect(10, 150, 61, 16))
        self.label_frequency.setObjectName("label_frequency")

        self.pushbutton_display = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_display.setGeometry(QtCore.QRect(10, 210, 93, 28))
        self.pushbutton_display.setObjectName("pushbutton_display")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushbutton_folder.clicked.connect(self.selectFile)

        gui_func.set_conversation_list(self.combobox_conversation)

        self.combobox_frequency.addItem('Daily')
        self.combobox_frequency.addItem('Weekly')
        self.combobox_frequency.addItem('Monthly')
        self.combobox_frequency.addItem('Yearly')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushbutton_folder.setText(_translate("MainWindow", "Folder"))
        self.label_folder_path.setText(_translate("MainWindow", "Folder path"))
        self.label_beg_year.setText(_translate("MainWindow", "Year"))
        self.label_beg_months.setText(_translate("MainWindow", "Month"))
        self.label_beg_day.setText(_translate("MainWindow", "Day"))
        self.label_beg.setText(_translate("MainWindow", "Beginning"))
        self.label_end_year.setText(_translate("MainWindow", "Year"))
        self.label_end_day.setText(_translate("MainWindow", "Day"))
        self.label_end_month.setText(_translate("MainWindow", "Month"))
        self.label_end.setText(_translate("MainWindow", "End"))
        self.label_frequency.setText(_translate("MainWindow", "Frequency"))
        self.pushbutton_display.setText(_translate("MainWindow", "Display"))

    def selectFile(self):
        self.label_folder_path.setText(QtWidgets.QFileDialog.getExistingDirectory())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

