# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'credentialswindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_credentialsWindow(object):
    def setupUi(self, credentialsWindow):
        credentialsWindow.setObjectName("credentialsWindow")
        credentialsWindow.resize(700, 285)
        credentialsWindow.setMinimumSize(QtCore.QSize(700, 285))
        credentialsWindow.setMaximumSize(QtCore.QSize(700, 285))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        credentialsWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/info_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        credentialsWindow.setWindowIcon(icon)
        credentialsWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(credentialsWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(credentialsWindow)
        self.label_1.setMinimumSize(QtCore.QSize(0, 75))
        self.label_1.setMaximumSize(QtCore.QSize(16777215, 95))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
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
        self.verticalLayout.addWidget(self.label_1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(credentialsWindow)
        self.label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.edit_1 = QtWidgets.QLineEdit(credentialsWindow)
        self.edit_1.setEnabled(True)
        self.edit_1.setMinimumSize(QtCore.QSize(0, 27))
        self.edit_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.edit_1.setFont(font)
        self.edit_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.edit_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200, 200, 200);\n"
"}")
        self.edit_1.setFrame(False)
        self.edit_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.edit_1.setObjectName("edit_1")
        self.gridLayout.addWidget(self.edit_1, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(credentialsWindow)
        self.label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.edit_2 = QtWidgets.QLineEdit(credentialsWindow)
        self.edit_2.setEnabled(True)
        self.edit_2.setMinimumSize(QtCore.QSize(0, 27))
        self.edit_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.edit_2.setFont(font)
        self.edit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.edit_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200, 200, 200);\n"
"}")
        self.edit_2.setFrame(False)
        self.edit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.edit_2.setObjectName("edit_2")
        self.gridLayout.addWidget(self.edit_2, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.submit = QtWidgets.QToolButton(credentialsWindow)
        self.submit.setMinimumSize(QtCore.QSize(90, 27))
        self.submit.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
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
        self.horizontalLayout_2.addWidget(self.submit)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.cancel = QtWidgets.QToolButton(credentialsWindow)
        self.cancel.setMinimumSize(QtCore.QSize(90, 27))
        self.cancel.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
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
        self.horizontalLayout_2.addWidget(self.cancel)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(credentialsWindow)
        QtCore.QMetaObject.connectSlotsByName(credentialsWindow)

    def retranslateUi(self, credentialsWindow):
        _translate = QtCore.QCoreApplication.translate
        credentialsWindow.setWindowTitle(_translate("credentialsWindow", "Information"))
        self.label_1.setText(_translate("credentialsWindow", "<html><head/><body><p>There is no password and/or username stored in the Option .ini file. A CMEMS account is mandatory to connect to the CMEMS Motu API. The username and password entered in the present window are not stored and used only for authentication with the CMEMS Motu API.</p></body></html>"))
        self.label_2.setText(_translate("credentialsWindow", "Username:"))
        self.label_3.setText(_translate("credentialsWindow", "Password:"))
        self.submit.setText(_translate("credentialsWindow", "Submit"))
        self.cancel.setText(_translate("credentialsWindow", "Cancel"))

