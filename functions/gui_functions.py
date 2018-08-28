import logging
import datetime
from PyQt5 import QtWidgets, QtGui, QtCore
from functions.window_functions import MyInfo, MyDayCalendar, MyMonthCalendar


def info_button(self):
    logging.debug('gui_functions.py - info_button - self.sender().objectName() ' + self.sender().objectName())
    if 'info_bt' in self.sender().objectName():
        self.infoWindow = MyInfo(self.info_button_text_dict[self.sender().objectName()])
        if self.sender().objectName() == 'info_bt_8':
            self.infoWindow.move(QtGui.QCursor.pos().x() - 350, QtGui.QCursor.pos().y() - 190)
            self.infoWindow.setMinimumSize(QtCore.QSize(700, 380))
            self.infoWindow.setMaximumSize(QtCore.QSize(700, 380))
        elif self.sender().objectName() == 'info_bt_1':
            self.infoWindow.move(QtGui.QCursor.pos().x() - 300, QtGui.QCursor.pos().y() + 20)
            self.infoWindow.setMinimumSize(QtCore.QSize(600, 330))
            self.infoWindow.setMaximumSize(QtCore.QSize(600, 330))
        else:
            self.infoWindow.move(QtGui.QCursor.pos().x() - 275, QtGui.QCursor.pos().y() + 20)
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
        self.main_cb_6.clear()
        self.main_cb_6.setEnabled(True)
        if isinstance(product['swath'], list):
            self.main_cb_6.addItem('Make a choice...')
            self.main_cb_6.addItems(product['swath'])
            clear_layout(self.variables_vertical_layout)
            self.main_cb_6.currentIndexChanged.connect(lambda: populate_variable_list(self, product))
            self.main_cb_6.currentIndexChanged.connect(lambda: activate_depth_cb(self, self.main_cb_6.currentIndex(), product))
            self.main_cb_6.currentIndexChanged.connect(lambda: activate_area_ln(self, product))
            self.main_cb_6.currentIndexChanged.connect(lambda: activate_date_picker(self, product))
            self.main_cb_6.currentIndexChanged.connect(lambda: activate_download_method(self, product))
            if product['swath_temporal'] is not None:
                self.main_cb_6.currentIndexChanged.connect(lambda: specific_period(self, self.main_cb_6.currentIndex(), product))
        else:
            self.main_cb_6.addItem(product['swath'])
            populate_variable_list(self, product)
            activate_depth_cb(self, self.main_cb_6.currentIndex(), product)
            activate_area_ln(self, product)
            activate_date_picker(self, product)
            activate_download_method(self, product)


def populate_variable_list(self, product):
    logging.debug('gui_functions.py - populate_variable_list')
    clean_stylesheet_dataset(self)
    clean_stylesheet_variable(self)
    clear_layout(self.variables_vertical_layout)
    if not read_other_parameters(self, product['other_parameters'], 'download_method'):
        variables = product['variables']
        if self.main_cb_6.currentText() != 'Make a choice...':
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            if len(product['suffix']) == 1 and product['suffix'][0] == 'FTP':
                label = QtWidgets.QLabel()
                label.setMinimumSize(QtCore.QSize(0, 27))
                label.setMaximumSize(QtCore.QSize(16777215, 27))
                label.setFont(font)
                label.setObjectName('label')
                label.setText('The current product/dataset is only available via FTP and can\'t be subseted.')
                self.variables_vertical_layout.addWidget(label)
            else:
                if variables is not None:
                    if isinstance(variables, list):
                        if isinstance(variables[0], list):
                            index = self.main_cb_6.currentIndex() - 1
                            variables = variables[index]
                    else:
                        variables = [variables]
                    self.variables_cb.clear()
                    var_num = 0
                    tab_index = self.tabWidget.currentIndex()
                    self.tabWidget.setCurrentIndex(1)
                    for var in variables:
                        self.variables_cb.append(QtWidgets.QCheckBox())
                        self.variables_cb[var_num].setMinimumSize(QtCore.QSize(0, 27))
                        self.variables_cb[var_num].setMaximumSize(QtCore.QSize(16777215, 27))
                        self.variables_cb[var_num].setFont(font)
                        self.variables_cb[var_num].setObjectName('variables_cb_' + str(var_num))
                        self.variables_cb[var_num].setText(self.variables_name[var] + ' (' + var + ')')
                        self.variables_cb[var_num].toggled.connect(lambda: clean_stylesheet_variable(self))
                        self.variables_vertical_layout.addWidget(self.variables_cb[var_num])
                        var_num += 1
                    self.tabWidget.setCurrentIndex(tab_index)
                else:
                    label = QtWidgets.QLabel()
                    label.setMinimumSize(QtCore.QSize(0, 27))
                    label.setMaximumSize(QtCore.QSize(16777215, 27))
                    label.setFont(font)
                    label.setObjectName('label')
                    label.setText('Only one variable is available with the current dataset. It has been automatically selected.')
                    self.variables_vertical_layout.addWidget(label)


