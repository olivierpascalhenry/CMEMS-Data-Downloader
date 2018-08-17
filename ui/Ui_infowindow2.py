# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infowindow2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_infoWindow(object):
    def setupUi(self, infoWindow):
        infoWindow.setObjectName("infoWindow")
        infoWindow.resize(550, 200)
        infoWindow.setMinimumSize(QtCore.QSize(550, 0))
        infoWindow.setMaximumSize(QtCore.QSize(550, 16777215))
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
        self.gridLayout_2 = QtWidgets.QGridLayout(infoWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(infoWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.label_2.setMaximumSize(QtCore.QSize(50, 50))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("icons/info_popup_icon.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(infoWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setMinimumSize(QtCore.QSize(0, 0))
        self.label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_1.setFont(font)
        self.label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_1.setLineWidth(0)
        self.label_1.setMidLineWidth(0)
        self.label_1.setTextFormat(QtCore.Qt.AutoText)
        self.label_1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_1.setWordWrap(True)
        self.label_1.setOpenExternalLinks(True)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.button = QtWidgets.QToolButton(infoWindow)
        self.button.setMinimumSize(QtCore.QSize(90, 27))
        self.button.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.button.setFont(font)
        self.button.setStyleSheet("QToolButton {\n"
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
        self.button.setObjectName("button")
        self.horizontalLayout_2.addWidget(self.button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(infoWindow)
        QtCore.QMetaObject.connectSlotsByName(infoWindow)

    def retranslateUi(self, infoWindow):
        _translate = QtCore.QCoreApplication.translate
        infoWindow.setWindowTitle(_translate("infoWindow", "Information"))
        self.label_1.setText(_translate("infoWindow", "<html><head/><body><p align=\"justify\">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus mi elementum enim lacinia, ac mollis urna vehicula. In at eleifend purus, et auctor ante. Mauris a est sapien. Proin finibus a urna eget auctor. Nam porttitor est et nibh accumsan fermentum. Praesent finibus nisl orci, a pellentesque enim dignissim accumsan. Pellentesque ac nibh tincidunt, mattis neque ut, porttitor lacus. Donec ac posuere magna, eu lobortis metus. Suspendisse potenti.</p></body></html>"))
        self.button.setText(_translate("infoWindow", "Ok"))

