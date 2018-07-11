# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectionwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectionWindow(object):
    def setupUi(self, selectionWindow):
        selectionWindow.setObjectName("selectionWindow")
        selectionWindow.resize(500, 180)
        selectionWindow.setMinimumSize(QtCore.QSize(500, 180))
        selectionWindow.setMaximumSize(QtCore.QSize(500, 180))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        selectionWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/warning_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        selectionWindow.setWindowIcon(icon)
        selectionWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(selectionWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sw_label_2 = QtWidgets.QLabel(selectionWindow)
        self.sw_label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.sw_label_2.setMaximumSize(QtCore.QSize(50, 50))
        self.sw_label_2.setText("")
        self.sw_label_2.setPixmap(QtGui.QPixmap("icons/warning_popup_icon.svg"))
        self.sw_label_2.setScaledContents(True)
        self.sw_label_2.setObjectName("sw_label_2")
        self.verticalLayout_2.addWidget(self.sw_label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.sw_label_1 = QtWidgets.QLabel(selectionWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sw_label_1.sizePolicy().hasHeightForWidth())
        self.sw_label_1.setSizePolicy(sizePolicy)
        self.sw_label_1.setMinimumSize(QtCore.QSize(0, 0))
        self.sw_label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.sw_label_1.setFont(font)
        self.sw_label_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.sw_label_1.setWordWrap(True)
        self.sw_label_1.setObjectName("sw_label_1")
        self.horizontalLayout.addWidget(self.sw_label_1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.sw_okButton = QtWidgets.QToolButton(selectionWindow)
        self.sw_okButton.setMinimumSize(QtCore.QSize(90, 27))
        self.sw_okButton.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.sw_okButton.setFont(font)
        self.sw_okButton.setStyleSheet("QToolButton {\n"
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
        self.sw_okButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.sw_okButton.setObjectName("sw_okButton")
        self.horizontalLayout_2.addWidget(self.sw_okButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(selectionWindow)
        QtCore.QMetaObject.connectSlotsByName(selectionWindow)

    def retranslateUi(self, selectionWindow):
        _translate = QtCore.QCoreApplication.translate
        selectionWindow.setWindowTitle(_translate("selectionWindow", "Warning"))
        self.sw_label_1.setText(_translate("selectionWindow", "<html><head/><body><p align=\"justify\">Few items haven\'t been selected and, thus, download can\'t start. Please check tabs and items in <span style=\" font-weight:600; color:#c80000;\">red</span> before clicking on <span style=\" font-weight:600;\">Download</span> again.</p></body></html>"))
        self.sw_okButton.setText(_translate("selectionWindow", "Ok"))