def activate_depth_cb(self, product_index, product):
    logging.debug('gui_functions.py - activate_depth_cb')
    deactivate_depth_cb(self)
    if self.main_cb_6.currentText() != 'Make a choice...' and self.main_cb_6.currentText() != 'No product selected...':
        if not read_other_parameters(self, product['other_parameters'], 'download_method'):
            depth = product['information']['vertical_coverage']
            swath_vertical = product['swath_vertical']
            suffixes = product['suffix']
            if len(suffixes) == 1 and suffixes[0] == 'FTP':
                pass
            else:
                if 'TDS' in suffixes:
                    self.main_cb_7.setEnabled(True)
                    self.main_cb_8.setEnabled(True)
                if swath_vertical == None:
                    if depth == 'surface':
                        self.main_cb_7.clear()
                        self.main_cb_7.addItem('surface')
                        self.main_cb_8.clear()
                        self.main_cb_8.addItem('surface')
                else:
                    if len(swath_vertical) > 1:
                        start = swath_vertical[product_index - 1][0]
                        end = swath_vertical[product_index - 1][1]
                    else:
                        start = swath_vertical[0][0]
                        end = swath_vertical[0][1]
                    self.main_cb_7.clear()
                    self.main_cb_8.clear()
                    if isinstance(start, list):
                        self.main_cb_7.addItem('Make a choice...')
                        self.main_cb_8.addItem('Make a choice...')
                        self.main_cb_7.addItems(start)
                        self.main_cb_8.addItems(end)
                    else:
                        self.main_cb_7.addItem(start)
                        self.main_cb_8.addItem(end)


def activate_area_ln(self, product):
    logging.debug('gui_functions.py - activate_area_ln')
    if not read_other_parameters(self, product['other_parameters'], 'download_method'):
        suffixes = product['suffix']
        if 'TDS' in suffixes:
            self.space_ln_north.setEnabled(True)
            self.space_ln_south.setEnabled(True)
            self.space_ln_east.setEnabled(True)
            self.space_ln_west.setEnabled(True)
            self.earth_im.setEnabled(True)


def activate_date_picker(self, product):
    logging.debug('gui_functions.py - activate_date_picker')
    deactivate_date_picker(self)
    if not read_other_parameters(self, product['other_parameters'], 'download_method'):
        period = product['information']['temporal_coverage']
        resolution = product['information']['temporal_resolution']
        if 'Present' in period:
            start, end = period[5:15], period[29:]
            if '+' in end:
                end = datetime.datetime.now() + datetime.timedelta(days=int(end[end.find('+') + 2:]))
            else:
                end = datetime.datetime.now()
            end = end.strftime('%Y-%m-%d')
        else:
            start, end = period[5:15], period[29:39]
        if 'DGF' in product['suffix'] or 'TDS' in product['suffix']:
            self.main_de_1.setEnabled(True)
            self.main_de_2.setEnabled(True)
            self.date_bt_1.setEnabled(True)
            self.date_bt_2.setEnabled(True)
        date_format = 'yyyy-MM-dd'
        if ',' in resolution:
            if resolution[:resolution.find(',')] == 'monthly-mean':
                date_format = 'yyyy-MM'
        else:
            if resolution == 'monthly-mean':
                date_format = 'yyyy-MM'
        if date_format == 'yyyy-MM':
            min_date = start[:-2] + '01'
            max_date = end[:-2] + '28'
        else:
            min_date = start
            max_date = end
        self.main_de_1.setDisplayFormat(date_format)
        self.main_de_2.setDisplayFormat(date_format)
        self.date_bt_1.clicked.connect(lambda: display_calendar(self))
        self.date_bt_2.clicked.connect(lambda: display_calendar(self))
        self.main_de_1.setMinimumDate(QtCore.QDate.fromString(min_date, QtCore.Qt.ISODate))
        self.main_de_1.setMaximumDate(QtCore.QDate.fromString(max_date, QtCore.Qt.ISODate))
        self.main_de_1.setDate(QtCore.QDate.fromString(start, QtCore.Qt.ISODate))
        self.main_de_2.setMinimumDate(QtCore.QDate.fromString(min_date, QtCore.Qt.ISODate))
        self.main_de_2.setMaximumDate(QtCore.QDate.fromString(max_date, QtCore.Qt.ISODate))
        self.main_de_2.setDate(QtCore.QDate.fromString(end, QtCore.Qt.ISODate))


