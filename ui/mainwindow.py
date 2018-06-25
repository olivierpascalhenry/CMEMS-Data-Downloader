import logging
import os
import tempfile
import time
import platform
import webbrowser
import shutil
import subprocess
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from ui._version import _downloader_version, _eclipse_version, _py_version, _qt_version
from functions.material_functions import info_button_text, object_init, dataset_data_information
from functions.gui_functions import activate_type_cb, activate_source_cb
from functions.window_functions import MyAbout, MyOptions, MyInfo, MyApi
from ui.Ui_mainwindow import Ui_MainWindow
from functions.thread_functions import CMEMSDataDownloadThread


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, path, config_dict, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.config_dict = config_dict
        self.config_path = path
        logging.info('mainwindow.py - UI initialization ...')
        self.setupUi(self)
        object_init(self)
        info_button_text(self)
        dataset_data_information(self)
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.main_cb_1.setItemDelegate(itemDelegate)
        self.main_cb_2.setItemDelegate(itemDelegate)
        self.main_cb_3.setItemDelegate(itemDelegate)
        self.main_cb_4.setItemDelegate(itemDelegate)
        self.main_cb_5.setItemDelegate(itemDelegate)
        self.main_cb_2.setEnabled(False)
        self.main_cb_3.setEnabled(False)
        self.main_cb_4.setEnabled(False)
        self.main_cb_5.setEnabled(False)
        self.main_cb_1.currentIndexChanged.connect(lambda: activate_type_cb(self))
        #self.download.clicked.connect(self.launch_query)
        self.api_information()
        self.check_file_folder()
        
        
    def launch_query(self):
        logging.info('mainwindow.py - launch_query')
        
        user = self.config_dict['CREDENTIALS'].get('user')
        password = self.config_dict['CREDENTIALS'].get('password')
        motu_url = self.config_dict['CREDENTIALS'].get('url')
        service = 'SEALEVEL_GLO_PHY_L3_REP_OBSERVATIONS_008_045-DGF'
        product = 'dataset-duacs-rep-global-alg-phy-l3'
        lon_min = '0'
        lon_max = '40'
        lat_min = '0'
        lat_max = '40'
        date_min = '2017-05-01T23:22:15'
        date_max = '2017-05-10T23:42:03'
        variable = 'sla'
        folder = self.config_dict['CREDENTIALS'].get('folder') + '\\'
        filename = 'test'
        output = 'netcdf'
        
        auth_query = {'product':product,
                      'service':service,
                      'scriptVersion':'1.5.00',
                      'mode':'status',
                      'action':'productdownload',
                      'output':output,
                      't_lo':date_min,
                      't_hi':date_max,
                      'x_lo':lon_min,
                      'x_hi':lon_max,
                      'y_lo':lat_min,
                      'y_hi':lat_max
                      }
        
        
        
        self.test = CMEMSDataDownloadThread(auth_query, motu_url, user, password, folder, filename)
        self.test.start()
        
        
    
    @QtCore.pyqtSlot()
    def on_actionExit_triggered(self):
        self.close()
    
    @QtCore.pyqtSlot()
    def on_actionSave_triggered(self):
        self.save_document()
    
    @QtCore.pyqtSlot()
    def on_actionOpen_triggered(self):
        self.open_document()
    
    @QtCore.pyqtSlot()
    def on_actionExpert_triggered(self):
        self.open_expert_mode()
    
    @QtCore.pyqtSlot()
    def on_actionAbout_triggered(self):
        self.open_about()
        
    @QtCore.pyqtSlot()
    def on_actionOptions_triggered(self):
        self.open_options()
    
    @QtCore.pyqtSlot()
    def on_actionUpdate_triggered(self):
        self.download_and_install_downloader_update()
    
    def save_document(self):
        print('no function yet')
        
    def open_document(self):
        print('no function yet')
        
    def open_expert_mode(self):
        print('no function yet')
        
    def open_about(self):
        logging.debug('mainwindow.py - open_about')
        text = ("The CMEMS Data Downloader v" + _downloader_version + " was developed by Olivier Henry"
                + ", using Eclipse " + _eclipse_version + ", Python " + _py_version + " and PyQt "
                + _qt_version + ". It was designed to help researchers to download data from CMEMS dif"
                + "ferent datasets by using the official CLS Motu API.")
        self.aboutWindow = MyAbout(text)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.aboutWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.aboutWindow.setGeometry(x2, y2, w2, h2)
        self.aboutWindow.setMinimumSize(QtCore.QSize(850, 450))
        self.aboutWindow.setMaximumSize(QtCore.QSize(850, 450))
        self.aboutWindow.exec_()
        
    def open_options(self):
        logging.debug('mainwindow.py - open_options')
        self.optionWindow = MyOptions(self.config_dict, self.info_button_text_dict)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.optionWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.optionWindow.setGeometry(x2, y2, w2, h2)
        self.optionWindow.exec_()
        if not self.optionWindow.cancel:
            self.config_dict = self.optionWindow.config_dict
            with open(os.path.join(self.config_path, 'cmems_downloader.ini'), 'w') as config_file:
                self.config_dict.write(config_file)
            logging.getLogger().setLevel(self.config_dict.get('LOG', 'level'))
            #self.check_downloader_update()
        
    def download_and_install_downloader_update(self):
        print('no function yet')
        
    def api_information(self):
        logging.debug('mainwindow.py - api_information')
        if self.config_dict['OPTIONS'].getboolean('display_api_info'):
            self.apiWindow = MyApi()
            _, _, w, h = QtWidgets.QDesktopWidget().screenGeometry(-1).getRect()
            _, _, w2, h2 = self.apiWindow.geometry().getRect()
            self.apiWindow.setGeometry(w/2 - w2/2, h/2 - h2/2, w2, h2)
            self.apiWindow.setMinimumSize(QtCore.QSize(700, 550))
            self.apiWindow.setMaximumSize(QtCore.QSize(700, 550))
            self.apiWindow.exec_()
            if self.apiWindow.checkbox.isChecked():
                if not self.config_dict['OPTIONS'].getboolean('display_api_info'):
                    self.config_dict.set('OPTIONS', 'display_api_info', 'True')
                    with open(os.path.join(self.config_path, 'cmems_downloader.ini'), 'w') as config_file:
                        self.config_dict.write(config_file)
            else:
                if self.config_dict['OPTIONS'].getboolean('display_api_info'):
                    self.config_dict.set('OPTIONS', 'display_api_info', 'False')
                    with open(os.path.join(self.config_path, 'cmems_downloader.ini'), 'w') as config_file:
                        self.config_dict.write(config_file)
    
    def check_file_folder(self):
        logging.debug('mainwindow.py - check_file_folder')
        if not os.path.isdir(self.config_dict.get('CREDENTIALS', 'folder')) and self.config_dict.get('CREDENTIALS', 'folder'):
            logging.exception('mainwindow.py - check_file_folder - exception occured when EDD checked the existence of the ECMWF file folder. '
                              + 'Please check that the folder exists. The folder option in the config file is going to be modified to the defa'
                              + 'ult folder.')
            self.config_dict.set('CREDENTIALS', 'folder', '')
            with open(os.path.join(self.config_path, 'ecmwf_downloader.ini'), 'w') as config_file:
                        self.config_dict.write(config_file)
            text = ('EDD has detected that the folder where ECMWF files are saved doesn\'t exist anymore. It has been reseted in the config file'
                    + ' to the default folder. Please check your options and set a new folder for ECMWF files.')
            self.infoWindow = MyInfo(text)
            _, _, w, h = QtWidgets.QDesktopWidget().screenGeometry(-1).getRect()
            _, _, w2, h2 = self.infoWindow.geometry().getRect()
            self.infoWindow.setGeometry(w/2 - w2/2, h/2 - h2/2, 450, self.infoWindow.sizeHint().height())
            self.infoWindow.setMinimumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
            self.infoWindow.setMaximumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
            self.infoWindow.exec_()