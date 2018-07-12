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
    logging.debug('gui_functions.py - activate_type_cb')
    deactivate_type_cb(self)
    deactivate_source_cb(self)
    deactivate_delivery_cb(self)
    deactivate_product_cb(self)
    deactivate_dataset_information(self)
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
    logging.debug('gui_functions.py - activate_source_cb')
    deactivate_source_cb(self)
    deactivate_delivery_cb(self)
    deactivate_product_cb(self)
    deactivate_dataset_information(self)
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
    logging.debug('gui_functions.py - activate_delivery_cb')
    deactivate_delivery_cb(self)
    deactivate_product_cb(self)
    deactivate_dataset_information(self)
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
    logging.debug('gui_functions.py - activate_product_cb')
    deactivate_product_cb(self)
    deactivate_dataset_information(self)
    try:
        products = self.dataset_database[self.main_cb_1.currentText()][self.main_cb_2.currentText()][self.main_cb_3.currentText()][self.main_cb_4.currentText()]
        self.main_cb_5.setEnabled(True)
        self.main_cb_5.clear()
        self.main_cb_5.addItem('Make a choice...')
        self.main_cb_5.addItems(sorted(products))
        self.main_cb_5.currentIndexChanged.connect(lambda: activate_dataset_information(self))
    except KeyError:
        pass


def activate_dataset_information(self):
    logging.debug('gui_functions.py - activate_dataset_information')
    deactivate_dataset_information(self)
    self.variables_cb.clear()
    if self.main_cb_5.currentText() != 'Make a choice...':
        self.set_modified()
        product = self.product_database[self.main_cb_5.currentText()]
        information_text = ('<p align="justify">Please click on the information button on the right to access more detailed information about the product.</p>'
                            + '<p align="justify">' + product['information']['short_description'] + '</p>')
        self.main_lb_7.setText(information_text)
        swath, period = product['swath'], product['information']['temporal_coverage']
        start, end = period[5:15], period[29:39]
        self.main_de_1.setEnabled(True)
        self.main_de_2.setEnabled(True)
        self.main_de_1.setDate(QtCore.QDate.fromString(start, QtCore.Qt.ISODate))
        self.main_de_1.setMinimumDate(QtCore.QDate.fromString(start, QtCore.Qt.ISODate))
        self.main_de_1.setMaximumDate(QtCore.QDate.fromString(end, QtCore.Qt.ISODate))
        self.main_de_2.setDate(QtCore.QDate.fromString(end, QtCore.Qt.ISODate))
        self.main_de_2.setMinimumDate(QtCore.QDate.fromString(start, QtCore.Qt.ISODate))
        self.main_de_2.setMaximumDate(QtCore.QDate.fromString(end, QtCore.Qt.ISODate))
        self.main_cb_6.clear()
        self.main_cb_6.setEnabled(True)
        if isinstance(swath, list):
            self.main_cb_6.addItem('Make a choice...')
            self.main_cb_6.addItems(swath)
            clear_layout(self.variables_vertical_layout)
            self.main_cb_6.currentIndexChanged.connect(lambda: populate_variable_list(self, product['variables']))
            self.main_cb_6.currentIndexChanged.connect(lambda: activate_depth_cb(self, product['information']['vertical_coverage']))
            self.main_cb_6.currentIndexChanged.connect(lambda: activate_area_ln(self, product['subset']))
            self.main_cb_6.currentIndexChanged.connect(lambda: specific_period(self, self.main_cb_6.currentIndex(), product['swath_temporal']))
        else:
            self.main_cb_6.addItem(swath)
            populate_variable_list(self, product['variables'])
            activate_depth_cb(self, product['information']['vertical_coverage'])
            activate_area_ln(self, product['subset'])


