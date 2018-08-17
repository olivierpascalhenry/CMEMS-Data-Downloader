# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendardwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_calendardWindow(object):
    def setupUi(self, calendardWindow):
        calendardWindow.setObjectName("calendardWindow")
        calendardWindow.resize(586, 384)
        calendardWindow.setMinimumSize(QtCore.QSize(586, 384))
        calendardWindow.setMaximumSize(QtCore.QSize(586, 384))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        calendardWindow.setFont(font)
        calendardWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(240,240,240);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(calendardWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.past_button = QtWidgets.QToolButton(calendardWindow)
        self.past_button.setMinimumSize(QtCore.QSize(0, 35))
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
        self.year_sb = QtWidgets.QSpinBox(calendardWindow)
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
"\n"
"\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top left;\n"
"    width: 35px;\n"
"    border-width: 1px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(icons/up_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom left;\n"
"    width: 35px;\n"
"    border-width: 1px;\n"
"    border-top-width: 0;\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"")
        self.year_sb.setFrame(False)
        self.year_sb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.year_sb.setAccelerated(True)
        self.year_sb.setMaximum(2099)
        self.year_sb.setProperty("value", 2018)
        self.year_sb.setObjectName("year_sb")
        self.horizontalLayout.addWidget(self.year_sb)
        self.label_3 = QtWidgets.QLabel(calendardWindow)
        self.label_3.setMinimumSize(QtCore.QSize(30, 35))
        self.label_3.setMaximumSize(QtCore.QSize(30, 35))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.month_cb = QtWidgets.QComboBox(calendardWindow)
        self.month_cb.setEnabled(True)
        self.month_cb.setMinimumSize(QtCore.QSize(160, 35))
        self.month_cb.setMaximumSize(QtCore.QSize(160, 35))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.month_cb.setFont(font)
        self.month_cb.setStyleSheet("QComboBox {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: transparent;\n"
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
"    width: 35px;\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
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
        self.month_cb.setMaxVisibleItems(12)
        self.month_cb.setObjectName("month_cb")
        self.month_cb.addItem("")
        self.month_cb.addItem("")
        self.month_cb.addItem("")
        self.month_cb.addItem("")
        self.month_cb.addItem("")
        self.month_cb.addItem("")
        self.month_cb.addItem("")
        self.month_cb.addItem("")
        self.month_cb.addItem("")
        self.month_cb.addItem("")
        self.month_cb.addItem("")
        self.month_cb.addItem("")
        self.horizontalLayout.addWidget(self.month_cb)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.future_button = QtWidgets.QToolButton(calendardWindow)
        self.future_button.setMinimumSize(QtCore.QSize(0, 35))
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
        self.line = QtWidgets.QFrame(calendardWindow)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        spacerItem3 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.table = QtWidgets.QTableWidget(calendardWindow)
        self.table.setMinimumSize(QtCore.QSize(0, 0))
        self.table.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.table.setFont(font)
        self.table.setFocusPolicy(QtCore.Qt.NoFocus)
        self.table.setStyleSheet("QTableWidget {\n"
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
        self.table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table.setLineWidth(0)
        self.table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setGridStyle(QtCore.Qt.SolidLine)
        self.table.setRowCount(7)
        self.table.setColumnCount(7)
        self.table.setObjectName("table")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(230, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(230, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(230, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(230, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(230, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.table.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(230, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(230, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(2, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(3, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(4, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(4, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(5, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(5, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(6, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(6, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(6, 6, item)
        self.table.horizontalHeader().setVisible(False)
        self.table.horizontalHeader().setDefaultSectionSize(80)
        self.table.horizontalHeader().setHighlightSections(False)
        self.table.horizontalHeader().setMinimumSectionSize(80)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(40)
        self.table.verticalHeader().setHighlightSections(False)
        self.table.verticalHeader().setMinimumSectionSize(40)
        self.gridLayout.addWidget(self.table, 1, 0, 1, 1)

        self.retranslateUi(calendardWindow)
        self.month_cb.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(calendardWindow)

    def retranslateUi(self, calendardWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("calendardWindow", "-"))
        self.month_cb.setItemText(0, _translate("calendardWindow", "January"))
        self.month_cb.setItemText(1, _translate("calendardWindow", "February"))
        self.month_cb.setItemText(2, _translate("calendardWindow", "March"))
        self.month_cb.setItemText(3, _translate("calendardWindow", "April"))
        self.month_cb.setItemText(4, _translate("calendardWindow", "May"))
        self.month_cb.setItemText(5, _translate("calendardWindow", "June"))
        self.month_cb.setItemText(6, _translate("calendardWindow", "July"))
        self.month_cb.setItemText(7, _translate("calendardWindow", "August"))
        self.month_cb.setItemText(8, _translate("calendardWindow", "September"))
        self.month_cb.setItemText(9, _translate("calendardWindow", "October"))
        self.month_cb.setItemText(10, _translate("calendardWindow", "November"))
        self.month_cb.setItemText(11, _translate("calendardWindow", "December"))
        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        item = self.table.item(0, 0)
        item.setText(_translate("calendardWindow", "Mon."))
        item.setToolTip(_translate("calendardWindow", "Sunday"))
        item = self.table.item(0, 1)
        item.setText(_translate("calendardWindow", "Tue."))
        item.setToolTip(_translate("calendardWindow", "Monday"))
        item = self.table.item(0, 2)
        item.setText(_translate("calendardWindow", "Wed."))
        item.setToolTip(_translate("calendardWindow", "Tuesday"))
        item = self.table.item(0, 3)
        item.setText(_translate("calendardWindow", "Thu."))
        item.setToolTip(_translate("calendardWindow", "Wednesday"))
        item = self.table.item(0, 4)
        item.setText(_translate("calendardWindow", "Fri."))
        item.setToolTip(_translate("calendardWindow", "Thursday"))
        item = self.table.item(0, 5)
        item.setText(_translate("calendardWindow", "Sat."))
        item.setToolTip(_translate("calendardWindow", "Friday"))
        item = self.table.item(0, 6)
        item.setText(_translate("calendardWindow", "Sun."))
        item.setToolTip(_translate("calendardWindow", "Saturday"))
        self.table.setSortingEnabled(__sortingEnabled)

