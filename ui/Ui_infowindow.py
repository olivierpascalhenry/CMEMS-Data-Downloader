# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infowindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_infoWindow(object):
    def setupUi(self, infoWindow):
        infoWindow.setObjectName("infoWindow")
        infoWindow.resize(450, 180)
        infoWindow.setMinimumSize(QtCore.QSize(450, 180))
        infoWindow.setMaximumSize(QtCore.QSize(452, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        infoWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/info_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        infoWindow.setWindowIcon(icon)
        infoWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(infoWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.iw_label_2 = QtWidgets.QLabel(infoWindow)
        self.iw_label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.iw_label_2.setMaximumSize(QtCore.QSize(50, 50))
        self.iw_label_2.setText("")
        self.iw_label_2.setPixmap(QtGui.QPixmap("icons/info_popup_icon.svg"))
        self.iw_label_2.setScaledContents(True)
        self.iw_label_2.setObjectName("iw_label_2")
        self.verticalLayout.addWidget(self.iw_label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.iw_label_1 = QtWidgets.QLabel(infoWindow)
        self.iw_label_1.setMinimumSize(QtCore.QSize(0, 0))
        self.iw_label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.iw_label_1.setFont(font)
        self.iw_label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.iw_label_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.iw_label_1.setLineWidth(0)
        self.iw_label_1.setMidLineWidth(0)
        self.iw_label_1.setText("")
        self.iw_label_1.setTextFormat(QtCore.Qt.AutoText)
        self.iw_label_1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.iw_label_1.setWordWrap(True)
        self.iw_label_1.setOpenExternalLinks(True)
        self.iw_label_1.setObjectName("iw_label_1")
        self.horizontalLayout.addWidget(self.iw_label_1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.iw_okButton = QtWidgets.QToolButton(infoWindow)
        self.iw_okButton.setMinimumSize(QtCore.QSize(90, 27))
        self.iw_okButton.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.iw_okButton.setFont(font)
        self.iw_okButton.setStyleSheet("QToolButton {\n"
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
        self.iw_okButton.setObjectName("iw_okButton")
        self.horizontalLayout_2.addWidget(self.iw_okButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(infoWindow)
        QtCore.QMetaObject.connectSlotsByName(infoWindow)

    def retranslateUi(self, infoWindow):
        _translate = QtCore.QCoreApplication.translate
        infoWindow.setWindowTitle(_translate("infoWindow", "Information"))
        self.iw_okButton.setText(_translate("infoWindow", "Ok"))

