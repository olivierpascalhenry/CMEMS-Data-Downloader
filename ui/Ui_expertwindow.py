# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expertwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_expertWindow(object):
    def setupUi(self, expertWindow):
        expertWindow.setObjectName("expertWindow")
        expertWindow.resize(640, 569)
        expertWindow.setMinimumSize(QtCore.QSize(640, 450))
        expertWindow.setMaximumSize(QtCore.QSize(700, 600))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        expertWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/expert_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        expertWindow.setWindowIcon(icon)
        expertWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(expertWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_1 = QtWidgets.QLabel(expertWindow)
        self.label_1.setEnabled(True)
        self.label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_12.addWidget(self.label_1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(14)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.edit_3 = QtWidgets.QLineEdit(expertWindow)
        self.edit_3.setMinimumSize(QtCore.QSize(400, 27))
        self.edit_3.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.edit_3.setFont(font)
        self.edit_3.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.edit_3.setObjectName("edit_3")
        self.horizontalLayout_4.addWidget(self.edit_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.ew_infoButton_4 = QtWidgets.QToolButton(expertWindow)
        self.ew_infoButton_4.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_4.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ew_infoButton_4.setIcon(icon1)
        self.ew_infoButton_4.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_4.setAutoRaise(False)
        self.ew_infoButton_4.setObjectName("ew_infoButton_4")
        self.horizontalLayout_4.addWidget(self.ew_infoButton_4)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edit_2 = QtWidgets.QLineEdit(expertWindow)
        self.edit_2.setMinimumSize(QtCore.QSize(400, 27))
        self.edit_2.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.edit_2.setFont(font)
        self.edit_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.edit_2.setObjectName("edit_2")
        self.horizontalLayout_3.addWidget(self.edit_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.ew_infoButton_3 = QtWidgets.QToolButton(expertWindow)
        self.ew_infoButton_3.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_3.setText("")
        self.ew_infoButton_3.setIcon(icon1)
        self.ew_infoButton_3.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_3.setAutoRaise(False)
        self.ew_infoButton_3.setObjectName("ew_infoButton_3")
        self.horizontalLayout_3.addWidget(self.ew_infoButton_3)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(expertWindow)
        self.label_2.setEnabled(True)
        self.label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.edit_11 = QtWidgets.QLineEdit(expertWindow)
        self.edit_11.setMinimumSize(QtCore.QSize(400, 27))
        self.edit_11.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.edit_11.setFont(font)
        self.edit_11.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.edit_11.setObjectName("edit_11")
        self.horizontalLayout_17.addWidget(self.edit_11)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem4)
        self.ew_infoButton_1 = QtWidgets.QToolButton(expertWindow)
        self.ew_infoButton_1.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_1.setText("")
        self.ew_infoButton_1.setIcon(icon1)
        self.ew_infoButton_1.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_1.setAutoRaise(False)
        self.ew_infoButton_1.setObjectName("ew_infoButton_1")
        self.horizontalLayout_17.addWidget(self.ew_infoButton_1)
        self.gridLayout_3.addLayout(self.horizontalLayout_17, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(expertWindow)
        self.label_15.setEnabled(True)
        self.label_15.setMinimumSize(QtCore.QSize(0, 27))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.edit_1 = QtWidgets.QLineEdit(expertWindow)
        self.edit_1.setMinimumSize(QtCore.QSize(400, 27))
        self.edit_1.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.edit_1.setFont(font)
        self.edit_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.edit_1.setObjectName("edit_1")
        self.horizontalLayout_2.addWidget(self.edit_1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.ew_infoButton_2 = QtWidgets.QToolButton(expertWindow)
        self.ew_infoButton_2.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_2.setText("")
        self.ew_infoButton_2.setIcon(icon1)
        self.ew_infoButton_2.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_2.setAutoRaise(False)
        self.ew_infoButton_2.setObjectName("ew_infoButton_2")
        self.horizontalLayout_2.addWidget(self.ew_infoButton_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.edit_4 = QtWidgets.QLineEdit(expertWindow)
        self.edit_4.setMinimumSize(QtCore.QSize(400, 27))
        self.edit_4.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.edit_4.setFont(font)
        self.edit_4.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.edit_4.setObjectName("edit_4")
        self.horizontalLayout_5.addWidget(self.edit_4)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.ew_infoButton_5 = QtWidgets.QToolButton(expertWindow)
        self.ew_infoButton_5.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_5.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_5.setText("")
        self.ew_infoButton_5.setIcon(icon1)
        self.ew_infoButton_5.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_5.setAutoRaise(False)
        self.ew_infoButton_5.setObjectName("ew_infoButton_5")
        self.horizontalLayout_5.addWidget(self.ew_infoButton_5)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(expertWindow)
        self.label_3.setEnabled(True)
        self.label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(expertWindow)
        self.label_4.setEnabled(True)
        self.label_4.setMinimumSize(QtCore.QSize(0, 27))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(expertWindow)
        self.label_5.setEnabled(True)
        self.label_5.setMinimumSize(QtCore.QSize(0, 27))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.download_method = QtWidgets.QComboBox(expertWindow)
        self.download_method.setEnabled(True)
        self.download_method.setMinimumSize(QtCore.QSize(180, 27))
        self.download_method.setMaximumSize(QtCore.QSize(180, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.download_method.setFont(font)
        self.download_method.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(200,200,200);\n"
"    selection-color: black;\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 5px 5px 5px 5px;\n"
"}")
        self.download_method.setMaxVisibleItems(12)
        self.download_method.setObjectName("download_method")
        self.download_method.addItem("")
        self.download_method.addItem("")
        self.download_method.addItem("")
        self.download_method.addItem("")
        self.download_method.addItem("")
        self.download_method.addItem("")
        self.horizontalLayout_19.addWidget(self.download_method)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem7)
        self.ew_infoButton_10 = QtWidgets.QToolButton(expertWindow)
        self.ew_infoButton_10.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_10.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_10.setText("")
        self.ew_infoButton_10.setIcon(icon1)
        self.ew_infoButton_10.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_10.setAutoRaise(False)
        self.ew_infoButton_10.setObjectName("ew_infoButton_10")
        self.horizontalLayout_19.addWidget(self.ew_infoButton_10)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem8)
        self.gridLayout_3.addLayout(self.horizontalLayout_19, 5, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(expertWindow)
        self.label_16.setEnabled(True)
        self.label_16.setMinimumSize(QtCore.QSize(0, 27))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 5, 0, 1, 1)
        self.horizontalLayout_14.addLayout(self.gridLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem10)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_6 = QtWidgets.QLabel(expertWindow)
        self.label_6.setEnabled(True)
        self.label_6.setMinimumSize(QtCore.QSize(0, 27))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_13.addWidget(self.label_6)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem12)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem13)
        self.label_11 = QtWidgets.QLabel(expertWindow)
        self.label_11.setEnabled(True)
        self.label_11.setMinimumSize(QtCore.QSize(0, 27))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.gridLayout_5.addLayout(self.horizontalLayout_10, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(expertWindow)
        self.label_7.setEnabled(True)
        self.label_7.setMinimumSize(QtCore.QSize(0, 27))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.edit_7 = QtWidgets.QLineEdit(expertWindow)
        self.edit_7.setMinimumSize(QtCore.QSize(100, 27))
        self.edit_7.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.edit_7.setFont(font)
        self.edit_7.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.edit_7.setObjectName("edit_7")
        self.gridLayout_5.addWidget(self.edit_7, 1, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem14)
        self.label_12 = QtWidgets.QLabel(expertWindow)
        self.label_12.setEnabled(True)
        self.label_12.setMinimumSize(QtCore.QSize(0, 27))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.gridLayout_5.addLayout(self.horizontalLayout_9, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(expertWindow)
        self.label_8.setEnabled(True)
        self.label_8.setMinimumSize(QtCore.QSize(0, 27))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.edit_10 = QtWidgets.QLineEdit(expertWindow)
        self.edit_10.setMinimumSize(QtCore.QSize(100, 27))
        self.edit_10.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.edit_10.setFont(font)
        self.edit_10.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.edit_10.setObjectName("edit_10")
        self.horizontalLayout_8.addWidget(self.edit_10)
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem15)
        self.ew_infoButton_8 = QtWidgets.QToolButton(expertWindow)
        self.ew_infoButton_8.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_8.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_8.setText("")
        self.ew_infoButton_8.setIcon(icon1)
        self.ew_infoButton_8.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_8.setAutoRaise(False)
        self.ew_infoButton_8.setObjectName("ew_infoButton_8")
        self.horizontalLayout_8.addWidget(self.ew_infoButton_8)
        self.gridLayout_5.addLayout(self.horizontalLayout_8, 2, 3, 1, 1)
        self.edit_5 = QtWidgets.QLineEdit(expertWindow)
        self.edit_5.setMinimumSize(QtCore.QSize(100, 27))
        self.edit_5.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.edit_5.setFont(font)
        self.edit_5.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.edit_5.setObjectName("edit_5")
        self.gridLayout_5.addWidget(self.edit_5, 0, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.edit_6 = QtWidgets.QLineEdit(expertWindow)
        self.edit_6.setMinimumSize(QtCore.QSize(100, 27))
        self.edit_6.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.edit_6.setFont(font)
        self.edit_6.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.edit_6.setObjectName("edit_6")
        self.horizontalLayout_6.addWidget(self.edit_6)
        spacerItem16 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem16)
        self.ew_infoButton_6 = QtWidgets.QToolButton(expertWindow)
        self.ew_infoButton_6.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_6.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_6.setText("")
        self.ew_infoButton_6.setIcon(icon1)
        self.ew_infoButton_6.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_6.setAutoRaise(False)
        self.ew_infoButton_6.setObjectName("ew_infoButton_6")
        self.horizontalLayout_6.addWidget(self.ew_infoButton_6)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 0, 3, 1, 1)
        self.edit_9 = QtWidgets.QLineEdit(expertWindow)
        self.edit_9.setMinimumSize(QtCore.QSize(100, 27))
        self.edit_9.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.edit_9.setFont(font)
        self.edit_9.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.edit_9.setObjectName("edit_9")
        self.gridLayout_5.addWidget(self.edit_9, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(expertWindow)
        self.label_9.setEnabled(True)
        self.label_9.setMinimumSize(QtCore.QSize(0, 27))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 2, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem17)
        self.label_10 = QtWidgets.QLabel(expertWindow)
        self.label_10.setEnabled(True)
        self.label_10.setMinimumSize(QtCore.QSize(0, 27))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.gridLayout_5.addLayout(self.horizontalLayout_11, 0, 2, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.edit_8 = QtWidgets.QLineEdit(expertWindow)
        self.edit_8.setMinimumSize(QtCore.QSize(100, 27))
        self.edit_8.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.edit_8.setFont(font)
        self.edit_8.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.edit_8.setObjectName("edit_8")
        self.horizontalLayout_7.addWidget(self.edit_8)
        spacerItem18 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem18)
        self.ew_infoButton_7 = QtWidgets.QToolButton(expertWindow)
        self.ew_infoButton_7.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_7.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_7.setText("")
        self.ew_infoButton_7.setIcon(icon1)
        self.ew_infoButton_7.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_7.setAutoRaise(False)
        self.ew_infoButton_7.setObjectName("ew_infoButton_7")
        self.horizontalLayout_7.addWidget(self.ew_infoButton_7)
        self.gridLayout_5.addLayout(self.horizontalLayout_7, 1, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(expertWindow)
        self.label_13.setEnabled(True)
        self.label_13.setMinimumSize(QtCore.QSize(0, 27))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 3, 0, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem19)
        self.label_14 = QtWidgets.QLabel(expertWindow)
        self.label_14.setEnabled(True)
        self.label_14.setMinimumSize(QtCore.QSize(0, 27))
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_16.addWidget(self.label_14)
        self.gridLayout_5.addLayout(self.horizontalLayout_16, 3, 2, 1, 1)
        self.edit_12 = QtWidgets.QLineEdit(expertWindow)
        self.edit_12.setMinimumSize(QtCore.QSize(100, 27))
        self.edit_12.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.edit_12.setFont(font)
        self.edit_12.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.edit_12.setObjectName("edit_12")
        self.gridLayout_5.addWidget(self.edit_12, 3, 1, 1, 1)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.edit_13 = QtWidgets.QLineEdit(expertWindow)
        self.edit_13.setMinimumSize(QtCore.QSize(100, 27))
        self.edit_13.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.edit_13.setFont(font)
        self.edit_13.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.edit_13.setObjectName("edit_13")
        self.horizontalLayout_18.addWidget(self.edit_13)
        spacerItem20 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem20)
        self.ew_infoButton_9 = QtWidgets.QToolButton(expertWindow)
        self.ew_infoButton_9.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_9.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_9.setText("")
        self.ew_infoButton_9.setIcon(icon1)
        self.ew_infoButton_9.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_9.setAutoRaise(False)
        self.ew_infoButton_9.setObjectName("ew_infoButton_9")
        self.horizontalLayout_18.addWidget(self.ew_infoButton_9)
        self.gridLayout_5.addLayout(self.horizontalLayout_18, 3, 3, 1, 1)
        self.horizontalLayout_15.addLayout(self.gridLayout_5)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem21)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        spacerItem22 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem22)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem23 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem23)
        self.submit = QtWidgets.QToolButton(expertWindow)
        self.submit.setMinimumSize(QtCore.QSize(90, 27))
        self.submit.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.submit.setFont(font)
        self.submit.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.submit.setObjectName("submit")
        self.horizontalLayout.addWidget(self.submit)
        spacerItem24 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem24)
        self.cancel = QtWidgets.QToolButton(expertWindow)
        self.cancel.setMinimumSize(QtCore.QSize(90, 27))
        self.cancel.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem25)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(expertWindow)
        self.download_method.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(expertWindow)

    def retranslateUi(self, expertWindow):
        _translate = QtCore.QCoreApplication.translate
        expertWindow.setWindowTitle(_translate("expertWindow", "Raw Inputs"))
        self.label_1.setText(_translate("expertWindow", "Main keywords:"))
        self.label_2.setText(_translate("expertWindow", "service_id"))
        self.label_15.setText(_translate("expertWindow", "MOTU URL"))
        self.label_3.setText(_translate("expertWindow", "product_id:"))
        self.label_4.setText(_translate("expertWindow", "variables:"))
        self.label_5.setText(_translate("expertWindow", "file name:"))
        self.download_method.setItemText(0, _translate("expertWindow", "Make a choice..."))
        self.download_method.setItemText(1, _translate("expertWindow", "Check size - TDS"))
        self.download_method.setItemText(2, _translate("expertWindow", "Check size - DGF"))
        self.download_method.setItemText(3, _translate("expertWindow", "Download - TDS"))
        self.download_method.setItemText(4, _translate("expertWindow", "Download - DGF"))
        self.download_method.setItemText(5, _translate("expertWindow", "Download - FTP"))
        self.label_16.setText(_translate("expertWindow", "action:"))
        self.label_6.setText(_translate("expertWindow", "Period and area keywords:"))
        self.label_11.setText(_translate("expertWindow", "latitude_max:"))
        self.label_7.setText(_translate("expertWindow", "date_min:"))
        self.label_12.setText(_translate("expertWindow", "longitude_max:"))
        self.label_8.setText(_translate("expertWindow", "latitude_min:"))
        self.label_9.setText(_translate("expertWindow", "longitude_min:"))
        self.label_10.setText(_translate("expertWindow", "date_max:"))
        self.label_13.setText(_translate("expertWindow", "depth_min:"))
        self.label_14.setText(_translate("expertWindow", "depth_max:"))
        self.submit.setText(_translate("expertWindow", "Submit"))
        self.cancel.setText(_translate("expertWindow", "Cancel"))

