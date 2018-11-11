# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from datetime import datetime, date, timedelta

from conversation import Conversation
from person import Person

from tools import normalise_length
import gui_func

import pdb

class Ui_MainWindow(object):
    def __init__(self):
        self.current_conv = None
        self.list_of_conv = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.combobox_conversation = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_conversation.setGeometry(QtCore.QRect(10, 90, 291, 22))
        self.combobox_conversation.setObjectName("combobox_conversation")
        self.pushbutton_folder = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_folder.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.pushbutton_folder.setObjectName("pushbutton_folder")
        self.label_folder_path = QtWidgets.QLabel(self.centralwidget)
        self.label_folder_path.setGeometry(QtCore.QRect(120, 10, 661, 21))
        self.label_folder_path.setObjectName("label_folder_path")
        self.lineedit_beg_year = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_beg_year.setGeometry(QtCore.QRect(80, 140, 51, 22))
        self.lineedit_beg_year.setObjectName("lineedit_beg_year")
        self.label_beg_year = QtWidgets.QLabel(self.centralwidget)
        self.label_beg_year.setGeometry(QtCore.QRect(80, 120, 55, 16))
        self.label_beg_year.setObjectName("label_beg_year")
        self.label_beg_months = QtWidgets.QLabel(self.centralwidget)
        self.label_beg_months.setGeometry(QtCore.QRect(140, 120, 55, 16))
        self.label_beg_months.setObjectName("label_beg_months")
        self.lineedit_beg_month = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_beg_month.setGeometry(QtCore.QRect(140, 140, 51, 22))
        self.lineedit_beg_month.setObjectName("lineedit_beg_month")
        self.label_beg_day = QtWidgets.QLabel(self.centralwidget)
        self.label_beg_day.setGeometry(QtCore.QRect(200, 120, 55, 16))
        self.label_beg_day.setObjectName("label_beg_day")
        self.lineedit_beg_day = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_beg_day.setGeometry(QtCore.QRect(200, 140, 51, 22))
        self.lineedit_beg_day.setObjectName("lineedit_beg_day")
        self.label_beg = QtWidgets.QLabel(self.centralwidget)
        self.label_beg.setGeometry(QtCore.QRect(10, 140, 61, 21))
        self.label_beg.setObjectName("label_beg")
        self.lineedit_end_month = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_end_month.setGeometry(QtCore.QRect(430, 140, 51, 22))
        self.lineedit_end_month.setObjectName("lineedit_end_month")
        self.label_end_year = QtWidgets.QLabel(self.centralwidget)
        self.label_end_year.setGeometry(QtCore.QRect(370, 120, 55, 16))
        self.label_end_year.setObjectName("label_end_year")
        self.label_end_day = QtWidgets.QLabel(self.centralwidget)
        self.label_end_day.setGeometry(QtCore.QRect(490, 120, 55, 16))
        self.label_end_day.setObjectName("label_end_day")
        self.label_end_month = QtWidgets.QLabel(self.centralwidget)
        self.label_end_month.setGeometry(QtCore.QRect(430, 120, 55, 16))
        self.label_end_month.setObjectName("label_end_month")
        self.lineedit_end_year = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_end_year.setGeometry(QtCore.QRect(370, 140, 51, 22))
        self.lineedit_end_year.setObjectName("lineedit_end_year")
        self.lineedit_end_day = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_end_day.setGeometry(QtCore.QRect(490, 140, 51, 22))
        self.lineedit_end_day.setObjectName("lineedit_end_day")
        self.label_end = QtWidgets.QLabel(self.centralwidget)
        self.label_end.setGeometry(QtCore.QRect(330, 140, 21, 21))
        self.label_end.setObjectName("label_end")
        self.combobox_frequency = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_frequency.setGeometry(QtCore.QRect(82, 190, 111, 22))
        self.combobox_frequency.setObjectName("combobox_frequency")
        self.label_frequency = QtWidgets.QLabel(self.centralwidget)
        self.label_frequency.setGeometry(QtCore.QRect(10, 190, 61, 16))
        self.label_frequency.setObjectName("label_frequency")
        self.pushbutton_display = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_display.setGeometry(QtCore.QRect(10, 250, 93, 28))
        self.pushbutton_display.setObjectName("pushbutton_display")
        self.pushbutton_get_conv = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_get_conv.setGeometry(QtCore.QRect(10, 50, 111, 28))
        self.pushbutton_get_conv.setObjectName("pushbutton_get_conv")
        self.pushbutton_load_data = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_load_data.setGeometry(QtCore.QRect(530, 90, 211, 28))
        self.pushbutton_load_data.setObjectName("pushbutton_load_data")
        self.combobox_your_name = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_your_name.setGeometry(QtCore.QRect(320, 90, 191, 22))
        self.combobox_your_name.setObjectName("combobox_your_name")
        self.label_your_name = QtWidgets.QLabel(self.centralwidget)
        self.label_your_name.setGeometry(QtCore.QRect(320, 60, 71, 16))
        self.label_your_name.setObjectName("label_your_name")
        self.textbrowser_conv_stats = QtWidgets.QTextBrowser(self.centralwidget)
        self.textbrowser_conv_stats.setGeometry(QtCore.QRect(480, 200, 256, 331))
        self.textbrowser_conv_stats.setObjectName("textbrowser_conv_stats")
        self.label_conv_stats = QtWidgets.QLabel(self.centralwidget)
        self.label_conv_stats.setGeometry(QtCore.QRect(480, 180, 191, 16))
        self.label_conv_stats.setObjectName("label_conv_stats")
        self.combobox_visualisation_type = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_visualisation_type.setGeometry(QtCore.QRect(240, 250, 221, 22))
        self.combobox_visualisation_type.setObjectName("combobox_visualisation_type")
        self.label_visualisation_type = QtWidgets.QLabel(self.centralwidget)
        self.label_visualisation_type.setGeometry(QtCore.QRect(240, 230, 101, 16))
        self.label_visualisation_type.setObjectName("label_visualisation_type")
        self.combobox_data_to_visualise = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_data_to_visualise.setGeometry(QtCore.QRect(350, 190, 111, 22))
        self.combobox_data_to_visualise.setObjectName("combobox_data_to_visualise")
        self.label_data_to_visualise = QtWidgets.QLabel(self.centralwidget)
        self.label_data_to_visualise.setGeometry(QtCore.QRect(250, 190, 101, 16))
        self.label_data_to_visualise.setObjectName("label_data_to_visualise")
        self.pushbutton_export = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_export.setGeometry(QtCore.QRect(10, 530, 75, 23))
        self.pushbutton_export.setObjectName("pushbutton_export")
        self.combobox_export = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_export.setGeometry(QtCore.QRect(100, 530, 191, 22))
        self.combobox_export.setObjectName("combobox_export")
        self.lineedit_export = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_export.setGeometry(QtCore.QRect(310, 530, 113, 20))
        self.lineedit_export.setObjectName("lineedit_export")
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

        self.link()

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
        self.pushbutton_get_conv.setText(_translate("MainWindow", "Get conversations"))
        self.pushbutton_load_data.setText(_translate("MainWindow", "Load conversation data"))
        self.label_your_name.setText(_translate("MainWindow", "Your name:"))
        self.label_conv_stats.setText(_translate("MainWindow", "Statistics about the conversation"))
        self.label_visualisation_type.setText(_translate("MainWindow", "Visualisation type"))
        self.label_data_to_visualise.setText(_translate("MainWindow", "Data to visualise"))
        self.pushbutton_export.setText(_translate("MainWindow", "Export"))

    def link(self):
        self.pushbutton_folder.clicked.connect(self.select_file)

        self.pushbutton_get_conv.clicked.connect(self.get_conversations)

        self.combobox_conversation.activated.connect(self.set_names)

        self.pushbutton_load_data.clicked.connect(self.get_conv_data)

        self.combobox_frequency.addItem('Daily')
        self.combobox_frequency.addItem('Weekly')
        self.combobox_frequency.addItem('Monthly')
        self.combobox_frequency.addItem('Yearly')
        self.combobox_frequency.addItem('Total')

        self.pushbutton_display.clicked.connect(self.get_graph)

        self.combobox_visualisation_type.addItem('Stacked bar')
        self.combobox_visualisation_type.addItem('Stacked bar (percentage)')
        self.combobox_visualisation_type.addItem('Stacked bar (cumulative)')
        self.combobox_visualisation_type.addItem('Stacked area')
        self.combobox_visualisation_type.addItem('Stacked area (percentage)')
        self.combobox_visualisation_type.addItem('Stacked area (cumulative)')
        self.combobox_visualisation_type.addItem('Pie chart')
        self.combobox_visualisation_type.addItem('Area chart')


        self.combobox_data_to_visualise.addItem('Messages')
        self.combobox_data_to_visualise.addItem('Words')

        self.pushbutton_export.clicked.connect(self.export_messages)

    def select_file(self):
        self.label_folder_path.setText(QtWidgets.QFileDialog.getExistingDirectory())

    def get_conversations(self):
        lst = gui_func.set_conversation_list(self.label_folder_path.text())
        self.list_of_conv = lst
        for elem in lst:
            self.combobox_conversation.addItem(elem[0])

    def set_names(self):
        data = self.combobox_conversation.currentText()
        data = data.split(", ")
        self.combobox_your_name.clear()
        for elem in data:
            self.combobox_your_name.addItem(elem)
            self.combobox_export.addItem(elem)

    def get_conv_data(self):
        names = [x[1] for x in self.list_of_conv if x[0] == self.combobox_conversation.currentText()]

        if len(names) == 1:
            name = names[0]
            path = self.label_folder_path.text() + '/' + name
            self.current_conv = gui_func.load_conv_data(path)

        else:
            # Do " choose between conv " (same=participants, dates, nb messages pour chaque)
            pass

        self.textbrowser_conv_stats.setText(self.current_conv.get_basic_stats())

    def export_messages(self):
        filename = self.lineedit_export.text()
        
        if not filename:
            filename = 'data.txt'

        person = self.current_conv.persons[self.combobox_export.currentText()]

        with open(filename + '.txt', 'w', encoding='utf8') as of:
            for mess in person.messages:
                of.write(mess['content'].encode('latin1').decode('utf8') + '\n') 


    def get_graph(self):
        self.current_conv.get_all_messages()

        beg_y = int(self.lineedit_beg_year.text() or 0)
        beg_m = int(self.lineedit_beg_month.text() or 0)
        beg_d = int(self.lineedit_beg_day.text() or 0)

        end_y = int(self.lineedit_end_year.text() or 0)
        end_m = int(self.lineedit_end_month.text() or 0)
        end_d = int(self.lineedit_end_day.text() or 0)

        beg_extrem = datetime.utcfromtimestamp(self.current_conv.extremum_dates[0] / 1000)
        end_extrem = datetime.utcfromtimestamp(self.current_conv.extremum_dates[1] / 1000)

        if not beg_y or beg_extrem.year > beg_y > end_extrem.year:
            beg_y = beg_extrem.year

        if not beg_m or beg_extrem.month > beg_y > end_extrem.month:
            beg_m = beg_extrem.month

        if not beg_d or beg_extrem.day > beg_y > end_extrem.day:
            beg_d = beg_extrem.day

        if not end_y or beg_extrem.year > end_y > end_extrem.year:
            end_y = end_extrem.year

        if not end_m or beg_extrem.month > end_y > end_extrem.month:
            end_m = end_extrem.month

        if not end_d or beg_extrem.day > end_y > end_extrem.day:
            end_d = end_extrem.day

        beginning = datetime(beg_y, beg_m, beg_d)
        end = datetime(end_y, end_m, end_d)

        frequency = self.combobox_frequency.currentText()
        your_name = self.combobox_your_name.currentText()
        visualisation = self.combobox_visualisation_type.currentText()
        data_to_visualise = self.combobox_data_to_visualise.currentText()

        other_names = [x for x in self.current_conv.persons.keys() if x != your_name]
        names = [x for x in self.current_conv.persons.keys()]

        if frequency == 'Weekly' and data_to_visualise == 'Messages':
            gui_func.plot_multiple_data(self.current_conv.get_all_messages(dates=[beginning, end], frequency='Weekly'),
                                        names,
                                        [data_to_visualise, 'Weeks'],
                                        dates=[beginning, end],
                                        visualisation=visualisation)

        elif frequency == 'Weekly' and data_to_visualise == 'Words':
                gui_func.plot_multiple_data(self.current_conv.get_all_words(dates=[beginning, end], frequency='Weekly'),
                                        names,
                                        [data_to_visualise, 'Weeks'],
                                        dates=[beginning, end],
                                        visualisation=visualisation)

        elif frequency == 'Daily' and data_to_visualise == 'Messages':
            gui_func.plot_multiple_data(self.current_conv.get_all_messages(dates=[beginning, end], frequency='Daily'),
                                        names,
                                        [data_to_visualise, 'Days'],
                                        dates=[beginning, end],
                                        visualisation=visualisation)

        elif frequency == 'Daily' and data_to_visualise == 'Words':
            gui_func.plot_multiple_data(self.current_conv.get_all_words(dates=[beginning, end], frequency='Daily'),
                                        names,
                                        [data_to_visualise, 'Weeks'],
                                        dates=[beginning, end],
                                        visualisation=visualisation)

        elif frequency == 'Total' and data_to_visualise == 'Messages':
            gui_func.plot_pie_chart(self.current_conv.get_all_messages(dates=[beginning, end], frequency='Total'),
                                    names,
                                    [data_to_visualise, 'Total'],
                                    dates=[beginning, end],
                                    visualisation=visualisation)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

