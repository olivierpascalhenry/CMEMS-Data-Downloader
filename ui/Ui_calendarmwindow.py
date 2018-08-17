# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendarmwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_calendarmWindow(object):
    def setupUi(self, calendarmWindow):
        calendarmWindow.setObjectName("calendarmWindow")
        calendarmWindow.resize(426, 224)
        calendarmWindow.setMinimumSize(QtCore.QSize(426, 224))
        calendarmWindow.setMaximumSize(QtCore.QSize(426, 224))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        calendarmWindow.setFont(font)
        calendarmWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(240,240,240);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(calendarmWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.past_button = QtWidgets.QToolButton(calendarmWindow)
        self.past_button.setMinimumSize(QtCore.QSize(27, 35))
        self.past_button.setMaximumSize(QtCore.QSize(27, 35))
        self.past_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.past_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/left_arrow_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.past_button.setIcon(icon)
        self.past_button.setIconSize(QtCore.QSize(23, 23))
        self.past_button.setAutoRaise(False)
        self.past_button.setObjectName("past_button")
        self.horizontalLayout.addWidget(self.past_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.year_sb = QtWidgets.QSpinBox(calendarmWindow)
        self.year_sb.setMinimumSize(QtCore.QSize(100, 35))
        self.year_sb.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.year_sb.setFont(font)
        self.year_sb.setStyleSheet("QSpinBox {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QSpinBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"")
        self.year_sb.setFrame(False)
        self.year_sb.setAlignment(QtCore.Qt.AlignCenter)
        self.year_sb.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.year_sb.setAccelerated(True)
        self.year_sb.setMaximum(2099)
        self.year_sb.setProperty("value", 2018)
        self.year_sb.setObjectName("year_sb")
        self.horizontalLayout.addWidget(self.year_sb)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.future_button = QtWidgets.QToolButton(calendarmWindow)
        self.future_button.setMinimumSize(QtCore.QSize(27, 35))
        self.future_button.setMaximumSize(QtCore.QSize(27, 35))
        self.future_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.future_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/right_arrow_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.future_button.setIcon(icon1)
        self.future_button.setIconSize(QtCore.QSize(23, 23))
        self.future_button.setAutoRaise(False)
        self.future_button.setObjectName("future_button")
        self.horizontalLayout.addWidget(self.future_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.line = QtWidgets.QFrame(calendarmWindow)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        spacerItem3 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.tableWidget = QtWidgets.QTableWidget(calendarmWindow)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tableWidget.setFont(font)
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"    selection-background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"    selection-color: black;\n"
"}\n"
"\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(2, 3, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(40)
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(calendarmWindow)
        QtCore.QMetaObject.connectSlotsByName(calendarmWindow)

    def retranslateUi(self, calendarmWindow):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("calendarmWindow", "January"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("calendarmWindow", "February"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("calendarmWindow", "March"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("calendarmWindow", "April"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("calendarmWindow", "May"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("calendarmWindow", "June"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("calendarmWindow", "July"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("calendarmWindow", "August"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("calendarmWindow", "September"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("calendarmWindow", "October"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("calendarmWindow", "November"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("calendarmWindow", "December"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

