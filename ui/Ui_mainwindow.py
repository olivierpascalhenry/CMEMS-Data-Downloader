# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1046, 550)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/cmems_data_downloader_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 340))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px solid rgb(180,180,180);\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    top: -1px;\n"
"    background-color: rgb(230,230,230);\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0px; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: transparent;\n"
"    border-top: 1px solid rgb(180,180,180);\n"
"    border-left: 1px solid rgb(180,180,180);\n"
"    border-right: 1px solid rgb(180,180,180);\n"
"    border-top-right-radius: 5px;\n"
"    border-top-left-radius: 5px;\n"
"    padding: 2px 10px 2px 10px;\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: rgb(210,210,210);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgb(230,230,230);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 4px; \n"
"}\n"
"\n"
"QTabBar::scroller {\n"
"}\n"
"\n"
"QTabBar QToolButton {\n"
"    border: 1px solid rgb(180,180,180);\n"
"    background-color: rgb(240,240,240);\n"
"}\n"
"\n"
"QTabBar QToolButton:hover {\n"
"    background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow {\n"
"    image: url(icons/right_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin : 2px 2px 2px 2px;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:pressed {\n"
"    right: -1px;\n"
"    bottom: -1px;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow {\n"
"    image: url(icons/left_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin : 2px 2px 2px 2px;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:pressed {\n"
"    right: -1px;\n"
"    bottom: -1px;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.tabWidgetPage1)
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.information_scroll_area = QtWidgets.QScrollArea(self.tabWidgetPage1)
        self.information_scroll_area.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"  border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"  border-top-right-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"  border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.information_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.information_scroll_area.setWidgetResizable(True)
        self.information_scroll_area.setObjectName("information_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1000, 356))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.main_lb_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_lb_1.sizePolicy().hasHeightForWidth())
        self.main_lb_1.setSizePolicy(sizePolicy)
        self.main_lb_1.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_1.setFont(font)
        self.main_lb_1.setObjectName("main_lb_1")
        self.gridLayout.addWidget(self.main_lb_1, 0, 0, 1, 1)
        self.main_cb_1 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.main_cb_1.setEnabled(True)
        self.main_cb_1.setMinimumSize(QtCore.QSize(180, 27))
        self.main_cb_1.setMaximumSize(QtCore.QSize(180, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_cb_1.setFont(font)
        self.main_cb_1.setStyleSheet("QComboBox {\n"
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
        self.main_cb_1.setMaxVisibleItems(12)
        self.main_cb_1.setObjectName("main_cb_1")
        self.main_cb_1.addItem("")
        self.main_cb_1.addItem("")
        self.main_cb_1.addItem("")
        self.main_cb_1.addItem("")
        self.main_cb_1.addItem("")
        self.main_cb_1.addItem("")
        self.gridLayout.addWidget(self.main_cb_1, 0, 1, 1, 1)
        self.main_lb_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_lb_2.sizePolicy().hasHeightForWidth())
        self.main_lb_2.setSizePolicy(sizePolicy)
        self.main_lb_2.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_2.setFont(font)
        self.main_lb_2.setObjectName("main_lb_2")
        self.gridLayout.addWidget(self.main_lb_2, 1, 0, 1, 1)
        self.main_cb_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.main_cb_2.setEnabled(False)
        self.main_cb_2.setMinimumSize(QtCore.QSize(180, 27))
        self.main_cb_2.setMaximumSize(QtCore.QSize(180, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_cb_2.setFont(font)
        self.main_cb_2.setStyleSheet("QComboBox {\n"
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
        self.main_cb_2.setMaxVisibleItems(12)
        self.main_cb_2.setObjectName("main_cb_2")
        self.main_cb_2.addItem("")
        self.gridLayout.addWidget(self.main_cb_2, 1, 1, 1, 1)
        self.main_lb_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_lb_3.sizePolicy().hasHeightForWidth())
        self.main_lb_3.setSizePolicy(sizePolicy)
        self.main_lb_3.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_3.setFont(font)
        self.main_lb_3.setObjectName("main_lb_3")
        self.gridLayout.addWidget(self.main_lb_3, 2, 0, 1, 1)
        self.main_cb_3 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.main_cb_3.setEnabled(False)
        self.main_cb_3.setMinimumSize(QtCore.QSize(180, 27))
        self.main_cb_3.setMaximumSize(QtCore.QSize(180, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_cb_3.setFont(font)
        self.main_cb_3.setStyleSheet("QComboBox {\n"
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
        self.main_cb_3.setMaxVisibleItems(12)
        self.main_cb_3.setObjectName("main_cb_3")
        self.main_cb_3.addItem("")
        self.gridLayout.addWidget(self.main_cb_3, 2, 1, 1, 1)
        self.main_lb_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_lb_4.sizePolicy().hasHeightForWidth())
        self.main_lb_4.setSizePolicy(sizePolicy)
        self.main_lb_4.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_4.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_4.setFont(font)
        self.main_lb_4.setObjectName("main_lb_4")
        self.gridLayout.addWidget(self.main_lb_4, 3, 0, 1, 1)
        self.main_cb_4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.main_cb_4.setEnabled(False)
        self.main_cb_4.setMinimumSize(QtCore.QSize(180, 27))
        self.main_cb_4.setMaximumSize(QtCore.QSize(180, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_cb_4.setFont(font)
        self.main_cb_4.setStyleSheet("QComboBox {\n"
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
        self.main_cb_4.setMaxVisibleItems(12)
        self.main_cb_4.setObjectName("main_cb_4")
        self.main_cb_4.addItem("")
        self.gridLayout.addWidget(self.main_cb_4, 3, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout.addItem(spacerItem2)
        self.forward_im = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.forward_im.setMinimumSize(QtCore.QSize(25, 25))
        self.forward_im.setMaximumSize(QtCore.QSize(25, 25))
        self.forward_im.setLineWidth(0)
        self.forward_im.setText("")
        self.forward_im.setPixmap(QtGui.QPixmap("icons/fwdarrow_icon.svg"))
        self.forward_im.setScaledContents(True)
        self.forward_im.setAlignment(QtCore.Qt.AlignCenter)
        self.forward_im.setObjectName("forward_im")
        self.verticalLayout.addWidget(self.forward_im)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.main_lb_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_lb_5.sizePolicy().hasHeightForWidth())
        self.main_lb_5.setSizePolicy(sizePolicy)
        self.main_lb_5.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_5.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_5.setFont(font)
        self.main_lb_5.setObjectName("main_lb_5")
        self.horizontalLayout_5.addWidget(self.main_lb_5)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.main_cb_5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.main_cb_5.setEnabled(False)
        self.main_cb_5.setMinimumSize(QtCore.QSize(430, 27))
        self.main_cb_5.setMaximumSize(QtCore.QSize(430, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_cb_5.setFont(font)
        self.main_cb_5.setStyleSheet("QComboBox {\n"
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
        self.main_cb_5.setMaxVisibleItems(12)
        self.main_cb_5.setObjectName("main_cb_5")
        self.main_cb_5.addItem("")
        self.verticalLayout_2.addWidget(self.main_cb_5)
        spacerItem8 = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.info_bt_1 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.info_bt_1.setMaximumSize(QtCore.QSize(27, 27))
        self.info_bt_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_bt_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info_bt_1.setIcon(icon1)
        self.info_bt_1.setIconSize(QtCore.QSize(23, 23))
        self.info_bt_1.setAutoRaise(False)
        self.info_bt_1.setObjectName("info_bt_1")
        self.horizontalLayout_2.addWidget(self.info_bt_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem10)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.main_lb_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_lb_6.sizePolicy().hasHeightForWidth())
        self.main_lb_6.setSizePolicy(sizePolicy)
        self.main_lb_6.setMinimumSize(QtCore.QSize(120, 27))
        self.main_lb_6.setMaximumSize(QtCore.QSize(120, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_6.setFont(font)
        self.main_lb_6.setStyleSheet("")
        self.main_lb_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.main_lb_6.setObjectName("main_lb_6")
        self.verticalLayout_4.addWidget(self.main_lb_6)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem12)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.main_lb_7 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_lb_7.sizePolicy().hasHeightForWidth())
        self.main_lb_7.setSizePolicy(sizePolicy)
        self.main_lb_7.setMinimumSize(QtCore.QSize(0, 0))
        self.main_lb_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_7.setFont(font)
        self.main_lb_7.setStyleSheet("QTextBrowser {\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.main_lb_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_lb_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.main_lb_7.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.main_lb_7.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.main_lb_7.setObjectName("main_lb_7")
        self.horizontalLayout_4.addWidget(self.main_lb_7)
        spacerItem13 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.product_info_button = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.product_info_button.setMaximumSize(QtCore.QSize(27, 27))
        self.product_info_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.product_info_button.setText("")
        self.product_info_button.setIcon(icon1)
        self.product_info_button.setIconSize(QtCore.QSize(23, 23))
        self.product_info_button.setAutoRaise(False)
        self.product_info_button.setObjectName("product_info_button")
        self.verticalLayout_7.addWidget(self.product_info_button)
        spacerItem14 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem14)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 1, 1, 2, 1)
        spacerItem15 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem15, 1, 2, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem16, 2, 0, 1, 1)
        self.information_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_26.addWidget(self.information_scroll_area, 0, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_26.addItem(spacerItem17, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.tabWidgetPage2)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.variables_scroll_area = QtWidgets.QScrollArea(self.tabWidgetPage2)
        self.variables_scroll_area.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"  border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"  border-top-right-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"  border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.variables_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.variables_scroll_area.setWidgetResizable(True)
        self.variables_scroll_area.setObjectName("variables_scroll_area")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 1000, 497))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem18 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem18, 0, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem19, 1, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.main_lb_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_lb_8.sizePolicy().hasHeightForWidth())
        self.main_lb_8.setSizePolicy(sizePolicy)
        self.main_lb_8.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_8.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_8.setFont(font)
        self.main_lb_8.setStyleSheet("")
        self.main_lb_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.main_lb_8.setObjectName("main_lb_8")
        self.horizontalLayout_3.addWidget(self.main_lb_8)
        spacerItem20 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem20)
        self.info_bt_2 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_6)
        self.info_bt_2.setMaximumSize(QtCore.QSize(27, 27))
        self.info_bt_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_bt_2.setText("")
        self.info_bt_2.setIcon(icon1)
        self.info_bt_2.setIconSize(QtCore.QSize(23, 23))
        self.info_bt_2.setAutoRaise(False)
        self.info_bt_2.setObjectName("info_bt_2")
        self.horizontalLayout_3.addWidget(self.info_bt_2)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem21)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem22 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem22)
        self.main_cb_6 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_6)
        self.main_cb_6.setEnabled(False)
        self.main_cb_6.setMinimumSize(QtCore.QSize(430, 27))
        self.main_cb_6.setMaximumSize(QtCore.QSize(430, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_cb_6.setFont(font)
        self.main_cb_6.setStyleSheet("QComboBox {\n"
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
        self.main_cb_6.setMaxVisibleItems(12)
        self.main_cb_6.setObjectName("main_cb_6")
        self.main_cb_6.addItem("")
        self.horizontalLayout_6.addWidget(self.main_cb_6)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem23)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        spacerItem24 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem24)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.main_lb_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_lb_10.sizePolicy().hasHeightForWidth())
        self.main_lb_10.setSizePolicy(sizePolicy)
        self.main_lb_10.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_10.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_10.setFont(font)
        self.main_lb_10.setStyleSheet("")
        self.main_lb_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.main_lb_10.setObjectName("main_lb_10")
        self.horizontalLayout_7.addWidget(self.main_lb_10)
        spacerItem25 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem25)
        self.info_bt_3 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_6)
        self.info_bt_3.setMaximumSize(QtCore.QSize(27, 27))
        self.info_bt_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_bt_3.setText("")
        self.info_bt_3.setIcon(icon1)
        self.info_bt_3.setIconSize(QtCore.QSize(23, 23))
        self.info_bt_3.setAutoRaise(False)
        self.info_bt_3.setObjectName("info_bt_3")
        self.horizontalLayout_7.addWidget(self.info_bt_3)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem26)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem27 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem27)
        self.variables_vertical_layout = QtWidgets.QVBoxLayout()
        self.variables_vertical_layout.setObjectName("variables_vertical_layout")
        self.horizontalLayout_8.addLayout(self.variables_vertical_layout)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem28)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.gridLayout_5.addLayout(self.verticalLayout_5, 1, 1, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(440, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem29, 1, 2, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(20, 157, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem30, 2, 1, 1, 1)
        self.variables_scroll_area.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_18.addWidget(self.variables_scroll_area, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QtWidgets.QWidget()
        self.tabWidgetPage3.setObjectName("tabWidgetPage3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabWidgetPage3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.spacetime_scroll_area = QtWidgets.QScrollArea(self.tabWidgetPage3)
        self.spacetime_scroll_area.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"  border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"  border-top-right-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"  border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.spacetime_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.spacetime_scroll_area.setWidgetResizable(True)
        self.spacetime_scroll_area.setObjectName("spacetime_scroll_area")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 980, 390))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem31 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem31, 0, 1, 1, 1)
        spacerItem32 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem32, 1, 0, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.main_lb_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_lb_11.sizePolicy().hasHeightForWidth())
        self.main_lb_11.setSizePolicy(sizePolicy)
        self.main_lb_11.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_11.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_11.setFont(font)
        self.main_lb_11.setStyleSheet("")
        self.main_lb_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.main_lb_11.setObjectName("main_lb_11")
        self.horizontalLayout_11.addWidget(self.main_lb_11)
        spacerItem33 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem33)
        self.info_bt_4 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.info_bt_4.setMaximumSize(QtCore.QSize(27, 27))
        self.info_bt_4.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_bt_4.setText("")
        self.info_bt_4.setIcon(icon1)
        self.info_bt_4.setIconSize(QtCore.QSize(23, 23))
        self.info_bt_4.setAutoRaise(False)
        self.info_bt_4.setObjectName("info_bt_4")
        self.horizontalLayout_11.addWidget(self.info_bt_4)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem34)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem35 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem35)
        self.main_lb_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.main_lb_13.setEnabled(True)
        self.main_lb_13.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_13.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_13.setFont(font)
        self.main_lb_13.setObjectName("main_lb_13")
        self.horizontalLayout_12.addWidget(self.main_lb_13)
        self.main_de_1 = QtWidgets.QDateEdit(self.scrollAreaWidgetContents_3)
        self.main_de_1.setEnabled(False)
        self.main_de_1.setMinimumSize(QtCore.QSize(130, 27))
        self.main_de_1.setMaximumSize(QtCore.QSize(130, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_de_1.setFont(font)
        self.main_de_1.setStyleSheet("QDateEdit {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"}\n"
"\n"
"QDateEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}\n"
"\n"
"QDateEdit:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
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
"QDateEdit::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}")
        self.main_de_1.setFrame(False)
        self.main_de_1.setAlignment(QtCore.Qt.AlignCenter)
        self.main_de_1.setAccelerated(True)
        self.main_de_1.setDateTime(QtCore.QDateTime(QtCore.QDate(1979, 1, 1), QtCore.QTime(23, 0, 0)))
        self.main_de_1.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.main_de_1.setCalendarPopup(True)
        self.main_de_1.setTimeSpec(QtCore.Qt.UTC)
        self.main_de_1.setDate(QtCore.QDate(1979, 1, 1))
        self.main_de_1.setObjectName("main_de_1")
        self.horizontalLayout_12.addWidget(self.main_de_1)
        self.main_lb_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.main_lb_14.setEnabled(True)
        self.main_lb_14.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_14.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_14.setFont(font)
        self.main_lb_14.setObjectName("main_lb_14")
        self.horizontalLayout_12.addWidget(self.main_lb_14)
        self.main_de_2 = QtWidgets.QDateEdit(self.scrollAreaWidgetContents_3)
        self.main_de_2.setEnabled(False)
        self.main_de_2.setMinimumSize(QtCore.QSize(130, 27))
        self.main_de_2.setMaximumSize(QtCore.QSize(130, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_de_2.setFont(font)
        self.main_de_2.setStyleSheet("QDateEdit {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"}\n"
"\n"
"QDateEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}\n"
"\n"
"QDateEdit:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
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
"QDateEdit::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}")
        self.main_de_2.setFrame(False)
        self.main_de_2.setAlignment(QtCore.Qt.AlignCenter)
        self.main_de_2.setAccelerated(True)
        self.main_de_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(23, 0, 0)))
        self.main_de_2.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.main_de_2.setCalendarPopup(True)
        self.main_de_2.setTimeSpec(QtCore.Qt.UTC)
        self.main_de_2.setDate(QtCore.QDate(2018, 1, 1))
        self.main_de_2.setObjectName("main_de_2")
        self.horizontalLayout_12.addWidget(self.main_de_2)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem36)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        spacerItem37 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem37)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.main_lb_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_lb_12.sizePolicy().hasHeightForWidth())
        self.main_lb_12.setSizePolicy(sizePolicy)
        self.main_lb_12.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_12.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_12.setFont(font)
        self.main_lb_12.setStyleSheet("")
        self.main_lb_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.main_lb_12.setObjectName("main_lb_12")
        self.horizontalLayout_13.addWidget(self.main_lb_12)
        spacerItem38 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem38)
        self.info_bt_5 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.info_bt_5.setMaximumSize(QtCore.QSize(27, 27))
        self.info_bt_5.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_bt_5.setText("")
        self.info_bt_5.setIcon(icon1)
        self.info_bt_5.setIconSize(QtCore.QSize(23, 23))
        self.info_bt_5.setAutoRaise(False)
        self.info_bt_5.setObjectName("info_bt_5")
        self.horizontalLayout_13.addWidget(self.info_bt_5)
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem39)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem40 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem40)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.main_lb_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.main_lb_15.setEnabled(True)
        self.main_lb_15.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_15.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_15.setFont(font)
        self.main_lb_15.setObjectName("main_lb_15")
        self.gridLayout_2.addWidget(self.main_lb_15, 0, 0, 1, 1)
        self.main_cb_7 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.main_cb_7.setEnabled(False)
        self.main_cb_7.setMinimumSize(QtCore.QSize(160, 27))
        self.main_cb_7.setMaximumSize(QtCore.QSize(160, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_cb_7.setFont(font)
        self.main_cb_7.setStyleSheet("QComboBox {\n"
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
        self.main_cb_7.setMaxVisibleItems(12)
        self.main_cb_7.setObjectName("main_cb_7")
        self.main_cb_7.addItem("")
        self.gridLayout_2.addWidget(self.main_cb_7, 0, 1, 1, 1)
        self.main_lb_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.main_lb_17.setEnabled(True)
        self.main_lb_17.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_17.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_17.setFont(font)
        self.main_lb_17.setObjectName("main_lb_17")
        self.gridLayout_2.addWidget(self.main_lb_17, 1, 0, 1, 1)
        self.main_cb_8 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.main_cb_8.setEnabled(False)
        self.main_cb_8.setMinimumSize(QtCore.QSize(160, 27))
        self.main_cb_8.setMaximumSize(QtCore.QSize(160, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_cb_8.setFont(font)
        self.main_cb_8.setStyleSheet("QComboBox {\n"
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
        self.main_cb_8.setMaxVisibleItems(12)
        self.main_cb_8.setObjectName("main_cb_8")
        self.main_cb_8.addItem("")
        self.gridLayout_2.addWidget(self.main_cb_8, 1, 1, 1, 1)
        self.horizontalLayout_14.addLayout(self.gridLayout_2)
        spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem41)
        self.verticalLayout_6.addLayout(self.horizontalLayout_14)
        spacerItem42 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem42)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.main_lb_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_lb_16.sizePolicy().hasHeightForWidth())
        self.main_lb_16.setSizePolicy(sizePolicy)
        self.main_lb_16.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_16.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_16.setFont(font)
        self.main_lb_16.setStyleSheet("")
        self.main_lb_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.main_lb_16.setObjectName("main_lb_16")
        self.horizontalLayout_17.addWidget(self.main_lb_16)
        spacerItem43 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem43)
        self.info_bt_7 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.info_bt_7.setMaximumSize(QtCore.QSize(27, 27))
        self.info_bt_7.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_bt_7.setText("")
        self.info_bt_7.setIcon(icon1)
        self.info_bt_7.setIconSize(QtCore.QSize(23, 23))
        self.info_bt_7.setAutoRaise(False)
        self.info_bt_7.setObjectName("info_bt_7")
        self.horizontalLayout_17.addWidget(self.info_bt_7)
        spacerItem44 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem44)
        self.verticalLayout_6.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem45 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem45)
        self.main_ln_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.main_ln_1.setEnabled(True)
        self.main_ln_1.setMinimumSize(QtCore.QSize(0, 27))
        self.main_ln_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_ln_1.setFont(font)
        self.main_ln_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.main_ln_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200, 200, 200);\n"