def populate_variable_list(self, variables):
    logging.debug('gui_functions.py - populate_variable_list')
    clean_stylesheet_dataset(self)
    clean_stylesheet_variable(self)
    clear_layout(self.variables_vertical_layout)
    if self.main_cb_6.currentText() != 'Make a choice...':
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        if variables is not None:
            if isinstance(variables, list):
                if isinstance(variables[0], list):
                    index = self.main_cb_6.currentIndex() - 1
                    variables = variables[index]
            else:
                variables = [variables]
            self.variables_cb.clear()
            var_num = 0
            for var in variables:
                self.variables_cb.append(QtWidgets.QCheckBox())
                self.variables_cb[var_num].setMinimumSize(QtCore.QSize(0, 27))
                self.variables_cb[var_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.variables_cb[var_num].setFont(font)
                self.variables_cb[var_num].setObjectName('variables_cb_' + str(var_num))
                self.variables_cb[var_num].setText(self.variables_name[var])
                self.variables_cb[var_num].toggled.connect(lambda: clean_stylesheet_variable(self))
                self.variables_vertical_layout.addWidget(self.variables_cb[var_num])
                var_num += 1
        else:
            label = QtWidgets.QLabel()
            label.setMinimumSize(QtCore.QSize(0, 27))
            label.setMaximumSize(QtCore.QSize(16777215, 27))
            label.setFont(font)
            label.setObjectName('label')
            label.setText('Only one variable is available with the current dataset. It has been automatically selected.')
            self.variables_vertical_layout.addWidget(label)


def activate_depth_cb(self, depth):
    logging.debug('gui_functions.py - activate_depth_cb')
    if self.main_cb_6.currentText() != 'Make a choice...' and self.main_cb_6.currentText() != 'No product selected...':
        if depth == 'surface':
            self.main_cb_7.clear()
            self.main_cb_7.addItem('surface')
        else:
            self.main_cb_7.setEnabled(True)
            self.main_cb_7.clear()
            self.main_cb_7.addItem('Make a choice...')


def activate_area_ln(self, subset):
    logging.debug('gui_functions.py - activate_area_ln')
    if subset == 'geographical':
        self.space_ln_north.setEnabled(True)
        self.space_ln_south.setEnabled(True)
        self.space_ln_east.setEnabled(True)
        self.space_ln_west.setEnabled(True)
        self.earth_im.setEnabled(True)


def specific_period(self, i, swath_temporal):
    logging.debug('gui_functions.py - specific_period')
    if i > 0:
        i -= 1
        index = swath_temporal[i].find('to')
        start = swath_temporal[i][:index]
        end = swath_temporal[i][index+2:]
        self.main_de_1.setDate(QtCore.QDate.fromString(start, QtCore.Qt.ISODate))
        self.main_de_1.setMinimumDate(QtCore.QDate.fromString(start, QtCore.Qt.ISODate))
        self.main_de_1.setMaximumDate(QtCore.QDate.fromString(end, QtCore.Qt.ISODate))
        self.main_de_2.setDate(QtCore.QDate.fromString(end, QtCore.Qt.ISODate))
        self.main_de_2.setMinimumDate(QtCore.QDate.fromString(start, QtCore.Qt.ISODate))
        self.main_de_2.setMaximumDate(QtCore.QDate.fromString(end, QtCore.Qt.ISODate))

    
def deactivate_area_ln(self):
    logging.debug('gui_functions.py - deactivate_area_ln')
    self.space_ln_north.setText('')
    self.space_ln_south.setText('')
    self.space_ln_east.setText('')
    self.space_ln_west.setText('')
    self.space_ln_north.setEnabled(False)
    self.space_ln_south.setEnabled(False)
    self.space_ln_east.setEnabled(False)
    self.space_ln_west.setEnabled(False)
    self.earth_im.setEnabled(False)


def deactivate_depth_cb(self):
    logging.debug('gui_functions.py - deactivate_depth_cb')
    try:
        self.main_cb_7.currentIndexChanged.disconnect(self.set_modified)
        depth_signal = True
    except TypeError:
        depth_signal = False
    self.main_cb_7.setEnabled(False)
    self.main_cb_7.clear()
    self.main_cb_7.addItem('No depth...')
    if depth_signal:
        self.main_cb_7.currentIndexChanged.connect(self.set_modified)


def deactivate_type_cb(self):
    logging.debug('gui_functions.py - deactivate_type_cb')
    try:
        self.main_cb_2.currentIndexChanged.disconnect()
    except TypeError:
        pass
    self.main_cb_2.clear()
    self.main_cb_2.addItem('No type available...')
    self.main_cb_2.setCurrentIndex(0)
    self.main_cb_2.setEnabled(False)


def deactivate_source_cb(self):
    logging.debug('gui_functions.py - deactivate_source_cb')
    try:
        self.main_cb_3.currentIndexChanged.disconnect()
    except TypeError:
        pass
    self.main_cb_3.clear()
    self.main_cb_3.addItem('No source available...')
    self.main_cb_3.setCurrentIndex(0)
    self.main_cb_3.setEnabled(False)


def deactivate_delivery_cb(self):
    logging.debug('gui_functions.py - deactivate_delivery_cb')
    try:
        self.main_cb_4.currentIndexChanged.disconnect()
    except TypeError:
        pass
    self.main_cb_4.clear()
    self.main_cb_4.addItem('No mode available...')
    self.main_cb_4.setCurrentIndex(0)
    self.main_cb_4.setEnabled(False)


def deactivate_product_cb(self):
    logging.debug('gui_functions.py - deactivate_product_cb')
    try:
        self.main_cb_5.currentIndexChanged.disconnect()
    except TypeError:
        pass
    self.main_cb_5.clear()
    self.main_cb_5.addItem('No product available...')
    self.main_cb_5.setCurrentIndex(0)
    self.main_cb_5.setEnabled(False)


def deactivate_dataset_information(self):
    logging.debug('gui_functions.py - deactivate_dataset_information')
    self.main_lb_7.setText('')
    try:
        self.main_cb_6.currentIndexChanged.disconnect()
    except TypeError:
        pass
    self.main_cb_6.clear()
    self.main_cb_6.addItem('No product selected...')
    self.main_cb_6.setCurrentIndex(0)
    self.main_cb_6.setEnabled(False)
    self.main_de_1.setMinimumDate(QtCore.QDate.fromString('1979-01-01', QtCore.Qt.ISODate))
    self.main_de_1.setDate(QtCore.QDate.fromString('1979-01-01', QtCore.Qt.ISODate))
    self.main_de_2.setMaximumDate(QtCore.QDate.fromString('2018-01-01', QtCore.Qt.ISODate))
    self.main_de_2.setDate(QtCore.QDate.fromString('2018-01-01', QtCore.Qt.ISODate))
    self.main_de_1.setEnabled(False)
    self.main_de_2.setEnabled(False)
    clear_layout(self.variables_vertical_layout)
    deactivate_depth_cb(self)
    deactivate_area_ln(self)
    clean_stylesheet_product(self)
    clean_stylesheet_dataset(self)
    clean_stylesheet_variable(self)


def clean_stylesheet_product(self):
    logging.debug('gui_functions.py - clean_stylesheet_product')
    self.main_lb_5.setStyleSheet("color: rgb(0,0,0);")
    self.tabWidget.tabBar().setTabTextColor(0, QtGui.QColor(0,0,0))
    
    
def clean_stylesheet_dataset(self):
    logging.debug('gui_functions.py - clean_stylesheet_dataset')
    self.main_lb_8.setStyleSheet("color: rgb(0,0,0);")
    self.tabWidget.tabBar().setTabTextColor(1, QtGui.QColor(0,0,0))


def clean_stylesheet_variable(self):
    logging.debug('gui_functions.py - clean_stylesheet_variable')
    self.main_lb_10.setStyleSheet("color: rgb(0,0,0);")
    self.tabWidget.tabBar().setTabTextColor(1, QtGui.QColor(0,0,0))
    
    
def clear_layout(layout):
    logging.debug('gui_functions.py - clear_layout')
    for i in reversed(range(layout.count())):   
        item = layout.itemAt(i)
        if isinstance(item, QtWidgets.QWidgetItem):
            item.widget().deleteLater()
        elif isinstance(item, QtWidgets.QLayout):
            clear_layout(item.layout())
        layout.removeItem(item)      
    
    
    
