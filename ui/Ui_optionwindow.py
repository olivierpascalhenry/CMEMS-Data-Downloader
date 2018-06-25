# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optionwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_optionWindow(object):
    def setupUi(self, optionWindow):
        optionWindow.setObjectName("optionWindow")
        optionWindow.resize(710, 446)
        optionWindow.setMinimumSize(QtCore.QSize(710, 446))
        optionWindow.setMaximumSize(QtCore.QSize(710, 446))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        optionWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/option_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        optionWindow.setWindowIcon(icon)
        optionWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(optionWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ow_label_4 = QtWidgets.QLabel(optionWindow)
        self.ow_label_4.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_4.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_4.setFont(font)
        self.ow_label_4.setObjectName("ow_label_4")
        self.gridLayout.addWidget(self.ow_label_4, 4, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ow_lineEdit_3 = QtWidgets.QLineEdit(optionWindow)
        self.ow_lineEdit_3.setMinimumSize(QtCore.QSize(400, 27))
        self.ow_lineEdit_3.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_lineEdit_3.setFont(font)
        self.ow_lineEdit_3.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.ow_lineEdit_3.setObjectName("ow_lineEdit_3")
        self.horizontalLayout_4.addWidget(self.ow_lineEdit_3)
        spacerItem = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.ow_infoButton_4 = QtWidgets.QToolButton(optionWindow)
        self.ow_infoButton_4.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_4.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_infoButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ow_infoButton_4.setIcon(icon1)
        self.ow_infoButton_4.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_4.setAutoRaise(False)
        self.ow_infoButton_4.setObjectName("ow_infoButton_4")
        self.horizontalLayout_4.addWidget(self.ow_infoButton_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 1, 1, 1)
        self.ow_label_5 = QtWidgets.QLabel(optionWindow)
        self.ow_label_5.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_5.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_5.setFont(font)
        self.ow_label_5.setObjectName("ow_label_5")
        self.gridLayout.addWidget(self.ow_label_5, 5, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ow_lineEdit_2 = QtWidgets.QLineEdit(optionWindow)
        self.ow_lineEdit_2.setMinimumSize(QtCore.QSize(400, 27))
        self.ow_lineEdit_2.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_lineEdit_2.setFont(font)
        self.ow_lineEdit_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.ow_lineEdit_2.setObjectName("ow_lineEdit_2")
        self.horizontalLayout_3.addWidget(self.ow_lineEdit_2)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.ow_infoButton_3 = QtWidgets.QToolButton(optionWindow)
        self.ow_infoButton_3.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_infoButton_3.setText("")
        self.ow_infoButton_3.setIcon(icon1)
        self.ow_infoButton_3.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_3.setAutoRaise(False)
        self.ow_infoButton_3.setObjectName("ow_infoButton_3")
        self.horizontalLayout_3.addWidget(self.ow_infoButton_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(14, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.line_3 = QtWidgets.QFrame(optionWindow)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        spacerItem5 = QtWidgets.QSpacerItem(14, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 2)
        self.ow_label_2 = QtWidgets.QLabel(optionWindow)
        self.ow_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_2.setFont(font)
        self.ow_label_2.setObjectName("ow_label_2")
        self.gridLayout.addWidget(self.ow_label_2, 1, 0, 1, 1)
        self.ow_label_3 = QtWidgets.QLabel(optionWindow)
        self.ow_label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_3.setFont(font)
        self.ow_label_3.setObjectName("ow_label_3")
        self.gridLayout.addWidget(self.ow_label_3, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ow_lineEdit_1 = QtWidgets.QLineEdit(optionWindow)
        self.ow_lineEdit_1.setMinimumSize(QtCore.QSize(400, 27))
        self.ow_lineEdit_1.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_lineEdit_1.setFont(font)
        self.ow_lineEdit_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.ow_lineEdit_1.setObjectName("ow_lineEdit_1")
        self.horizontalLayout.addWidget(self.ow_lineEdit_1)
        self.ow_openButton_1 = QtWidgets.QToolButton(optionWindow)
        self.ow_openButton_1.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_openButton_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_openButton_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/open_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ow_openButton_1.setIcon(icon2)
        self.ow_openButton_1.setIconSize(QtCore.QSize(23, 23))
        self.ow_openButton_1.setAutoRaise(False)
        self.ow_openButton_1.setObjectName("ow_openButton_1")
        self.horizontalLayout.addWidget(self.ow_openButton_1)
        spacerItem6 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.ow_infoButton_2 = QtWidgets.QToolButton(optionWindow)
        self.ow_infoButton_2.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_infoButton_2.setText("")
        self.ow_infoButton_2.setIcon(icon1)
        self.ow_infoButton_2.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_2.setAutoRaise(False)
        self.ow_infoButton_2.setObjectName("ow_infoButton_2")
        self.horizontalLayout.addWidget(self.ow_infoButton_2)
        spacerItem7 = QtWidgets.QSpacerItem(13, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ow_comboBox_1 = QtWidgets.QComboBox(optionWindow)
        self.ow_comboBox_1.setMinimumSize(QtCore.QSize(100, 27))
        self.ow_comboBox_1.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_comboBox_1.setFont(font)
        self.ow_comboBox_1.setStyleSheet("QComboBox {\n"
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
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
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
"QComboBox::down-arrow:on {\n"
"    top: 1px; \n"
"    left: 1px;\n"
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
        self.ow_comboBox_1.setObjectName("ow_comboBox_1")
        self.ow_comboBox_1.addItem("")
        self.ow_comboBox_1.addItem("")
        self.ow_comboBox_1.addItem("")
        self.ow_comboBox_1.addItem("")
        self.ow_comboBox_1.addItem("")
        self.horizontalLayout_7.addWidget(self.ow_comboBox_1)
        spacerItem8 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.ow_infoButton_1 = QtWidgets.QToolButton(optionWindow)
        self.ow_infoButton_1.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_infoButton_1.setText("")
        self.ow_infoButton_1.setIcon(icon1)
        self.ow_infoButton_1.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_1.setAutoRaise(False)
        self.ow_infoButton_1.setObjectName("ow_infoButton_1")
        self.horizontalLayout_7.addWidget(self.ow_infoButton_1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ow_lineEdit_4 = QtWidgets.QLineEdit(optionWindow)
        self.ow_lineEdit_4.setMinimumSize(QtCore.QSize(400, 27))
        self.ow_lineEdit_4.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_lineEdit_4.setFont(font)
        self.ow_lineEdit_4.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.ow_lineEdit_4.setObjectName("ow_lineEdit_4")
        self.horizontalLayout_5.addWidget(self.ow_lineEdit_4)
        spacerItem10 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.ow_infoButton_5 = QtWidgets.QToolButton(optionWindow)
        self.ow_infoButton_5.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_5.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_infoButton_5.setText("")
        self.ow_infoButton_5.setIcon(icon1)
        self.ow_infoButton_5.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_5.setAutoRaise(False)
        self.ow_infoButton_5.setObjectName("ow_infoButton_5")
        self.horizontalLayout_5.addWidget(self.ow_infoButton_5)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 1, 1, 1)
        self.ow_label_1 = QtWidgets.QLabel(optionWindow)
        self.ow_label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_1.setFont(font)
        self.ow_label_1.setObjectName("ow_label_1")
        self.gridLayout.addWidget(self.ow_label_1, 0, 0, 1, 1)
        self.ow_label_6 = QtWidgets.QLabel(optionWindow)
        self.ow_label_6.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_6.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_6.setFont(font)
        self.ow_label_6.setObjectName("ow_label_6")
        self.gridLayout.addWidget(self.ow_label_6, 6, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.ow_lineEdit_5 = QtWidgets.QLineEdit(optionWindow)
        self.ow_lineEdit_5.setMinimumSize(QtCore.QSize(400, 27))
        self.ow_lineEdit_5.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_lineEdit_5.setFont(font)
        self.ow_lineEdit_5.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.ow_lineEdit_5.setObjectName("ow_lineEdit_5")
        self.horizontalLayout_9.addWidget(self.ow_lineEdit_5)
        self.ow_openButton_2 = QtWidgets.QToolButton(optionWindow)
        self.ow_openButton_2.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_openButton_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_openButton_2.setText("")
        self.ow_openButton_2.setIcon(icon2)
        self.ow_openButton_2.setIconSize(QtCore.QSize(23, 23))
        self.ow_openButton_2.setAutoRaise(False)
        self.ow_openButton_2.setObjectName("ow_openButton_2")
        self.horizontalLayout_9.addWidget(self.ow_openButton_2)
        spacerItem12 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem12)
        self.ow_infoButton_8 = QtWidgets.QToolButton(optionWindow)
        self.ow_infoButton_8.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_8.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_infoButton_8.setText("")
        self.ow_infoButton_8.setIcon(icon1)
        self.ow_infoButton_8.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_8.setAutoRaise(False)
        self.ow_infoButton_8.setObjectName("ow_infoButton_8")
        self.horizontalLayout_9.addWidget(self.ow_infoButton_8)
        spacerItem13 = QtWidgets.QSpacerItem(13, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem13)
        self.gridLayout.addLayout(self.horizontalLayout_9, 6, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem14 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem14)
        self.line = QtWidgets.QFrame(optionWindow)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        spacerItem15 = QtWidgets.QSpacerItem(14, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem15)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ow_checkBox_1 = QtWidgets.QCheckBox(optionWindow)
        self.ow_checkBox_1.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkBox_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_checkBox_1.setFont(font)
        self.ow_checkBox_1.setChecked(False)
        self.ow_checkBox_1.setObjectName("ow_checkBox_1")
        self.horizontalLayout_8.addWidget(self.ow_checkBox_1)
        spacerItem16 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem16)
        self.ow_infoButton_6 = QtWidgets.QToolButton(optionWindow)
        self.ow_infoButton_6.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_6.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_infoButton_6.setText("")
        self.ow_infoButton_6.setIcon(icon1)
        self.ow_infoButton_6.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_6.setAutoRaise(False)
        self.ow_infoButton_6.setObjectName("ow_infoButton_6")
        self.horizontalLayout_8.addWidget(self.ow_infoButton_6)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem17)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ow_checkBox_2 = QtWidgets.QCheckBox(optionWindow)
        self.ow_checkBox_2.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkBox_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_checkBox_2.setFont(font)
        self.ow_checkBox_2.setObjectName("ow_checkBox_2")
        self.horizontalLayout_6.addWidget(self.ow_checkBox_2)
        spacerItem18 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem18)
        self.ow_infoButton_7 = QtWidgets.QToolButton(optionWindow)
        self.ow_infoButton_7.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_7.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_infoButton_7.setText("")
        self.ow_infoButton_7.setIcon(icon1)
        self.ow_infoButton_7.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_7.setAutoRaise(False)
        self.ow_infoButton_7.setObjectName("ow_infoButton_7")
        self.horizontalLayout_6.addWidget(self.ow_infoButton_7)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem19)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem20 = QtWidgets.QSpacerItem(138, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem20)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem21 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem21)
        self.ow_okButton = QtWidgets.QToolButton(optionWindow)
        self.ow_okButton.setMinimumSize(QtCore.QSize(90, 27))
        self.ow_okButton.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ow_okButton.setFont(font)
        self.ow_okButton.setStyleSheet("QToolButton {\n"
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
        self.ow_okButton.setObjectName("ow_okButton")
        self.horizontalLayout_2.addWidget(self.ow_okButton)
        spacerItem22 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem22)
        self.ow_cancelButton = QtWidgets.QToolButton(optionWindow)
        self.ow_cancelButton.setMinimumSize(QtCore.QSize(90, 27))
        self.ow_cancelButton.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ow_cancelButton.setFont(font)
        self.ow_cancelButton.setStyleSheet("QToolButton {\n"
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
        self.ow_cancelButton.setObjectName("ow_cancelButton")
        self.horizontalLayout_2.addWidget(self.ow_cancelButton)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem23)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(optionWindow)
        QtCore.QMetaObject.connectSlotsByName(optionWindow)

    def retranslateUi(self, optionWindow):
        _translate = QtCore.QCoreApplication.translate
        optionWindow.setWindowTitle(_translate("optionWindow", "Options"))
        self.ow_label_4.setText(_translate("optionWindow", "Username:"))
        self.ow_label_5.setText(_translate("optionWindow", "Password:"))
        self.ow_label_2.setText(_translate("optionWindow", "Path of the logging file:"))
        self.ow_label_3.setText(_translate("optionWindow", "API URL:"))
        self.ow_comboBox_1.setItemText(0, _translate("optionWindow", "DEBUG"))
        self.ow_comboBox_1.setItemText(1, _translate("optionWindow", "INFO"))
        self.ow_comboBox_1.setItemText(2, _translate("optionWindow", "WARNING"))
        self.ow_comboBox_1.setItemText(3, _translate("optionWindow", "CRITICAL"))
        self.ow_comboBox_1.setItemText(4, _translate("optionWindow", "ERROR"))
        self.ow_label_1.setText(_translate("optionWindow", "Logging level:"))
        self.ow_label_6.setText(_translate("optionWindow", "CMEMS file folder:"))
        self.ow_checkBox_1.setText(_translate("optionWindow", "Display CMEMS web API information at startup"))
        self.ow_checkBox_2.setText(_translate("optionWindow", "Check CMEMS Data Downloader updates on GitHub"))
        self.ow_okButton.setText(_translate("optionWindow", "Ok"))
        self.ow_cancelButton.setText(_translate("optionWindow", "Cancel"))