def activate_download_method(self, product):
    deactivate_download_method(self)
    self.download_method.setEnabled(True)
    if not read_other_parameters(self, product['other_parameters'], 'download_method'):
        suffixes = product['suffix']
        for suffix in suffixes:
            if suffix == 'FTP':
                self.download_method.model().item(5).setEnabled(True)
            elif suffix == 'TDS':
                self.download_method.model().item(3).setEnabled(True)
                self.download_method.model().item(1).setEnabled(True)
            elif suffix == 'DGF':
                self.download_method.model().item(4).setEnabled(True)
                self.download_method.model().item(2).setEnabled(True)
        self.download_method.setCurrentIndex(0)
    else:
        self.download_method.model().item(5).setEnabled(True)
        self.download_method.setCurrentIndex(5)


def specific_period(self, i, product):
    logging.debug('gui_functions.py - specific_period')
    deactivate_date_picker(self)
    if not read_other_parameters(self, product['other_parameters'], 'download_method'):
        swath_temporal = product['swath_temporal']
        swath_temporal_resolution = product['swath_temporal_resolution']
        suffixes = product['suffix']
        if len(suffixes) == 1 and suffixes[0] == 'FTP':
            pass
        else:
            if i > 0:
                i -= 1
                index = swath_temporal[i].find('to')
                start = swath_temporal[i][:index]
                end = swath_temporal[i][index+2:]
                if 'Present' in end:
                    if '+' in end:
                        end = datetime.datetime.now() + datetime.timedelta(days=int(end[end.find('+') + 1:]))
                    else:
                        end = datetime.datetime.now()
                    end = end.strftime('%Y-%m-%d')
                date_format = 'yyyy-MM-dd'
                if swath_temporal_resolution is not None:
                    if ',' in swath_temporal_resolution[i]:
                        if swath_temporal_resolution[i][:swath_temporal_resolution[i].find(',')] == 'mm':
                            date_format = 'yyyy-MM'
                    else:
                        if swath_temporal_resolution[i] == 'mm':
                            date_format = 'yyyy-MM'
                if date_format == 'yyyy-MM':
                    min_date = start[:-2] + '01'
                    max_date = end[:-2] + '28'
                else:
                    min_date = start
                    max_date = end
                self.main_de_1.setDisplayFormat(date_format)
                self.main_de_2.setDisplayFormat(date_format)
                self.main_de_1.setMinimumDate(QtCore.QDate.fromString(min_date, QtCore.Qt.ISODate))
                self.main_de_1.setMaximumDate(QtCore.QDate.fromString(max_date, QtCore.Qt.ISODate))
                self.main_de_1.setDate(QtCore.QDate.fromString(start, QtCore.Qt.ISODate))
                self.main_de_2.setMinimumDate(QtCore.QDate.fromString(min_date, QtCore.Qt.ISODate))
                self.main_de_2.setMaximumDate(QtCore.QDate.fromString(max_date, QtCore.Qt.ISODate))
                self.main_de_2.setDate(QtCore.QDate.fromString(end, QtCore.Qt.ISODate))
                self.main_de_1.setEnabled(True)
                self.main_de_2.setEnabled(True)
                self.date_bt_1.setEnabled(True)
                self.date_bt_2.setEnabled(True)

    
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
        self.main_cb_8.currentIndexChanged.disconnect(self.set_modified)
        depth_signal = True
    except TypeError:
        depth_signal = False
    self.main_cb_7.setEnabled(False)
    self.main_cb_7.clear()
    self.main_cb_7.addItem('No depth...')
    self.main_cb_8.setEnabled(False)
    self.main_cb_8.clear()
    self.main_cb_8.addItem('No depth...')
    if depth_signal:
        self.main_cb_7.currentIndexChanged.connect(self.set_modified)
        self.main_cb_8.currentIndexChanged.connect(self.set_modified)