"}")
        self.main_ln_1.setFrame(False)
        self.main_ln_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.main_ln_1.setObjectName("main_ln_1")
        self.horizontalLayout_18.addWidget(self.main_ln_1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_18)
        spacerItem46 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem46)
        self.horizontalLayout_16.addLayout(self.verticalLayout_6)
        spacerItem47 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem47)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_16.addWidget(self.line_2)
        spacerItem48 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem48)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem49 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem49)
        self.main_lb_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_lb_9.sizePolicy().hasHeightForWidth())
        self.main_lb_9.setSizePolicy(sizePolicy)
        self.main_lb_9.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_9.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_9.setFont(font)
        self.main_lb_9.setStyleSheet("")
        self.main_lb_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.main_lb_9.setObjectName("main_lb_9")
        self.horizontalLayout_15.addWidget(self.main_lb_9)
        spacerItem50 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem50)
        self.info_bt_6 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.info_bt_6.setMaximumSize(QtCore.QSize(27, 27))
        self.info_bt_6.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_bt_6.setText("")
        self.info_bt_6.setIcon(icon1)
        self.info_bt_6.setIconSize(QtCore.QSize(23, 23))
        self.info_bt_6.setAutoRaise(False)
        self.info_bt_6.setObjectName("info_bt_6")
        self.horizontalLayout_15.addWidget(self.info_bt_6)
        spacerItem51 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem51)
        self.verticalLayout_9.addLayout(self.horizontalLayout_15)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem52 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem52)
        self.space_ln_north = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.space_ln_north.setEnabled(False)
        self.space_ln_north.setMinimumSize(QtCore.QSize(60, 27))
        self.space_ln_north.setMaximumSize(QtCore.QSize(60, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.space_ln_north.setFont(font)
        self.space_ln_north.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.space_ln_north.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200, 200, 200);\n"
"}")
        self.space_ln_north.setFrame(False)
        self.space_ln_north.setAlignment(QtCore.Qt.AlignCenter)
        self.space_ln_north.setObjectName("space_ln_north")
        self.horizontalLayout_9.addWidget(self.space_ln_north)
        spacerItem53 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem53)
        self.gridLayout_8.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem54 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem54)
        self.space_ln_west = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.space_ln_west.setEnabled(False)
        self.space_ln_west.setMinimumSize(QtCore.QSize(60, 27))
        self.space_ln_west.setMaximumSize(QtCore.QSize(60, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.space_ln_west.setFont(font)
        self.space_ln_west.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200, 200, 200);\n"
"}")
        self.space_ln_west.setFrame(False)
        self.space_ln_west.setAlignment(QtCore.Qt.AlignCenter)
        self.space_ln_west.setObjectName("space_ln_west")
        self.verticalLayout_8.addWidget(self.space_ln_west)
        spacerItem55 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem55)
        self.gridLayout_8.addLayout(self.verticalLayout_8, 1, 0, 1, 1)
        self.earth_im = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.earth_im.setEnabled(False)
        self.earth_im.setMinimumSize(QtCore.QSize(230, 230))
        self.earth_im.setMaximumSize(QtCore.QSize(230, 230))
        self.earth_im.setText("")
        self.earth_im.setPixmap(QtGui.QPixmap("icons/EMC_globe_terrestre.png"))
        self.earth_im.setScaledContents(True)
        self.earth_im.setAlignment(QtCore.Qt.AlignCenter)
        self.earth_im.setObjectName("earth_im")
        self.gridLayout_8.addWidget(self.earth_im, 1, 1, 1, 1)
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        spacerItem56 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_28.addItem(spacerItem56)
        self.space_ln_east = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.space_ln_east.setEnabled(False)
        self.space_ln_east.setMinimumSize(QtCore.QSize(60, 27))
        self.space_ln_east.setMaximumSize(QtCore.QSize(60, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.space_ln_east.setFont(font)
        self.space_ln_east.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200, 200, 200);\n"
"}")
        self.space_ln_east.setFrame(False)
        self.space_ln_east.setAlignment(QtCore.Qt.AlignCenter)
        self.space_ln_east.setObjectName("space_ln_east")
        self.verticalLayout_28.addWidget(self.space_ln_east)
        spacerItem57 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_28.addItem(spacerItem57)
        self.gridLayout_8.addLayout(self.verticalLayout_28, 1, 2, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem58 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem58)
        self.space_ln_south = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.space_ln_south.setEnabled(False)
        self.space_ln_south.setMinimumSize(QtCore.QSize(60, 27))
        self.space_ln_south.setMaximumSize(QtCore.QSize(60, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.space_ln_south.setFont(font)
        self.space_ln_south.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200, 200, 200);\n"
"}")
        self.space_ln_south.setFrame(False)
        self.space_ln_south.setAlignment(QtCore.Qt.AlignCenter)
        self.space_ln_south.setObjectName("space_ln_south")
        self.horizontalLayout_10.addWidget(self.space_ln_south)
        spacerItem59 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem59)
        self.gridLayout_8.addLayout(self.horizontalLayout_10, 2, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_8)
        self.horizontalLayout_16.addLayout(self.verticalLayout_9)
        spacerItem60 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem60)
        self.gridLayout_6.addLayout(self.horizontalLayout_16, 1, 1, 2, 2)
        spacerItem61 = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem61, 2, 3, 1, 1)
        spacerItem62 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem62, 3, 2, 1, 1)
        self.spacetime_scroll_area.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.addWidget(self.spacetime_scroll_area, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage3, "")
        self.gridLayout_7.addWidget(self.tabWidget, 0, 0, 1, 1)
        spacerItem63 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem63, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem64 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem64)
        self.productdownload = QtWidgets.QToolButton(self.centralwidget)
        self.productdownload.setEnabled(True)
        self.productdownload.setMinimumSize(QtCore.QSize(150, 35))
        self.productdownload.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.productdownload.setFont(font)
        self.productdownload.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
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
        self.productdownload.setObjectName("productdownload")
        self.horizontalLayout.addWidget(self.productdownload)
        spacerItem65 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem65)
        self.getSize = QtWidgets.QToolButton(self.centralwidget)
        self.getSize.setEnabled(True)
        self.getSize.setMinimumSize(QtCore.QSize(150, 35))
        self.getSize.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.getSize.setFont(font)
        self.getSize.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
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
        self.getSize.setObjectName("getSize")
        self.horizontalLayout.addWidget(self.getSize)
        spacerItem66 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem66)
        self.gridLayout_7.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(35, 35))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/save_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionSave.setFont(font)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/open_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionOpen.setFont(font)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/exit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/about_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionAbout.setFont(font)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSeparator1 = QtWidgets.QAction(MainWindow)
        self.actionSeparator1.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/separator_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSeparator1.setIcon(icon6)
        self.actionSeparator1.setObjectName("actionSeparator1")
        self.actionSeparator2 = QtWidgets.QAction(MainWindow)
        self.actionSeparator2.setEnabled(False)
        self.actionSeparator2.setIcon(icon6)
        self.actionSeparator2.setObjectName("actionSeparator2")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setEnabled(False)
        self.actionUpdate.setIcon(icon)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionOptions = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/option_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOptions.setIcon(icon7)
        self.actionOptions.setObjectName("actionOptions")
        self.actionExpert = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/expert_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExpert.setIcon(icon8)
        self.actionExpert.setObjectName("actionExpert")
        self.toolBar.addAction(self.actionExit)
        self.toolBar.addAction(self.actionSeparator1)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionExpert)
        self.toolBar.addAction(self.actionSeparator2)
        self.toolBar.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionOptions)
        self.toolBar.addAction(self.actionUpdate)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.main_cb_1.setCurrentIndex(0)
        self.main_cb_2.setCurrentIndex(0)
        self.main_cb_3.setCurrentIndex(0)
        self.main_cb_4.setCurrentIndex(0)
        self.main_cb_5.setCurrentIndex(0)
        self.main_cb_6.setCurrentIndex(0)
        self.main_cb_7.setCurrentIndex(0)
        self.main_cb_8.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CMEMS Data Downloader"))
        self.main_lb_1.setText(_translate("MainWindow", "1) Select a regional domain:"))
        self.main_cb_1.setItemText(0, _translate("MainWindow", "Make a choice..."))
        self.main_cb_1.setItemText(1, _translate("MainWindow", "Global"))
        self.main_cb_1.setItemText(2, _translate("MainWindow", "Arctic Ocean"))
        self.main_cb_1.setItemText(3, _translate("MainWindow", "Baltic Sea"))
        self.main_cb_1.setItemText(4, _translate("MainWindow", "Mediterranean Sea"))
        self.main_cb_1.setItemText(5, _translate("MainWindow", "Black Sea"))
        self.main_lb_2.setText(_translate("MainWindow", "2) Select the data type:"))
        self.main_cb_2.setItemText(0, _translate("MainWindow", "No type available..."))
        self.main_lb_3.setText(_translate("MainWindow", "3) Select the data source:"))
        self.main_cb_3.setItemText(0, _translate("MainWindow", "No source available..."))
        self.main_lb_4.setText(_translate("MainWindow", "4) Select the delivery mode:"))
        self.main_cb_4.setItemText(0, _translate("MainWindow", "No mode available..."))
        self.main_lb_5.setText(_translate("MainWindow", "<html><head/><body><p>5) Select now a <span style=\" font-weight:600;\">product</span>:</p></body></html>"))
        self.main_cb_5.setItemText(0, _translate("MainWindow", "No product available..."))
        self.main_lb_6.setText(_translate("MainWindow", "Information:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("MainWindow", "Product / Information"))
        self.main_lb_8.setText(_translate("MainWindow", "Datasets:"))
        self.main_cb_6.setItemText(0, _translate("MainWindow", "No product selected..."))
        self.main_lb_10.setText(_translate("MainWindow", "Variables:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("MainWindow", "Datasets / Variables"))
        self.main_lb_11.setText(_translate("MainWindow", "Temporal coverage:"))
        self.main_lb_13.setText(_translate("MainWindow", "from"))
        self.main_de_1.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.main_lb_14.setText(_translate("MainWindow", "to"))
        self.main_de_2.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.main_lb_12.setText(_translate("MainWindow", "Depth:"))
        self.main_lb_15.setText(_translate("MainWindow", "start depth:"))
        self.main_cb_7.setItemText(0, _translate("MainWindow", "No depth..."))
        self.main_lb_17.setText(_translate("MainWindow", "end depth:"))
        self.main_cb_8.setItemText(0, _translate("MainWindow", "No depth..."))
        self.main_lb_16.setText(_translate("MainWindow", "File name:"))
        self.main_lb_9.setText(_translate("MainWindow", "Regional coverage:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), _translate("MainWindow", "Time / Space and File"))
        self.productdownload.setText(_translate("MainWindow", "Download"))
        self.getSize.setText(_translate("MainWindow", "Check size"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSave.setText(_translate("MainWindow", "Save..."))
        self.actionSave.setToolTip(_translate("MainWindow", "Save job in an XML file"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open an XML file containing a job"))
        self.actionExit.setText(_translate("MainWindow", "Exit..."))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit CMEMS Data Downloader"))
        self.actionAbout.setText(_translate("MainWindow", "CMEMS Data Downloader..."))
        self.actionAbout.setToolTip(_translate("MainWindow", "About CMEMS Data Downloader"))
        self.actionSeparator1.setText(_translate("MainWindow", "separator1"))
        self.actionSeparator2.setText(_translate("MainWindow", "separator2"))
        self.actionSeparator2.setToolTip(_translate("MainWindow", "separator2"))
        self.actionUpdate.setText(_translate("MainWindow", "Update..."))
        self.actionUpdate.setToolTip(_translate("MainWindow", "No update available !"))
        self.actionOptions.setText(_translate("MainWindow", "Options..."))
        self.actionOptions.setToolTip(_translate("MainWindow", "Click to modify CMEMS Data Downloader options"))
        self.actionExpert.setText(_translate("MainWindow", "Expert..."))
        self.actionExpert.setToolTip(_translate("MainWindow", "Open the window for raw inputs"))

