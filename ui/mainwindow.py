import logging
import os
import tempfile
import time
import platform
import webbrowser
import shutil
import subprocess
import sys
import ast
from PyQt5 import QtCore, QtWidgets, QtGui
from ui._version import _downloader_version, _eclipse_version, _py_version, _qt_version
from functions.material_functions import info_button_text, object_init, dataset_data_information
from functions.gui_functions import activate_type_cb, activate_source_cb
from functions.window_functions import MyAbout, MyOptions, MyInfo, MyApi, MyWarningUpdate, MyUpdate, MyProduct, MyQuery, MyWarning, MySelect, MySuccess
from functions.window_functions import MyCredentials, MyExpert, MyDatabaseUpdate
from functions.xml_functions import save_xml_query, open_xml_query
from ui.Ui_mainwindow import Ui_MainWindow
from functions.thread_functions import CMEMSDataDownloadThread, CheckCMEMSDownloaderOnline, CheckDatabaseVersion


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
        self.main_cb_6.setItemDelegate(itemDelegate)
        self.main_cb_7.setItemDelegate(itemDelegate)
        self.main_cb_8.setItemDelegate(itemDelegate)
        self.productdownload.clicked.connect(lambda: self.launch_query())
        self.getSize.clicked.connect(lambda: self.launch_query())
        self.api_information()
        self.check_downloader_update()
        self.check_file_folder()
        self.prepare_datasets_database()
        self.main_cb_1.currentIndexChanged.connect(lambda: activate_type_cb(self))
        self.product_info_button.clicked.connect(self.product_information)
        self.main_cb_6.currentIndexChanged.connect(self.set_modified)
        self.main_cb_7.currentIndexChanged.connect(self.set_modified)
        self.main_cb_8.currentIndexChanged.connect(self.set_modified)
        self.space_ln_north.textChanged.connect(self.set_modified)
        self.space_ln_south.textChanged.connect(self.set_modified)
        self.space_ln_west.textChanged.connect(self.set_modified)
        self.space_ln_east.textChanged.connect(self.set_modified)
        self.main_ln_1.textChanged.connect(self.set_modified)
        self.main_de_1.dateChanged.connect(self.set_modified)
        self.main_de_2.dateChanged.connect(self.set_modified)
        self.make_window_title()
        logging.info('mainwindow.py - UI initialized ...')
        logging.info('*****************************************')
    
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
        self.download_and_install_update()
    
    def save_document(self):
        logging.debug('mainwindow.py - save_document')
        filename = self.get_file_name('save')
        if filename:
            save_xml_query(self, filename)
        
    def open_document(self):
        logging.debug('mainwindow.py - open_document')
        if self.modified:
            result = self.save_warning_window("Open")
            if result == "save_button":
                self.save_document()
                filename = self.get_file_name('open')
                if filename:
                    open_xml_query(self, filename)
            elif result == "nosave_button":
                filename = self.get_file_name('open')
                if filename:
                    open_xml_query(self, filename)
        else:
            filename = self.get_file_name('open')
            if filename:
                open_xml_query(self, filename)
        
    def open_expert_mode(self):
        logging.debug('mainwindow.py - open_expert_mode')
        self.expertWindow = MyExpert(self.info_button_text_dict)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.expertWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.expertWindow.setGeometry(x2, y2, w2, h2)
        self.expertWindow.exec_()
        query, filename = self.expertWindow.query, self.expertWindow.filename
        if query and filename:
            self.launch_query(query, filename)
        
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
            self.check_downloader_update()
        
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
            text = ('CDD has detected that the folder where ECMWF files are saved doesn\'t exist anymore. It has been reseted in the config file'
                    + ' to the default folder. Please check your options and set a new folder for ECMWF files.')
            self.infoWindow = MyInfo(text)
            _, _, w, h = QtWidgets.QDesktopWidget().screenGeometry(-1).getRect()
            _, _, w2, h2 = self.infoWindow.geometry().getRect()
            self.infoWindow.setGeometry(w/2 - w2/2, h/2 - h2/2, 450, self.infoWindow.sizeHint().height())
            self.infoWindow.setMinimumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
            self.infoWindow.setMaximumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
            self.infoWindow.exec_()
            
    def prepare_datasets_database(self):
        logging.debug('mainwindow.py - prepare_datasets_database')
        database_path = 'database/'
        try:
            if os.path.isdir(database_path):
                self.product_database, self.dataset_database = {}, {}
                for file in os.listdir(database_path):
                    if os.path.isfile(os.path.join(database_path, file)) and file[-4:] == '.dat' and file != 'PRODUCT_DATABASE.dat':
                        domain, data_type, source, mode, product, short_description, description, resolution = None, None, None, None, None, None, None, None
                        temporal_resolution, level, data_type, vertical, temporal, production, image, variables = None, None, None, None, None, None, None, None
                        subset, swath, suffix = None, None, None
                        name = file[:-4]
                        f = open(database_path + file, 'r', encoding='utf-8')
                        for line in f:
                            if line[:3] != '###':
                                index = line.find('=')
                                parameter = line[:index]
                                value = line[index+1:].replace('\n','')
                                if parameter != 'version' and parameter != 'creation_date':
                                    if parameter == 'server_url':
                                        server_url = value
                                    if parameter == 'ftp_url':
                                        ftp_url = value
                                    if parameter == 'domain':
                                        domain = value
                                    if parameter == 'type':
                                        data_type = value
                                    if parameter == 'source':
                                        source = value
                                    if parameter == 'mode':
                                        mode = value
                                    if parameter == 'product':
                                        product = value
                                    if parameter == 'short_description':
                                        short_description = value
                                    if parameter == 'description':
                                        description = value
                                    if parameter == 'resolution':
                                        resolution = value
                                    if parameter == 'temporal_resolution':
                                        temporal_resolution = value
                                    if parameter == 'level':
                                        level = value
                                    if parameter == 'dataset_type':
                                        dataset_type = value
                                    if parameter == 'vertical':
                                        vertical = value
                                    if parameter == 'swath_vertical':
                                        swath_vertical_tmp = value
                                        if swath_vertical_tmp == 'None':
                                            swath_vertical = None
                                        else:
                                            swath_vertical = []
                                            if '|' in swath_vertical_tmp:
                                                swath_vertical_tmp = swath_vertical_tmp.split('|')
                                                for swath in swath_vertical_tmp:
                                                    if 'to' in swath:
                                                        index = swath.find('to')
                                                        start = swath[:index].split('/')
                                                        end = swath[index+2:].split('/')
                                                        swath_vertical.append([start, end])
                                                    else:
                                                        swath_vertical.append([swath, swath])
                                            else:
                                                index = swath_vertical_tmp.find('to')
                                                start = swath_vertical_tmp[:index].split('/')
                                                end = swath_vertical_tmp[index+2:].split('/')
                                                swath_vertical.append([start, end])
                                    if parameter == 'temporal':
                                        temporal = value
                                    if parameter == 'production':
                                        production = value
                                    if parameter == 'image':
                                        image = value
                                    if parameter == 'variables':
                                        variables = value
                                        if variables == 'None':
                                            variables = None
                                        else:
                                            if '|' in variables:
                                                variables = variables.split('|')
                                                for index, var in enumerate(variables):
                                                    if ','in var:
                                                        var = var.split(',')
                                                    else:
                                                        var = [var]
                                                    variables[index] = sorted(var)
                                            elif ',' in variables:
                                                variables = sorted(variables.split(','))
                                            else:
                                                variables = [variables]
                                    if parameter == 'swath':
                                        swath = value
                                        if ',' in swath:
                                            swath = swath.split(',')
                                    if parameter == 'swath_temporal':
                                        swath_temporal = value
                                        if ',' in swath_temporal:
                                            swath_temporal = swath_temporal.split(',')
                                    if parameter == 'swath_temporal_resolution':
                                        swath_temporal_resolution = value
                                        if ',' in swath_temporal_resolution:
                                            swath_temporal_resolution = swath_temporal_resolution.split(',')
                                    if parameter == 'suffix':
                                        suffix = value
                        f.close()
                        try:
                            self.dataset_database[domain]
                        except KeyError:
                            self.dataset_database[domain] = {}
                        try:
                            self.dataset_database[domain][data_type]
                        except KeyError:
                            self.dataset_database[domain][data_type] = {}
                        try:
                            self.dataset_database[domain][data_type][source]
                        except KeyError:
                            self.dataset_database[domain][data_type][source] = {}
                        try:
                            self.dataset_database[domain][data_type][source][mode]
                        except KeyError:
                            self.dataset_database[domain][data_type][source][mode] = []
                        self.dataset_database[domain][data_type][source][mode].append(product)
                        try:
                            self.product_database[product]
                        except KeyError:
                            self.product_database[product] = {}
                        self.product_database[product]['information'] = {'short_description':short_description,
                                                                            'description':description,
                                                                            'spatial_resolution':resolution,
                                                                            'temporal_resolution':temporal_resolution,
                                                                            'level':level,
                                                                            'product_type':dataset_type,
                                                                            'vertical_coverage':vertical,
                                                                            'temporal_coverage':temporal,
                                                                            'production':production,
                                                                            'image':image}
                        self.product_database[product]['variables'] = variables
                        self.product_database[product]['swath'] = swath
                        self.product_database[product]['swath_temporal'] = swath_temporal
                        self.product_database[product]['swath_vertical'] = swath_vertical
                        self.product_database[product]['suffix'] = suffix
                        self.product_database[product]['tree'] = [domain, data_type, source, mode]
                        self.product_database[product]['server_url'] = server_url
                        self.product_database[product]['ftp_url'] = ftp_url
                domain_list = []
                for key, _ in self.dataset_database.items():
                    domain_list.append(key)
                self.main_cb_1.clear()
                self.main_cb_1.addItem('Make a choice...')
                self.main_cb_1.addItems(sorted(domain_list))
                logging.debug('mainwindow.py - prepare_datasets_database - database ready')
        except Exception:
            logging.exception('An exception occured during the reading of the .dat files')
    
    def product_information(self):
        logging.debug('mainwindow.py - product_information')
        if self.main_cb_5.currentText() != 'Make a choice...' and self.main_cb_5.currentText() != 'No product available...':
            self.productWindow = MyProduct(self.main_cb_5.currentText(), self.product_database[self.main_cb_5.currentText()])
            x1, y1, w1, h1 = self.geometry().getRect()
            _, _, w2, h2 = self.productWindow.geometry().getRect()
            x2 = x1 + w1/2 - w2/2
            y2 = y1 + h1/2 - h2/2
            self.productWindow.setGeometry(x2, y2, w2, h2)
            self.productWindow.exec_()
    
    def launch_query(self, query=None, filename=None):
        logging.info('mainwindow.py - launch_query')
        if query is None and filename is None:
            product, dataset, variable = self.check_product_dataset()
            if product and dataset and variable:
                user = self.config_dict['CREDENTIALS'].get('user')
                password = self.config_dict['CREDENTIALS'].get('password')
                if not user or not password:
                    self.credentialsyWindow = MyCredentials(user, password)
                    x1, y1, w1, h1 = self.geometry().getRect()
                    _, _, w2, h2 = self.credentialsyWindow.geometry().getRect()
                    x2 = x1 + w1/2 - w2/2
                    y2 = y1 + h1/2 - h2/2
                    self.credentialsyWindow.setGeometry(x2, y2, w2, h2)
                    self.credentialsyWindow.exec_()
                    if self.credentialsyWindow.username and self.credentialsyWindow.password:
                        user = self.credentialsyWindow.username
                        password = self.credentialsyWindow.password
                if user and password:
                    query, motu_url, folder, filename = self.prepare_query() 
                    query['action'] = str(self.sender().objectName())
                    self.queryWindow = MyQuery(query, motu_url, user, password, folder, filename)
                    x1, y1, w1, h1 = self.geometry().getRect()
                    _, _, w2, h2 = self.queryWindow.geometry().getRect()
                    x2 = x1 + w1/2 - w2/2
                    y2 = y1 + h1/2 - h2/2
                    self.queryWindow.setGeometry(x2, y2, w2, h2)
                    self.queryWindow.exec_()
                    try:
                        download_time = self.queryWindow.download_time
                        file_path = self.queryWindow.file_path
                        average_speed = self.queryWindow.average_speed
                        self.successWindow = MySuccess(download_time, file_path, average_speed)
                        x1, y1, w1, h1 = self.geometry().getRect()
                        _, _, w2, h2 = self.successWindow.geometry().getRect()
                        x2 = x1 + w1/2 - w2/2
                        y2 = y1 + h1/2 - h2/2
                        self.successWindow.setGeometry(x2, y2, w2, h2)
                        self.successWindow.exec_()
                    except AttributeError:
                        pass
            else:
                if not product:
                    self.main_lb_5.setStyleSheet("color: rgb(200,0,0);")
                    self.tabWidget.tabBar().setTabTextColor(0, QtGui.QColor(200,0,0))
                if not dataset:
                    self.main_lb_8.setStyleSheet("color: rgb(200,0,0);")
                    self.tabWidget.tabBar().setTabTextColor(1, QtGui.QColor(200,0,0))
                if not variable:
                    self.main_lb_10.setStyleSheet("color: rgb(200,0,0);")
                    self.tabWidget.tabBar().setTabTextColor(1, QtGui.QColor(200,0,0))
                self.selectionWindow = MySelect()
                x1, y1, w1, h1 = self.geometry().getRect()
                _, _, w2, h2 = self.selectionWindow.geometry().getRect()
                self.selectionWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
                self.selectionWindow.setMinimumSize(QtCore.QSize(500, self.selectionWindow.sizeHint().height()))
                self.selectionWindow.setMaximumSize(QtCore.QSize(500, self.selectionWindow.sizeHint().height()))
                self.selectionWindow.exec_()
        else:
            user = self.config_dict['CREDENTIALS'].get('user')
            password = self.config_dict['CREDENTIALS'].get('password')
            if not user or not password:
                self.credentialsyWindow = MyCredentials(user, password)
                x1, y1, w1, h1 = self.geometry().getRect()
                _, _, w2, h2 = self.credentialsyWindow.geometry().getRect()
                x2 = x1 + w1/2 - w2/2
                y2 = y1 + h1/2 - h2/2
                self.credentialsyWindow.setGeometry(x2, y2, w2, h2)
                self.credentialsyWindow.exec_()
                if self.credentialsyWindow.username and self.credentialsyWindow.password:
                    user = self.credentialsyWindow.username
                    password = self.credentialsyWindow.password
            if user and password:
                folder = self.config_dict['CREDENTIALS'].get('folder')
                motu_url = self.config_dict['CREDENTIALS'].get('url')
                
                print(query)
                
                query['action'] = 'productdownload'
                self.queryWindow = MyQuery(query, motu_url, user, password, folder, filename)
                x1, y1, w1, h1 = self.geometry().getRect()
                _, _, w2, h2 = self.queryWindow.geometry().getRect()
                x2 = x1 + w1/2 - w2/2
                y2 = y1 + h1/2 - h2/2
                self.queryWindow.setGeometry(x2, y2, w2, h2)
                self.queryWindow.exec_()
                try:
                    download_time = self.queryWindow.download_time
                    file_path = self.queryWindow.file_path
                    average_speed = self.queryWindow.average_speed
                    self.successWindow = MySuccess(download_time, file_path, average_speed)
                    x1, y1, w1, h1 = self.geometry().getRect()
                    _, _, w2, h2 = self.successWindow.geometry().getRect()
                    x2 = x1 + w1/2 - w2/2
                    y2 = y1 + h1/2 - h2/2
                    self.successWindow.setGeometry(x2, y2, w2, h2)
                    self.successWindow.exec_()
                except AttributeError:
                    pass
    
    def check_downloader_update(self):
        logging.debug('mainwindow.py - check_downloader_update')
        self.actionUpdate.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/cmems_data_downloader_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpdate.setIcon(icon)
        self.actionUpdate.setToolTip('')
        
        if self.config_dict['OPTIONS'].getboolean('check_update'):
            self.check_downloader = CheckCMEMSDownloaderOnline()
            self.check_downloader.start()
            self.check_downloader.finished.connect(self.parse_downloader_update)
        else:
            logging.info('mainwindow.py - check_downloader_update - from options, no update check')
                    
    def parse_downloader_update(self, val):
        logging.debug('mainwindow.py - parse_downloader_update - val ' + str(val))
        if val == 'no new version':
            if self.config_dict['OPTIONS'].getboolean('check_database'):
                self.check_database = CheckDatabaseVersion()
                self.check_database.start()
                self.check_database.finished.connect(self.parse_database_update)
            else:
                self.actionUpdate.setEnabled(False)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("icons/cmems_data_downloader_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.actionUpdate.setIcon(icon)
                self.actionUpdate.setToolTip('No update available !')
        elif 'http' in val:
            self.actionUpdate.setEnabled(True)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/cmems_data_downloader_update_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionUpdate.setIcon(icon)
            if getattr(sys, 'frozen', False ) :
                self.actionUpdate.setToolTip('A new update is available for CMEMS Data Downloader ! Click here to install it automatically.')
            else:
                self.actionUpdate.setToolTip('A new update is available for CMEMS Data Downloader ! Click here to download it.')
            self.link_latest_version = val
    
    def download_and_install_update(self):
        logging.debug('mainwindow.py - download_and_install_update - link_latest_version ' + str(self.link_latest_version))
        if self.link_latest_version:
            if isinstance(self.link_latest_version, dict):
                self.downloadWindow = MyDatabaseUpdate(self.link_latest_version)
                x1, y1, w1, h1 = self.geometry().getRect()
                _, _, w2, h2 = self.downloadWindow.geometry().getRect()
                x2 = x1 + w1/2 - w2/2
                y2 = y1 + h1/2 - h2/2
                self.downloadWindow.setGeometry(x2, y2, w2, h2)
                self.downloadWindow.setMinimumSize(QtCore.QSize(500, self.downloadWindow.sizeHint().height()))
                self.downloadWindow.setMaximumSize(QtCore.QSize(500, self.downloadWindow.sizeHint().height()))
                self.downloadWindow.exec_()
                if self.downloadWindow.done:
                    self.prepare_datasets_database()
                    self.actionUpdate.setEnabled(False)
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("icons/cmems_data_downloader_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.actionUpdate.setIcon(icon)
                    self.actionUpdate.setToolTip('')
            else:
                frozen = False
                height = 250
                if getattr(sys, 'frozen', False) :
                    frozen = True
                    height = 200
                self.updateWindow = MyWarningUpdate(frozen)
                x1, y1, w1, h1 = self.geometry().getRect()
                _, _, w2, h2 = self.updateWindow.geometry().getRect()
                x2 = x1 + w1/2 - w2/2
                y2 = y1 + h1/2 - h2/2
                self.updateWindow.setGeometry(x2, y2, w2, h2)
                self.updateWindow.setMinimumSize(QtCore.QSize(600, height))
                self.updateWindow.setMaximumSize(QtCore.QSize(600, height))
                self.updateWindow.exec_()
                try:
                    if self.updateWindow.buttonName == 'update_button':
                        if getattr(sys, 'frozen', False) :
                            temp_folder = tempfile.gettempdir()
                        else:
                            temp_folder = os.path.expanduser("~")+"/Downloads/"
                        self.downloadWindow = MyUpdate(self.link_latest_version, temp_folder)
                        x1, y1, w1, h1 = self.geometry().getRect()
                        _, _, w2, h2 = self.downloadWindow.geometry().getRect()
                        x2 = x1 + w1/2 - w2/2
                        y2 = y1 + h1/2 - h2/2
                        self.downloadWindow.setGeometry(x2, y2, w2, h2)
                        self.downloadWindow.setMinimumSize(QtCore.QSize(500, self.downloadWindow.sizeHint().height()))
                        self.downloadWindow.setMaximumSize(QtCore.QSize(500, self.downloadWindow.sizeHint().height()))
                        self.downloadWindow.exec_()
                        logging.debug('mainwindow.py - download_and_install_downloader_update - download finished')
                        if not self.downloadWindow.cancel:
                            if getattr(sys, 'frozen', False) :
                                filename = self.link_latest_version[self.link_latest_version.rfind('/')+1:]
                                if platform.system() == 'Windows':
                                    os.startfile(temp_folder + '\\' + filename)
                                    time.sleep(0.1)
                                    self.close()
                                elif platform.system() == 'Linux':
                                    shutil.copy('functions/unzip_update.py', temp_folder)
                                    install_folder = self.config_path + '/'
                                    command = 'python3 ' + temp_folder + '/unzip_update.py ' + temp_folder + '/' + filename + ' ' + install_folder
                                    os.system('x-terminal-emulator -e ' + command)
                                    time.sleep(0.1)
                                    self.close()
                            else:
                                time.sleep(0.1)
                                self.close()
                except AttributeError:
                    pass
    
    def parse_database_update(self, val):
        if val:
            self.actionUpdate.setEnabled(True)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/cmems_data_downloader_update_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionUpdate.setIcon(icon)
            self.actionUpdate.setToolTip('New products are available for the product database. Click here to download them automatically.')
            self.link_latest_version = val
    
    def get_file_name(self, action):
        logging.debug('mainwindow.py - get_file_name')
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setDefaultSuffix('xml')
        if action == 'save':
            file_name, _ = file_dialog.getSaveFileName(self, 'Save XML File', '', filter='XML Files (*.xml)')
        elif action == 'open':
            file_name, _ = file_dialog.getOpenFileName(self, 'Open XML File', '', filter='XML Files (*.xml)')
        logging.debug('mainwindow.py - get_file_name - file_name ' + file_name)
        return file_name
    
    def set_modified(self):
        logging.debug('mainwindow.py - set_modified')
        if not self.modified:
            self.modified = True
            self.make_window_title()
    
    def make_window_title(self):
        logging.debug('mainwindow.py - make_window_title - self.modified ' + str(self.modified))
        title_string = 'CMEMS Data Downloader v' + _downloader_version
        modified_string = ''
        if self.modified:
            modified_string = ' - modified'
        title_string = title_string + modified_string
        self.setWindowTitle(title_string)
    
    def save_warning_window(self, string):
        logging.debug('mainwindow.py - save_warning_window')
        self.presaveWindow = MyWarning(string)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.presaveWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.presaveWindow.setGeometry(x2, y2, w2, h2)
        self.presaveWindow.setMinimumSize(QtCore.QSize(500, self.presaveWindow.sizeHint().height()))
        self.presaveWindow.setMaximumSize(QtCore.QSize(500, self.presaveWindow.sizeHint().height()))
        self.presaveWindow.exec_()
        return self.presaveWindow.buttonName

    def closeEvent(self, event):
        logging.debug('mainwindow.py - closeEvent - self.modified ' + str(self.modified))
        if self.modified:
            result = self.save_warning_window("Close")
            if result == "save_button":
                self.save_document()
                logging.info('CMEMS Data Downloader ' + _downloader_version + ' is closing ...')
                self.close()
            elif result == "nosave_button":
                logging.info('CMEMS Data Downloader ' + _downloader_version + ' is closing ...')
                self.close()
            else:
                event.ignore()
        else:
            logging.info('CMEMS Data Downloader ' + _downloader_version + ' is closing ...')
            self.close()
    
    def check_product_dataset(self):
        logging.debug('mainwindow.py - check_product_dataset')
        product, dataset, variable = True, True, False
        if self.main_cb_5.currentText() == 'Make a choice...' or self.main_cb_5.currentText() == 'No product available...':
            product = False
        if self.main_cb_6.currentText() == 'Make a choice...' or self.main_cb_6.currentText() == 'No product selected...':
            dataset = False
        if self.variables_cb:
            for cb in self.variables_cb:
                if cb.isChecked():
                    variable = True
        else:
            if self.variables_vertical_layout.count() == 0:
                variable = False
            else:
                variable = True
        return product, dataset, variable
    
    def prepare_query(self):
        logging.debug('mainwindow.py - prepare_query')
        query = {}
        motu_url, service, product, var, folder, filename, output = None, None, None, None, None, None, None
        lon_min, lon_max, lat_min, lat_max, date_min, date_max, depth_min, depth_max = None, None, None, None, None, None, None, None
        
        ### service
        service = str(self.main_cb_5.currentText()) + self.product_database[self.main_cb_5.currentText()]['suffix']
        
        ### product
        product = str(self.main_cb_6.currentText())
        
        ### url
        motu_url = self.product_database[self.main_cb_5.currentText()]['server_url']

        ### longitude and latitude
        if self.space_ln_north.text():
            lat_max = self.space_ln_north.text()
        if self.space_ln_south.text():
            lat_min = self.space_ln_south.text()
        if self.space_ln_west.text():
            lon_min = self.space_ln_west.text()
        if self.space_ln_east.text():
            lon_max = self.space_ln_east.text()
        
        ### depth
        if self.main_cb_7.isEnabled():
            if self.main_cb_7.currentText() != 'Make a choice...' and self.main_cb_8.currentText() != 'Make a choice...':
                depth_min, depth_max = self.main_cb_7.currentText(), self.main_cb_8.currentText()
        
        ### date
        date_min = self.main_de_1.date().toString(QtCore.Qt.ISODate)
        date_max = self.main_de_2.date().toString(QtCore.Qt.ISODate)
        
        # filename and folder
        filename = str(self.main_ln_1.text())
        folder = self.config_dict['CREDENTIALS'].get('folder')
        
        # variables
        var_tmp = []
        var_names = {v: k for k, v in self.variables_name.items()}
        checked_count = 0
        if self.variables_cb:
            for cb in self.variables_cb:
                if cb.isChecked():
                    checked_count +=1
                    var_tmp.append(var_names[cb.text()[:cb.text().find('(') - 1]])
        if var_tmp:
            if len(self.variables_cb) != checked_count:
                var = var_tmp
        
        # prepare dictionary
        parameter_list = [service, product, lon_min, lon_max, lat_min, lat_max, 
                          date_min, date_max, depth_min, depth_max, var, output]
        name_list = ['service', 'product', 'x_lo', 'x_hi', 'y_lo', 'y_hi', 
                          't_lo', 't_hi','z_lo', 'z_hi', 'variable', 'output']
        for index, parameter in enumerate(parameter_list):
            if parameter != None:
                query[name_list[index]] = parameter
        query['scriptVersion'] = '1.5.00'
        query['mode'] = 'status'
        
        logging.debug('mainwindow.py - prepare_query - query ready: ' + str(query))
        return query, motu_url, folder, filename
    
    
    
    ### snippet to read a file on github
    def check_database(self):
        import requests
        import base64
        import json
        url = 'https://api.github.com/repos/olivierpascalhenry/CMEMS-Data-Downloader/contents/database/PRODUCT_DATABASE.dat'
        test_json = requests.get(url=url).json()
        text = test_json['content']
    
        product_database = json.loads(base64.b64decode(text).decode('utf-8'))
        
        
        print(product_database)
        
        
    