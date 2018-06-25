import logging
from PyQt5 import QtWidgets, QtGui, QtCore
from functions.window_functions import MyInfo


def info_button(self):
    logging.debug('gui_functions.py - info_button - self.sender().objectName() ' + self.sender().objectName())
    if 'infoButton' in self.sender().objectName():
        x = QtGui.QCursor.pos().x()
        y = QtGui.QCursor.pos().y()
        x = x - 225
        y = y + 50
        self.infoWindow = MyInfo(self.info_button_text_dict[self.sender().objectName()])
        self.infoWindow.setMinimumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
        self.infoWindow.setMaximumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
        self.infoWindow.setGeometry(x, y, 450, self.infoWindow.sizeHint().height())
        self.infoWindow.exec_()


def activate_type_cb(self):
    deactivate_type_cb(self)
    deactivate_source_cb(self)
    deactivate_delivery_cb(self)
    deactivate_product_cb(self)
    deactivate_information_lab(self)
    try:
        types = self.dataset_database[self.main_cb_1.currentText()]
        cb_list = []
        for key, _ in types.items():
            cb_list.append(key)
        self.main_cb_2.setEnabled(True)
        self.main_cb_2.clear()
        self.main_cb_2.addItem('Make a choice...')
        self.main_cb_2.addItems(sorted(cb_list))
        self.main_cb_2.currentIndexChanged.connect(lambda: activate_source_cb(self))
    except KeyError:
        pass


def activate_source_cb(self):
    deactivate_source_cb(self)
    deactivate_delivery_cb(self)
    deactivate_product_cb(self)
    deactivate_information_lab(self)
    try:
        sources = self.dataset_database[self.main_cb_1.currentText()][self.main_cb_2.currentText()]
        cb_list = []
        for key, _ in sources.items():
            cb_list.append(key)
        self.main_cb_3.setEnabled(True)
        self.main_cb_3.clear()
        self.main_cb_3.addItem('Make a choice...')
        self.main_cb_3.addItems(sorted(cb_list))
        self.main_cb_3.currentIndexChanged.connect(lambda: activate_delivery_cb(self))
    except KeyError:
        pass


def activate_delivery_cb(self):
    deactivate_delivery_cb(self)
    deactivate_product_cb(self)
    deactivate_information_lab(self)
    try:
        deliveries = self.dataset_database[self.main_cb_1.currentText()][self.main_cb_2.currentText()][self.main_cb_3.currentText()]
        cb_list = []
        for key, _ in deliveries.items():
            cb_list.append(key)
        self.main_cb_4.setEnabled(True)
        self.main_cb_4.clear()
        self.main_cb_4.addItem('Make a choice...')
        self.main_cb_4.addItems(sorted(cb_list))
        self.main_cb_4.currentIndexChanged.connect(lambda: activate_product_cb(self))
    except KeyError:
        pass


def activate_product_cb(self):
    deactivate_product_cb(self)
    deactivate_information_lab(self)
    try:
        products = self.dataset_database[self.main_cb_1.currentText()][self.main_cb_2.currentText()][self.main_cb_3.currentText()][self.main_cb_4.currentText()]
        self.main_cb_5.setEnabled(True)
        self.main_cb_5.clear()
        self.main_cb_5.addItem('Make a choice...')
        self.main_cb_5.addItems(sorted(products))
        self.main_cb_5.currentIndexChanged.connect(lambda: activate_information_tab(self))
    except KeyError:
        pass


def activate_information_tab(self):
    deactivate_information_lab(self)
    try:
        product = self.product_database[self.main_cb_5.currentText()]
        information_text = ('<p align="justify">Please click on the information button on the right to access more detailed information about the product.</p>'
                            + '<p align="justify">' + product['information']['short_description'] + '</p>')
        self.main_lb_7.setText(information_text)
        self.tabWidget.setEnabled(True)
        self.information_scroll_area.setVisible(True)
    except KeyError:
        pass


def deactivate_type_cb(self):
    try:
        self.main_cb_2.currentIndexChanged.disconnect(lambda: activate_source_cb(self))
    except TypeError:
        pass
    self.main_cb_2.setCurrentIndex(0)
    self.main_cb_2.setEnabled(False)


def deactivate_source_cb(self):
    try:
        self.main_cb_3.currentIndexChanged.disconnect(lambda: activate_delivery_cb(self))
    except TypeError:
        pass
    self.main_cb_3.setCurrentIndex(0)
    self.main_cb_3.setEnabled(False)


def deactivate_delivery_cb(self):
    try:
        self.main_cb_4.currentIndexChanged.disconnect(lambda: activate_product_cb(self))
    except TypeError:
        pass
    self.main_cb_4.setCurrentIndex(0)
    self.main_cb_4.setEnabled(False)


def deactivate_product_cb(self):
    try:
        self.main_cb_5.currentIndexChanged.disconnect(lambda: activate_information_tab(self))
    except TypeError:
        pass
    self.main_cb_5.setCurrentIndex(0)
    self.main_cb_5.setEnabled(False)


def deactivate_information_lab(self):
    self.main_lb_7.setText('')