def deactivate_date_picker(self):
    logging.debug('gui_functions.py - deactivate_date_picker')
    self.main_de_1.setDisplayFormat('yyyy-MM-dd')
    self.main_de_2.setDisplayFormat('yyyy-MM-dd')
    self.main_de_1.setMinimumDate(QtCore.QDate.fromString('1579-01-01', QtCore.Qt.ISODate))
    self.main_de_2.setMaximumDate(QtCore.QDate.fromString('2518-01-01', QtCore.Qt.ISODate))
    self.main_de_1.setDate(QtCore.QDate.fromString('1979-01-01', QtCore.Qt.ISODate))
    self.main_de_1.setMinimumDate(QtCore.QDate.fromString('1579-01-01', QtCore.Qt.ISODate))
    self.main_de_2.setMaximumDate(QtCore.QDate.fromString('2518-01-01', QtCore.Qt.ISODate))
    self.main_de_2.setDate(QtCore.QDate.fromString('2018-01-01', QtCore.Qt.ISODate))
    self.main_de_1.setEnabled(False)
    self.main_de_2.setEnabled(False)
    self.date_bt_1.setEnabled(False)
    self.date_bt_2.setEnabled(False)
    try:
        self.date_bt_1.clicked.disconnect()
        self.date_bt_2.clicked.disconnect()
    except TypeError:
        pass


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
    clear_layout(self.variables_vertical_layout)
    deactivate_depth_cb(self)
    deactivate_area_ln(self)
    deactivate_date_picker(self)
    deactivate_download_method(self)
    clean_stylesheet_product(self)
    clean_stylesheet_dataset(self)
    clean_stylesheet_variable(self)


def deactivate_download_method(self):
    self.download_method.setEnabled(False)
    for i in range(5):
        self.download_method.model().item(i + 1).setEnabled(False)
    self.download_method.setCurrentIndex(0)


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
    

def display_calendar(self):
    logging.debug('gui_functions.py - display_calendar')
    object = {'date_bt_1': self.main_de_1, 'date_bt_2': self.main_de_2}
    object_name = self.sender().objectName()
    object_edit = object[object_name]
    current_date = object_edit.date().toString(QtCore.Qt.ISODate)
    min_date = object_edit.minimumDate().toString(QtCore.Qt.ISODate)
    max_date = object_edit.maximumDate().toString(QtCore.Qt.ISODate)
    y = self.sender().pos().y() + self.pos().y() + 152
    if object_edit.displayFormat() == 'yyyy-MM-dd':
        x = self.sender().pos().x() + self.pos().x() - 255
        self.calendar_test = MyDayCalendar(current_date, min_date, max_date)
    else:
        x = self.sender().pos().x() + self.pos().x() - 175
        self.calendar_test = MyMonthCalendar(current_date, min_date, max_date)
    self.calendar_test.move(x, y)
    self.calendar_test.setWindowFlags(QtCore.Qt.Popup|QtCore.Qt.FramelessWindowHint)
    self.calendar_test.exec_()
    if self.calendar_test.year is not None:
        year = str(self.calendar_test.year)
        month = str(self.calendar_test.month)
        day = str(self.calendar_test.day)
        if len(month) == 1:
            month = '0' + month
        if len(day) == 1:
            day = '0' + day
        if object_edit.displayFormat() == 'yyyy-MM':
            if object_name == 'date_bt_1':
                day = '01'
            else:
                day = '28'
        date = year + '-' + month + '-' + day
        object_edit.setDate(QtCore.QDate.fromString(date, QtCore.Qt.ISODate))


def read_other_parameters(self, other_parameters, parameter):
    if isinstance(other_parameters, dict):
        if parameter == 'download_method':
            try:
                if other_parameters['download_method'][self.main_cb_6.currentText()] == 'FTP':
                    return True
            except KeyError:
                return False
    else:
        return False
    

def clear_layout(layout):
    logging.debug('gui_functions.py - clear_layout')
    for i in reversed(range(layout.count())):   
        item = layout.itemAt(i)
        if isinstance(item, QtWidgets.QWidgetItem):
            item.widget().deleteLater()
        elif isinstance(item, QtWidgets.QLayout):
            clear_layout(item.layout())
        layout.removeItem(item)      

