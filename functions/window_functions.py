import logging
import os
import time
import platform
import subprocess
import datetime
from calendar import monthrange
from ui.Ui_calendardwindow import Ui_calendardWindow
from ui.Ui_calendarmwindow import Ui_calendarmWindow
from ui.Ui_infowindow import Ui_infoWindow
from ui.Ui_productwindow import Ui_productWindow
from ui.Ui_aboutlogwindow import Ui_aboutlogWindow
from ui.Ui_optionwindow import Ui_optionWindow
from ui.Ui_apiwindow import Ui_apiWindow
from ui.Ui_updatewindow import Ui_updateWindow
from ui.Ui_downloadwindow import Ui_downloadWindow
from ui.Ui_presavewindow import Ui_presaveWindow
from ui.Ui_selectionwindow import Ui_selectionWindow
from ui.Ui_storewindow import Ui_storeWindow
from ui.Ui_successwindow import Ui_successWindow
from ui.Ui_credentialswindow import Ui_credentialsWindow
from ui.Ui_expertwindow import Ui_expertWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from functions.thread_functions import DownloadFile, CMEMSDataDownloadThread, DownloadProducts


class MyDayCalendar(QtWidgets.QDialog, Ui_calendardWindow):
    def __init__(self, object_date, min_date, max_date):
        logging.info('window_functions.py - MyDayCalendar - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.month_cb.setItemDelegate(itemDelegate)
        self.current_year = int(object_date[:4])
        self.current_month = int(object_date[5:7])
        self.current_day = int(object_date[8:])
        self.old_year = int(object_date[:4])
        self.old_month = int(object_date[5:7])
        self.old_day = int(object_date[8:])
        self.min = datetime.datetime(int(min_date[:4]), int(min_date[5:7]), int(min_date[8:]))
        self.max = datetime.datetime(int(max_date[:4]), int(max_date[5:7]), int(max_date[8:]))
        self.year = None
        self.month = None
        self.day = None
        self.past_button.clicked.connect(self.minus_month)
        self.future_button.clicked.connect(self.plus_month)
        self.year_sb.valueChanged.connect(self.year_changed)
        self.month_cb.currentIndexChanged.connect(self.month_changed)
        self.table.cellClicked.connect(self.set_date)
        self.display_date()
    
    def minus_month(self):
        logging.debug('window_functions.py - MyDayCalendar - minus_month')
        self.current_month -= 1
        if self.current_month == 0:
            self.current_year -= 1
            self.current_month = 12
        self.display_date()
    
    def plus_month(self):
        logging.debug('window_functions.py - MyDayCalendar - plus_month')
        self.current_month += 1
        if self.current_month == 13:
            self.current_year += 1
            self.current_month = 1
        self.display_date()
    
    def year_changed(self, val):
        logging.debug('window_functions.py - MyDayCalendar - year_changed')
        self.current_year = val
        self.parse_days()
    
    def month_changed(self, val):
        logging.debug('window_functions.py - MyDayCalendar - month_changed')
        self.current_month = val + 1
        self.parse_days()
    
    def display_date(self):
        logging.debug('window_functions.py - MyDayCalendar - display_date')
        self.year_sb.valueChanged.disconnect(self.year_changed)
        self.month_cb.currentIndexChanged.disconnect(self.month_changed)
        self.year_sb.setValue(self.current_year)
        self.month_cb.setCurrentIndex(self.current_month - 1)
        self.year_sb.valueChanged.connect(self.year_changed)
        self.month_cb.currentIndexChanged.connect(self.month_changed)
        self.parse_days()
    
    def parse_days(self):
        logging.debug('window_functions.py - MyDayCalendar - parse_days')
        day = 1
        start = datetime.date(self.current_year, self.current_month, 1).weekday()
        _, number_days = monthrange(self.current_year, self.current_month)
        end = datetime.date(self.current_year, self.current_month, number_days).weekday()
        for col in range(0, 7):
            self.table.item(1,col).setSelected(False)
            self.table.item(1,col).setText('')
            self.table.item(1,col).setBackground(QtGui.QColor(240, 240, 240))
            if col < start:
                self.table.item(1,col).setBackground(QtGui.QColor(230, 230, 230))
                self.table.item(1,col).setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            else:
                self.table.item(1,col).setText(str(day))
                current = datetime.datetime(self.current_year, self.current_month, day)
                if current < self.min or current > self.max:
                    self.table.item(1,col).setBackground(QtGui.QColor(230, 230, 230))
                    self.table.item(1,col).setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                else:
                    self.table.item(1,col).setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
                if self.current_year == self.old_year and self.current_month == self.old_month and self.current_day == day:
                    self.table.item(1,col).setSelected(True)
                day += 1
        for row in range(2, 7):
            for col in range(0, 7):
                self.table.item(row,col).setSelected(False)
                self.table.item(row,col).setText('')
                self.table.item(row,col).setBackground(QtGui.QColor(240, 240, 240))
                if day > number_days:
                    self.table.item(row,col).setBackground(QtGui.QColor(230, 230, 230))
                    self.table.item(row,col).setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                else:
                    self.table.item(row,col).setText(str(day))
                    current = datetime.datetime(self.current_year, self.current_month, day)
                    if current < self.min or current > self.max:
                        self.table.item(row,col).setBackground(QtGui.QColor(230, 230, 230))
                        self.table.item(row,col).setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                    else:
                        self.table.item(row,col).setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
                    if self.current_year == self.old_year and self.current_month == self.old_month and self.current_day == day:
                        self.table.item(row,col).setSelected(True)
                    day += 1
    
    def set_date(self, row, col):
        logging.debug('window_functions.py - MyDayCalendar - set_date')
        if self.table.item(row, col).isSelected():
            self.year = self.current_year
            self.month = self.current_month
            self.day = int(self.table.item(row, col).text())
            time.sleep(0.15)
            self.closeWindow()
        
    def closeWindow(self):
        logging.info('window_functions.py - MyDayCalendar - closeWindow')
        self.close()


class MyMonthCalendar(QtWidgets.QDialog, Ui_calendarmWindow):
    def __init__(self, object_date, min_date, max_date):
        logging.info('window_functions.py - MyMonthCalendar - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.current_year = int(object_date[:4])
        self.current_month = int(object_date[5:7])
        self.current_day = int(object_date[8:])
        self.old_year = int(object_date[:4])
        self.min = datetime.datetime(int(min_date[:4]), int(min_date[5:7]), int(min_date[8:]))
        self.max = datetime.datetime(int(max_date[:4]), int(max_date[5:7]), int(max_date[8:]))
        self.year = None
        self.month = None
        self.day = None
        self.month_numbers = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6,
                              'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
        self.month_names = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June',
                            7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
        self.year_sb.valueChanged.connect(self.year_changed)
        self.display_year()
        self.set_month()
        self.past_button.clicked.connect(self.minus_year)
        self.future_button.clicked.connect(self.plus_year)
        self.tableWidget.cellClicked.connect(self.set_date)
        
    def minus_year(self):
        logging.debug('window_functions.py - MyDayCalendar - minus_year')
        self.current_year -= 1
        self.display_year()
    
    def plus_year(self):
        logging.debug('window_functions.py - MyDayCalendar - plus_year')
        self.current_year += 1
        self.display_year()
    
    def year_changed(self, val):
        logging.debug('window_functions.py - MyDayCalendar - year_changed')
        self.current_year = val
    
    def display_year(self):
        logging.debug('window_functions.py - MyDayCalendar - display_year')
        self.year_sb.setValue(self.current_year)
        for row in range(3):
            for col in range(4):
                self.tableWidget.item(row,col).setSelected(False)
                self.tableWidget.item(row,col).setBackground(QtGui.QColor(240, 240, 240))
                self.tableWidget.item(row,col).setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
                current = datetime.datetime(self.current_year, self.month_numbers[self.tableWidget.item(row, col).text()], self.current_day)
                if current < self.min or current > self.max:
                    self.tableWidget.item(row,col).setBackground(QtGui.QColor(230, 230, 230))
                    self.tableWidget.item(row,col).setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                if self.current_year == self.old_year and self.tableWidget.item(row, col).text() == self.month_names[self.current_month]:
                    self.tableWidget.item(row,col).setSelected(True)
    
    def set_month(self):
        logging.debug('window_functions.py - MyDayCalendar - set_month')
        found = False
        for row in range(3):
            for col in range(4):
                if self.month_names[self.current_month] == self.tableWidget.item(row,col).text():
                    self.tableWidget.item(row,col).setSelected(True)
                    found = True
                if found:
                    break
            if found:
                break  
    
    def set_date(self, row, col):
        logging.debug('window_functions.py - MyDayCalendar - set_date')
        if self.tableWidget.item(row, col).isSelected():
            self.year = self.current_year
            self.month = self.month_numbers[self.tableWidget.item(row, col).text()]
            self.day = self.current_day
            time.sleep(0.15)
            self.closeWindow()
        
    def closeWindow(self):
        logging.info('window_functions.py - MyMonthCalendar - closeWindow')
        self.close()


class MyInfo(QtWidgets.QDialog, Ui_infoWindow):
    def __init__(self, infoText):
        logging.info('window_functions.py - MyInfo - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.iw_label_1.setText(infoText)
        self.iw_okButton.clicked.connect(self.closeWindow)
        
    def closeWindow(self):
        logging.info('window_functions.py - MyInfo - closeWindow')
        self.close()


class MyProduct(QtWidgets.QDialog, Ui_productWindow):
    def __init__(self, name, product):
        logging.info('window_functions.py - MyProduct - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.name = name
        self.product = product
        self.button.clicked.connect(self.closeWindow)
        self.parse_product_information()
    
    def parse_product_information(self):
        logging.debug('window_functions.py - MyProduct - parse_product_information')
        self.edit_1.setText(self.name)
        self.edit_2.setText(self.product['information']['description'])
        self.edit_3.setText(self.product['information']['production'])
        self.edit_4.setText(self.product['information']['level'])
        self.edit_5.setText(self.product['information']['spatial_resolution'])
        self.edit_6.setText(self.product['information']['temporal_resolution'])
        self.edit_7.setText(self.product['information']['vertical_coverage'])
        self.edit_8.setText(self.product['information']['temporal_coverage'])
        self.edit_9.setText(self.product['information']['product_type'])
    
    def closeWindow(self):
        logging.info('window_functions.py - MyProduct - closeWindow')
        self.close()

        
class MyAbout(QtWidgets.QDialog, Ui_aboutlogWindow):
    def __init__(self, text):
        logging.info('window_functions.py - MyAbout - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.label_1.setText(text)
        self.browser.setPlainText(open("documentation/changelog.txt").read())
        self.button.clicked.connect(self.closeWindow)

    def closeWindow(self):
        logging.debug('window_functions.py - MyAbout - closeWindow')
        self.close()


class MyApi(QtWidgets.QDialog, Ui_apiWindow):
    def __init__(self):
        logging.debug('window_functions.py - MyApi - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.button.clicked.connect(self.closeWindow)
        
    def closeWindow(self):
        logging.info('window_functions.py - MyApi - closeWindow')
        self.close()


class MyOptions(QtWidgets.QDialog, Ui_optionWindow):
    def __init__(self, config_dict, info_text):
        logging.info('window_functions.py - MyOptions - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.config_dict = config_dict
        self.info_text = info_text
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.ow_comboBox_1.setItemDelegate(itemDelegate)
        self.ow_okButton.clicked.connect(self.save_and_close)
        self.ow_cancelButton.clicked.connect(self.close_window)
        self.ow_openButton_1.clicked.connect(self.get_directory)
        self.ow_openButton_2.clicked.connect(self.get_directory)
        all_info_boxes = self.findChildren(QtWidgets.QToolButton)
        for widget in all_info_boxes:
            if 'infoButton' in widget.objectName():
                widget.clicked.connect(lambda: self.info_button())
        self.cancel = True
        self.read_config_dict()
        self.setTabOrder(self.ow_lineEdit_1,self.ow_lineEdit_2)
        self.setTabOrder(self.ow_lineEdit_2,self.ow_lineEdit_3)
        self.setTabOrder(self.ow_lineEdit_3,self.ow_lineEdit_4)
        self.ow_lineEdit_1.setFocus()
    
    def read_config_dict(self):
        logging.debug('window_functions.py - MyOptions - read_config_dict')
        log_level = self.config_dict.get('LOG', 'level')
        log_path = self.config_dict.get('LOG', 'path')
        check_database = self.config_dict['OPTIONS'].getboolean('check_database')
        check_update = self.config_dict['OPTIONS'].getboolean('check_update')
        display_api = self.config_dict['OPTIONS'].getboolean('display_api_info')
        password = self.config_dict.get('CREDENTIALS', 'password')
        username = self.config_dict.get('CREDENTIALS', 'user')
        folder = self.config_dict.get('CREDENTIALS', 'folder')
        self.ow_comboBox_1.setCurrentIndex(self.ow_comboBox_1.findText(log_level))
        self.ow_lineEdit_1.setText(log_path)
        self.ow_lineEdit_2.setText(username)
        self.ow_lineEdit_3.setText(password)
        self.ow_lineEdit_4.setText(folder)
        self.ow_checkBox_1.setChecked(display_api)
        self.ow_checkBox_2.setChecked(check_update)
        self.ow_checkBox_3.setChecked(check_database)
    
    def get_directory(self):
        logging.debug('window_functions.py - MyOptions - get_directory')
        file_dialog = QtWidgets.QFileDialog()
        out_dir = file_dialog.getExistingDirectory(self, "Select Directory")
        if self.sender().objectName() == 'ow_openButton_1':
            self.ow_lineEdit_1.setText(str(out_dir.replace('/','\\')))
        elif self.sender().objectName() == 'ow_openButton_2':
            self.ow_lineEdit_5.setText(str(out_dir.replace('/','\\')))
    
    def save_and_close(self):
        logging.debug('window_functions.py - MyOptions - save_and_close')
        self.cancel = False
        self.config_dict.set('LOG', 'level', str(self.ow_comboBox_1.currentText()))
        self.config_dict.set('LOG', 'path', str(self.ow_lineEdit_1.text()))
        self.config_dict.set('OPTIONS', 'check_update', str(self.ow_checkBox_2.isChecked()))
        self.config_dict.set('OPTIONS', 'check_database', str(self.ow_checkBox_3.isChecked()))
        self.config_dict.set('OPTIONS', 'display_api_info', str(self.ow_checkBox_1.isChecked()))
        self.config_dict.set('CREDENTIALS', 'password', str(self.ow_lineEdit_3.text()))
        self.config_dict.set('CREDENTIALS', 'user', str(self.ow_lineEdit_2.text()))
        self.config_dict.set('CREDENTIALS', 'folder', str(self.ow_lineEdit_4.text()))
        self.close_window()
    
    def info_button(self):
        logging.debug('window_functions.py - MyOptions - info_button - self.sender().objectName() ' + self.sender().objectName())
        if 'infoButton' in self.sender().objectName():
            self.infoWindow = MyInfo(self.info_text[self.sender().objectName()])
            self.infoWindow.move(QtGui.QCursor.pos().x() - 275, QtGui.QCursor.pos().y() + 20)
            self.infoWindow.exec_()
    
    def close_window(self):
        logging.info('window_functions.py - MyOptions - close_window')
        self.close()


class MyUpdate(QtWidgets.QDialog, Ui_storeWindow):
    def __init__(self, url, folder):
        logging.info('window_functions.py - MyUpdate - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.temp_folder = folder
        self.url = url
        if platform.system() == 'Windows':
            self.update_file = self.temp_folder + '\\' + self.url[self.url.rfind('/')+1:]
        elif platform.system() == 'Linux':
            self.update_file = self.temp_folder + '/' + self.url[self.url.rfind('/')+1:]
        self.sw_button.clicked.connect(self.cancel_download)
        self.cancel = False
        self.download_update()
    
    def update_progress_bar(self, val):
        if isinstance(val, list):
            self.progressBar.setValue(val[0])
            self.sw_label.setText(val[1])
        else:
            self.progressBar.setValue(val)
    
    def download_update(self):
        logging.debug('window_functions.py - MyUpdate - download_update')
        self.thread = DownloadFile(self.url, self.update_file)
        self.thread.download_update.connect(self.update_progress_bar)
        self.thread.download_done.connect(self.close)
        self.thread.download_failed.connect(self.download_failed)
        self.thread.start()
    
    def cancel_download(self):
        logging.debug('window_functions.py - MyUpdate - cancel_download')
        self.thread.cancel_download()
        self.cancel = True
        time.sleep(0.25)
        self.close()
        
    def download_failed(self):
        logging.debug('window_functions.py - MyUpdate - download_failed')
        self.update_progress_bar(0)
        self.sw_label.setText('Download failed')
        self.cancel_download()
        
    def closeEvent(self, event):
        logging.info('window_functions.py - MyUpdate - closeEvent')
        self.thread.download_update.disconnect(self.update_progress_bar)
        if self.cancel:
            os.remove(self.update_file)


class MyDatabaseUpdate(QtWidgets.QDialog, Ui_storeWindow):
    def __init__(self, product_list):
        logging.info('window_functions.py - MyDatabaseUpdate - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.product_list = product_list
        self.cancel = False
        self.done = False
        self.download_database()
    
    def update_progress_bar(self, val):
        if isinstance(val, list):
            self.progressBar.setValue(val[0])
            self.sw_label.setText(val[1])
        else:
            self.progressBar.setValue(val)
    
    def download_database(self):
        logging.debug('window_functions.py - MyDatabaseUpdate - download_database')
        self.thread = DownloadProducts(self.product_list)
        self.thread.download_update.connect(self.update_progress_bar)
        self.thread.download_done.connect(self.download_done)
        self.thread.download_failed.connect(self.download_failed)
        self.thread.start()

    def cancel_download(self):
        logging.debug('window_functions.py - MyDatabaseUpdate - cancel_download')
        self.thread.cancel_download()
        self.cancel = True
        time.sleep(0.25)
        self.close()
        
    def download_failed(self):
        logging.debug('window_functions.py - MyDatabaseUpdate - download_failed')
        self.update_progress_bar(0)
        self.sw_label.setText('Download failed')
        self.cancel_download()
    
    def download_done(self, val):
        logging.debug('window_functions.py - MyDatabaseUpdate - download_done')
        self.done = True
        if val:
            text = ('During the update of the product database, one or more files were considered as corrupted and were not included in the '
                    + 'database. Please restart CDD and launch a new update procedure to update again the database.')
            self.infoWindow = MyInfo(text)
            _, _, w, h = QtWidgets.QDesktopWidget().screenGeometry(-1).getRect()
            _, _, w2, h2 = self.infoWindow.geometry().getRect()
            self.infoWindow.setGeometry(w/2 - w2/2, h/2 - h2/2, 450, self.infoWindow.sizeHint().height())
            self.infoWindow.setMinimumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
            self.infoWindow.setMaximumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
            self.infoWindow.exec_()
        self.close()
    
    def closeEvent(self, event):
        logging.info('window_functions.py - MyDatabaseUpdate - closeEvent')
        if self.cancel:
            pass


class MyWarningUpdate(QtWidgets.QDialog, Ui_updateWindow):
    def __init__(self, frozen):
        logging.info('window_functions.py - MyWarningUpdate - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        if not frozen:
            self.label_1.setText('<p>Click on <b>Download</b> to download the latest update from GitHub repository.</p>'
                                 + '<p>Once the download is over, the software will close automatically. The package is'
                                 + ' downloaded in the <b>Download</b> folder of your operating system. You will have t'
                                 + 'o uncompress it and move all files in the directory of <b>CMEMS Data Downloader</b>'
                                 + '. Do not delete <i>cmems_downloader.ini</i> if you want to keep all your options.</p>')
            self.update_button.setText('Download')
        self.update_button.clicked.connect(self.closeWindow)
        self.cancel_button.clicked.connect(self.closeWindow)
        
    def closeWindow(self):
        logging.info('window_functions.py - MyWarningUpdate - closeWindow')
        self.buttonName = self.sender().objectName()
        self.close()


class MySelect(QtWidgets.QDialog, Ui_selectionWindow):
    def __init__(self):
        logging.info('window_functions.py - MySelect - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.sw_okButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        logging.info('window_functions.py - MySelect - closeWindow')
        self.close()
        
        
class MyQuery(QtWidgets.QDialog, Ui_downloadWindow):
    def __init__(self, query, motu_url, user, password, folder=None, filename=None):
        logging.info('window_functions.py - MyQuery - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.query = query
        if self.query['action'] == 'getSize':
            self.setWindowTitle('Check size')
        self.motu_url = motu_url
        self.user = user
        self.password = password
        self.folder = folder
        self.filename = filename
        self.browser_text = []
        self.dw_button.clicked.connect(self.cancel_download)
        self.download_data()
    
    def download_data(self):
        logging.debug('window_functions.py - MyQuery - download_data')
        self.thread = CMEMSDataDownloadThread(self.query, self.motu_url, self.user, self.password, self.folder, self.filename)
        self.thread.download_update.connect(self.update_progress)
        self.thread.download_done.connect(self.download_done)
        self.thread.download_failed.connect(self.download_failed)
        self.thread.start()
    
    def update_progress(self, val):
        self.update_browser(val['browser_text'])
        self.update_progress_bar(val['progress'])
        self.update_bar_text(val['bar_text'])
    
    def update_browser(self, text):
        if text:
            self.browser_text.append(text)
            string = ''
            for t in self.browser_text:
                string += t + '<br>'
            string = string[:-4]
            self.dw_browser.setText(string)
            self.dw_browser.moveCursor(QtGui.QTextCursor.End)
    
    def update_progress_bar(self, val):
        self.dw_progress.setValue(val)
    
    def update_bar_text(self, string):
        self.dw_label.setText(string)
    
    def cancel_download(self):
        logging.debug('window_functions.py - MyQuery - cancel_download')
        self.thread.cancel_download()
        time.sleep(0.25)
        self.close()
        
    def download_failed(self, val):
        logging.debug('window_functions.py - MyQuery - download_failed')
        self.update_progress_bar(0)
        self.dw_label.setText('Download failed')
        self.update_browser(val)
        self.dw_button.setText('Quit')
        self.dw_button.clicked.disconnect(self.cancel_download)
        self.dw_button.clicked.connect(self.close)
    
    def download_done(self, val):
        logging.debug('window_functions.py - MyQuery - download_done')
        if val:
            time = str(val['download_time'])
            index1 = time.find(':')
            index2 = time.find(':', index1 + 1)
            hour = time[:index1]
            min = time[index1 + 1:index2]
            sec = time[index2 + 1:]
            if len(hour) == 1:
                hour = '0' + hour
            if len(min) == 1:
                min ='0' + min
            self.download_time = hour + 'h ' + min + 'mn ' + sec + 's'
            self.file_path = val['file_path']
            self.average_speed = val['average_speed']
            self.close()
        else:
            self.size_recovered()
            
    def size_recovered(self):
        logging.debug('window_functions.py - MyQuery - size_recovered')
        self.update_progress_bar(0)
        self.dw_label.setText('Size recovered')
        self.dw_button.setText('Quit')
        self.dw_button.clicked.disconnect(self.cancel_download)
        self.dw_button.clicked.connect(self.close)
    
    def closeEvent(self, event):
        logging.info('window_functions.py - MyQuery - closeEvent')
        self.thread.download_update.disconnect(self.update_progress)
        self.thread.download_done.disconnect(self.download_done)
        self.thread.download_failed.disconnect(self.download_failed)
        self.thread.stop()


class MyWarning(QtWidgets.QDialog, Ui_presaveWindow):
    def __init__(self, string):
        QtWidgets.QWidget.__init__(self)
        logging.info('mainwindow.py - MyWarning - __init__ - string ' + string)
        self.setupUi(self)
        self.cancel_button.setFocus(True)
        all_buttons = self.findChildren(QtWidgets.QToolButton)
        for widget in all_buttons:
            widget.clicked.connect(self.closeWindow)
        self.nosave_button.setText(string + " without saving")

    def closeWindow(self):
        logging.info('window_functions.py - MyWarning - closeWindow')
        self.buttonName = self.sender().objectName()
        self.close()
        
        
class MyCredentials(QtWidgets.QDialog, Ui_credentialsWindow):
    def __init__(self, user, password):
        QtWidgets.QWidget.__init__(self)
        logging.info('mainwindow.py - MyCredentials - __init__')
        self.setupUi(self)
        if user:
            self.edit_1.setText(user)
        if password:
            self.edit_2.setText(password)
        self.username = ''
        self.password = ''
        self.submit.clicked.connect(self.set_username_password)
        self.cancel.clicked.connect(self.closeWindow)

    def set_username_password(self):
        logging.debug('window_functions.py - MyCredentials - set_username_password')
        self.username = str(self.edit_1.text())
        self.password = str(self.edit_2.text())
        self.closeWindow()

    def closeWindow(self):
        logging.info('window_functions.py - MyCredentials - closeWindow')
        self.close()
        
        
class MyExpert(QtWidgets.QDialog, Ui_expertWindow):
    def __init__(self, info_text):
        logging.debug('window_functions.py - MyExpert - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.info_text = info_text
        self.cancel.clicked.connect(self.closeWindow)
        self.submit.clicked.connect(self.prepare_query)
        self.setTabOrder(self.edit_1,self.edit_2)
        self.setTabOrder(self.edit_2,self.edit_3)
        self.setTabOrder(self.edit_3,self.edit_4)
        self.setTabOrder(self.edit_4,self.edit_5)
        self.setTabOrder(self.edit_5,self.edit_6)
        self.setTabOrder(self.edit_6,self.edit_7)
        self.setTabOrder(self.edit_7,self.edit_8)
        self.setTabOrder(self.edit_8,self.edit_9)
        self.setTabOrder(self.edit_9,self.edit_10)
        self.setTabOrder(self.edit_10,self.edit_12)
        self.setTabOrder(self.edit_12,self.edit_13)
        self.edit_1.setFocus()
        self.query = {}
        self.filename = ''
        
        '''all_info_boxes = self.findChildren(QtWidgets.QToolButton,)
        for widget in all_info_boxes:
            if 'infoButton' in widget.objectName():
                widget.clicked.connect(lambda: self.info_button())'''
    
    def info_button(self):
        logging.debug('window_functions.py - MyExpert - info_button - self.sender().objectName() ' + self.sender().objectName())
        if 'infoButton' in self.sender().objectName():
            if len(self.info_text[self.sender().objectName()]) > 400:
                w = 650
            else:
                w = 450
            x = QtGui.QCursor.pos().x()
            y = QtGui.QCursor.pos().y()
            x = x - 225
            y = y + 50
            self.infoWindow = MyInfo(self.info_text[self.sender().objectName()])
            self.infoWindow.setMinimumSize(QtCore.QSize(w, self.infoWindow.sizeHint().height()))
            self.infoWindow.setMaximumSize(QtCore.QSize(w, self.infoWindow.sizeHint().height()))
            self.infoWindow.setGeometry(x, y, w, self.infoWindow.sizeHint().height())
            self.infoWindow.exec_()
    
    def prepare_query(self):
        logging.debug('window_functions.py - MyExpert - prepare_query')
        try:
            self.filename = str(self.edit_4.text())
            keyword_list = [self.edit_1, self.edit_2, self.edit_9, self.edit_10, self.edit_7, self.edit_8, 
                              self.edit_5, self.edit_6, self.edit_12, self.edit_13, self.edit_3]
            name_list = ['service', 'product', 'x_lo', 'x_hi', 'y_lo', 
                         'y_hi', 't_lo', 't_hi','z_lo', 'z_hi', 'variable']
            for index, keyword in enumerate(keyword_list):
                if keyword.text():
                    if ',' in keyword.text():
                        var_list = [x for x in keyword.text().split(',')]
                        self.query[name_list[index]] = var_list
                    else:
                        self.query[name_list[index]] = keyword.text()
            self.query['scriptVersion'] = '1.5.00'
            self.query['mode'] = 'status'
        except Exception:
            self.query = {}
            self.filename = ''
        self.closeWindow()
    
    def closeWindow(self):
        logging.debug('window_functions.py - MyExpert - closeWindow - query' + str(self.query))
        self.close()


class MySuccess(QtWidgets.QDialog, Ui_successWindow):
    def __init__(self, download_time, file_path, average_speed):
        QtWidgets.QWidget.__init__(self)
        logging.info('mainwindow.py - MySuccess - __init__')
        self.setupUi(self)
        self.download_time = download_time
        self.file_path = file_path
        self.average_speed = average_speed
        self.label_6.setText(self.average_speed)
        self.label_8.setText(self.download_time)
        self.label_7.setText(self.file_path)
        self.label_7.setCursorPosition(0)
        self.open.clicked.connect(self.open_path)
        self.button.clicked.connect(self.closeWindow)

    def open_path(self):
        logging.debug('mainwindow.py - MySuccess - open_path')
        folder = os.path.dirname(self.file_path)
        if platform.system() == 'Windows':
            subprocess.Popen('explorer "' + folder + '"')
        elif platform.system() == 'Linux':
            subprocess.Popen(['xdg-open', folder])
        elif platform.system() == 'Darwin':
            subprocess.Popen(['open', folder])

    def closeWindow(self):
        logging.info('window_functions.py - MySuccess - closeWindow')
        self.close()
