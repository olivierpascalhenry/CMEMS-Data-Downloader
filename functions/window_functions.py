import logging
import os
import time
import platform
import subprocess
from ui.Ui_infowindow import Ui_infoWindow
from ui.Ui_aboutlogwindow import Ui_aboutlogWindow
from ui.Ui_optionwindow import Ui_optionWindow
from ui.Ui_apiwindow import Ui_apiWindow
from ui.Ui_updatewindow import Ui_updateWindow
from ui.Ui_downloadwindow import Ui_downloadWindow

from ui.Ui_storewindow import Ui_storeWindow
'''from ui.Ui_selectionwindow import Ui_selectionWindow

from ui.Ui_cancelwindow import Ui_cancelWindow

from ui.Ui_presavewindow import Ui_presaveWindow

from ui.Ui_expertwindow import Ui_expertWindow
from ui.Ui_successwindow import Ui_successWindow
from functions.thread_functions import DownloadFile, ECMWFDataDownloadThread'''
from PyQt5 import QtWidgets, QtCore, QtGui
from functions.thread_functions import DownloadFile


class MyInfo(QtWidgets.QDialog, Ui_infoWindow):
    def __init__(self, infoText):
        logging.debug('window_functions.py - MyInfo - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.iw_label_1.setText(infoText)
        self.iw_okButton.clicked.connect(self.closeWindow)
        
    def closeWindow(self):
        logging.debug('window_functions.py - MyInfo - closeWindow')
        self.close()

        
class MyAbout(QtWidgets.QDialog, Ui_aboutlogWindow):
    def __init__(self, text):
        logging.debug('window_functions.py - MyAbout - __init__')
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
        logging.debug('window_functions.py - MyApi - closeWindow')
        self.close()


class MyOptions(QtWidgets.QDialog, Ui_optionWindow):
    def __init__(self, config_dict, info_text):
        logging.debug('window_functions.py - MyOptions - __init__')
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
        all_info_boxes = self.findChildren(QtWidgets.QToolButton,)
        for widget in all_info_boxes:
            if 'infoButton' in widget.objectName():
                widget.clicked.connect(lambda: self.info_button())
        self.cancel = True
        self.read_config_dict()
    
    def read_config_dict(self):
        logging.debug('window_functions.py - MyOptions - read_config_dict')
        log_level = self.config_dict.get('LOG', 'level')
        log_path = self.config_dict.get('LOG', 'path')
        check_update = self.config_dict['OPTIONS'].getboolean('check_update')
        display_api = self.config_dict['OPTIONS'].getboolean('display_api_info')
        url = self.config_dict.get('CREDENTIALS', 'url')
        key = self.config_dict.get('CREDENTIALS', 'password')
        email = self.config_dict.get('CREDENTIALS', 'user')
        folder = self.config_dict.get('CREDENTIALS', 'folder')
        self.ow_comboBox_1.setCurrentIndex(self.ow_comboBox_1.findText(log_level))
        self.ow_lineEdit_1.setText(log_path)
        self.ow_lineEdit_2.setText(url)
        self.ow_lineEdit_3.setText(key)
        self.ow_lineEdit_4.setText(email)
        self.ow_lineEdit_5.setText(folder)
        self.ow_checkBox_1.setChecked(display_api)
        self.ow_checkBox_2.setChecked(check_update)
    
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
        self.config_dict.set('OPTIONS', 'display_api_info', str(self.ow_checkBox_1.isChecked()))
        self.config_dict.set('CREDENTIALS', 'url', str(self.ow_lineEdit_2.text()))
        self.config_dict.set('CREDENTIALS', 'password', str(self.ow_lineEdit_3.text()))
        self.config_dict.set('CREDENTIALS', 'user', str(self.ow_lineEdit_4.text()))
        self.config_dict.set('CREDENTIALS', 'folder', str(self.ow_lineEdit_5.text()))
        self.close_window()
    
    def info_button(self):
        logging.debug('window_functions.py - MyOptions - info_button - self.sender().objectName() ' + self.sender().objectName())
        if 'infoButton' in self.sender().objectName():
            x = QtGui.QCursor.pos().x()
            y = QtGui.QCursor.pos().y()
            x = x - 175
            y = y + 50
            self.infoWindow = MyInfo(self.info_text[self.sender().objectName()])
            self.infoWindow.setMinimumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
            self.infoWindow.setMaximumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
            self.infoWindow.setGeometry(x, y, 450, self.infoWindow.sizeHint().height())
            self.infoWindow.exec_()
    
    def close_window(self):
        logging.debug('window_functions.py - MyOptions - closeWindow')
        self.close()


class MyUpdate(QtWidgets.QDialog, Ui_storeWindow):
    def __init__(self, url, folder):
        logging.debug('window_functions.py - MyUpdate - __init__')
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
        logging.debug('window_functions.py - MyUpdate - closeEvent')
        self.thread.download_update.disconnect(self.update_progress_bar)
        if self.cancel:
            os.remove(self.update_file)


class MyWarningUpdate(QtWidgets.QDialog, Ui_updateWindow):
    def __init__(self, frozen):
        logging.debug('window_functions.py - MyWarningUpdate - __init__')
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
        logging.debug('window_functions.py - MyWarningUpdate - closeWindow')
        self.buttonName = self.sender().objectName()
        self.close()


'''class MySelect(QtWidgets.QDialog, Ui_selectionWindow):
    def __init__(self):
        logging.debug('window_functions.py - MySelect - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.sw_okButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        logging.debug('window_functions.py - MySelect - closeWindow')
        self.close()
        
        
class MyQuery(QtWidgets.QDialog, Ui_downloadWindow):
    def __init__(self, query, config_dict):
        logging.debug('window_functions.py - MyQuery - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.query = query
        self.config_dict = config_dict
        self.browser_text = []
        self.download_data()
        self.dw_button.clicked.connect(self.cancel_window)
    
    def download_data(self):
        logging.debug('window_functions.py - MyQuery - download_data')
        api_url = self.config_dict.get('CREDENTIALS', 'url')
        api_key = self.config_dict.get('CREDENTIALS', 'key')
        api_email = self.config_dict.get('CREDENTIALS', 'email')
        file_folder = self.config_dict.get('CREDENTIALS', 'folder')
        self.thread = ECMWFDataDownloadThread(self.query, api_url, api_key, api_email, file_folder)
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
            self.dw_browser.setText(string)
            self.dw_browser.moveCursor(QtGui.QTextCursor.End)
    
    def update_progress_bar(self, val):
        self.dw_progress.setValue(val)
    
    def update_bar_text(self, string):
        self.dw_label.setText(string)
    
    def cancel_window(self):
        logging.debug('window_functions.py - MyQuery - cancel_window')
        if not self.thread.downloading:
            self.cancelWindow = MyCancel()
            x1, y1, w1, h1 = self.geometry().getRect()
            _, _, w2, h2 = self.cancelWindow.geometry().getRect()
            x2 = x1 + w1/2 - w2/2
            y2 = y1 + h1/2 - h2/2
            self.cancelWindow.setGeometry(x2, y2, w2, h2)
            self.cancelWindow.exec_()
            if self.cancelWindow.cancel:
                self.close()
        else:
            self.cancel_download()
    
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
        self.dw_button.clicked.disconnect(self.cancel_window)
        self.dw_button.clicked.connect(self.close)
    
    def download_done(self, val):
        logging.debug('window_functions.py - MyQuery - download_done')
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
    
    def closeEvent(self, event):
        logging.debug('window_functions.py - MyQuery - closeEvent')
        self.thread.download_update.disconnect(self.update_progress)
        self.thread.download_done.disconnect(self.download_done)
        self.thread.download_failed.disconnect(self.download_failed)
        self.thread.stop()


class MyCancel(QtWidgets.QDialog, Ui_cancelWindow):
    def __init__(self):
        logging.debug('window_functions.py - MyCancel - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.cancel = False
        self.cw_okButton.clicked.connect(self.closeWindow)
        self.cw_cancelButton.clicked.connect(self.set_cancel)
        
    def set_cancel(self):
        logging.debug('window_functions.py - MyCancel - set_cancel')
        self.cancel = True
        self.closeWindow()
    
    def closeWindow(self):
        logging.debug('window_functions.py - MyCancel - closeWindow')
        self.close()


class MyWarning(QtWidgets.QDialog, Ui_presaveWindow):
    def __init__(self, string):
        QtWidgets.QWidget.__init__(self)
        logging.debug('mainwindow.py - MyWarning - __init__ - string ' + string)
        self.setupUi(self)
        self.cancel_button.setFocus(True)
        all_buttons = self.findChildren(QtWidgets.QToolButton)
        for widget in all_buttons:
            widget.clicked.connect(self.closeWindow)
        self.nosave_button.setText(string + " without saving")

    def closeWindow(self):
        logging.debug('window_functions.py - MyWarning - closeWindow')
        self.buttonName = self.sender().objectName()
        self.close()
        
        

        
        
class MyExpert(QtWidgets.QDialog, Ui_expertWindow):
    def __init__(self, info_text):
        logging.debug('window_functions.py - MyExpert - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.query = {}
        self.info_text = info_text
        self.cancel.clicked.connect(self.closeWindow)
        self.submit.clicked.connect(self.prepare_query)
        all_info_boxes = self.findChildren(QtWidgets.QToolButton,)
        for widget in all_info_boxes:
            if 'infoButton' in widget.objectName():
                widget.clicked.connect(lambda: self.info_button())
    
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
        keyword_list = [self.main_ln_1,self.main_ln_2,self.main_ln_3,self.main_ln_4,self.main_ln_5,self.main_ln_6,self.main_ln_7,self.area_ln_1,
                          self.area_ln_2,self.area_ln_3,self.area_ln_4,self.area_ln_5,self.area_ln_6,self.other_ln_1,self.other_ln_2,self.other_ln_3]
        name_list = ['dataset','stream','type','class','expver','levtype','levelist','date','step','time','grid','area','param','target','format']
        for index, keyword in enumerate(keyword_list):
            try:
                if keyword.text():
                    self.query[name_list[index]] = keyword.text()
            except AttributeError:
                if keyword.toPlainText():
                    string = keyword.toPlainText()
                    i, j = -3, 0
                    while j < len(string):
                        j = string.find(': ', i + 3)
                        keyword = string[i + 3:j]
                        i = string.find(' ; ', j)
                        if i != -1:
                            value = string[j + 2:i]
                            self.query[keyword] = value
                        else:
                            value = string[j + 2:]
                            self.query[keyword] = value
                            break
        self.closeWindow()
    
    def closeWindow(self):
        logging.debug('window_functions.py - MyExpert - closeWindow')
        self.close()


class MySuccess(QtWidgets.QDialog, Ui_successWindow):
    def __init__(self, download_time, file_path, average_speed):
        QtWidgets.QWidget.__init__(self)
        logging.debug('mainwindow.py - MySuccess - __init__')
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
        logging.debug('window_functions.py - MySuccess - closeWindow')
        self.close()'''
