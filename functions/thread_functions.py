import logging
import requests
import time
import json
import os
import platform
import sys
import re
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import parse_qs, urlparse

import urllib

from hurry.filesize import size, alternative
from PyQt5 import QtCore, Qt
from distutils.version import LooseVersion
from ui._version import _downloader_version
from PyQt5 import QtWidgets
from datetime import datetime
from xml.dom import minidom

        
class CheckCMEMSDownloaderOnline(Qt.QThread):
    finished = QtCore.pyqtSignal(str)
    
    def __init__(self):
        Qt.QThread.__init__(self)
        logging.debug('thread_functions.py - CheckCMEMSDownloaderOnline - __init__')
    
    def run(self):
        logging.debug('thread_functions.py - CheckCMEMSDownloaderOnline - run')
        url = 'https://api.github.com/repos/olivierpascalhenry/CMEMS-Data-Downloader/releases/latest'
        try:
            json_object = requests.get(url=url).json()
            format = ''
            if getattr(sys, 'frozen', False) :
                if platform.system() == 'Windows':
                    format = '.msi'
                elif platform.system() == 'Linux':
                    format = '.tar.gz'
            else:
                format = 'sources.zip'
                
            if LooseVersion(_downloader_version) < LooseVersion(json_object['tag_name']):
                assets = json_object['assets']
                download_url = 'no new version'
                for asset in assets:
                    link = asset['browser_download_url']
                    if format in link:
                        download_url = link  
                self.finished.emit(download_url)
            else:
                self.finished.emit('no new version')
        except Exception:
            logging.exception('thread_functions.py - CheckCMEMSDownloaderOnline - run - internet connection error - url ' + url)
    
    def stop(self):
        self.terminate()
        
        
class DownloadFile(Qt.QThread):
    download_update = QtCore.pyqtSignal(list)
    download_done = QtCore.pyqtSignal()
    download_failed = QtCore.pyqtSignal()
    
    def __init__(self, url_name, update_file=None):
        Qt.QThread.__init__(self)
        logging.debug('thread_functions.py - DownloadFile - __init__ - url_name ' + str(url_name)
                      + ' ; update_file ' + str(update_file))
        self.url_name = url_name
        self.update_file = update_file
        self.filename = self.url_name[self.url_name.rfind("/")+1:]
        self.cancel = False
        
    def run(self):
        logging.debug('thread_functions.py - DownloadFile - run - download started')
        if len(self.filename) > 35:
            if platform.system() == 'Windows':
                self.filename = self.filename[:21] + '[...]' + self.filename[-4:]
            elif platform.system() == 'Linux':
                self.filename = self.filename[:21] + '[...]' + self.filename[-7:]
            
        self.download_update.emit([0, 'Downloading %s...' % self.filename])
        opened_file = open(self.update_file, 'wb')
        try:
            opened_url = urlopen(self.url_name, timeout=10)
            totalFileSize = int(opened_url.info()['Content-Length'])
            bufferSize = 9192
            fileSize = 0
            start = time.time()
            while True:
                if self.cancel:
                    opened_file.close()
                    break
                buffer = opened_url.read(bufferSize)
                if not buffer:
                    break
                fileSize += len(buffer)
                opened_file.write(buffer)
                download_speed = self._set_size(fileSize/(time.time() - start)) + '/s'
                self.download_update.emit([round(fileSize * 100 / totalFileSize), 'Downloading %s at %s' % (self.filename, download_speed)])
            opened_file.close()
            if not self.cancel:
                logging.debug('thread_functions.py - DownloadFile - run - download finished')
                self.download_done.emit()
            else:
                logging.debug('thread_functions.py - DownloadFile - run - download canceled')
        except Exception:
            logging.exception('thread_functions.py - DownloadFile - run - connexion issue ; self.url_name ' + self.url_name)
            opened_file.close()
            self.download_failed.emit()
    
    def _set_size(self, bytes):
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        i = 0
        while bytes >= 1024 and i < len(suffixes)-1:
            bytes /= 1024.
            i += 1
        f = ('%.2f' % bytes).rstrip('0').rstrip('.')
        return '%s %s' % (f, suffixes[i])
    
    def cancel_download(self):
        logging.debug('thread_functions.py - DownloadFile - cancel_download')
        self.cancel = True
    
    def stop(self):
        logging.debug('thread_functions.py - DownloadFile - stop')
        self.terminate()
        
        
class CMEMSDataDownloadThread(Qt.QThread):
    download_update = QtCore.pyqtSignal(dict)
    download_done = QtCore.pyqtSignal(dict)
    download_failed = QtCore.pyqtSignal(str)
    
    def __init__(self, query, motu_url, user, password, out_folder, out_filename):
        Qt.QThread.__init__(self)
        logging.debug('thread_functions.py - CMEMSDataDownloadThread - __init__')
        self.query = query
        self.motu_url = motu_url
        self.user = user
        self.password = password
        if platform.system() == 'Windows':
            self.out_folder = out_folder + '\\'
        else:
            self.out_folder = out_folder + '/'
        self.out_filename = out_filename
        self.headers = {'X-Client-Id': 'motu-client-python', 'X-Client-Version': '1.5.00'}
        self.error = ''
        self.cancel = False
        self.downloading = False
        self._prepare_url_and_variables()
    
    def run(self):
        logging.debug('thread_functions.py - CMEMSDataDownloadThread - run')
        try:
            self.download_update.emit({'browser_text':'Welcome to the MOTU API.<br>Authentication pending...<br>',
                                       'bar_text':'Authentication pending...',
                                       'progress':0})
            service_url = self._auth_connexion(self.auth_url)
            self.download_update.emit({'browser_text':'Authentication successfull.<br>Query is sent to the MOTU server.<br>',
                                       'bar_text':'Sending query...',
                                       'progress':0})
            id_res = requests.get(service_url, headers=self.headers)
            status = minidom.parseString(id_res.text).getElementsByTagName('statusModeResponse')[0].getAttribute('status')
            id = minidom.parseString(id_res.text).getElementsByTagName('statusModeResponse')[0].getAttribute('requestId')
            if status == "2":
                message = minidom.parseString(id_res.text).getElementsByTagName('statusModeResponse')[0].getAttribute('msg')
                status_url = None
                logging.exception('thread_functions.py - ECMWFDataDownloadThread - run - Exception ' + message)
                self.download_failed.emit(message)
            else:
                status_url = self.motu_url + '?action=getreqstatus&requestid=' + id + "&service=" + self.query['service'] + "&product=" + self.query['product']
            if status_url is not None:
                retry = 0
                while True:
                    service_url = self._auth_connexion(status_url)
                    status_res = requests.get(service_url, headers=self.headers)
                    for node in minidom.parseString(status_res.text).getElementsByTagName('statusModeResponse'):
                        status = node.getAttribute('status')    
                        download_url = node.getAttribute('remoteUri')
                        message = node.getAttribute('msg')
                    if status == "0" or status == "3":
                        if retry == 0:
                            self.download_update.emit({'browser_text':'Query has been accepted and is now queued.<br>',
                                                       'bar_text':'Query queued...',
                                                       'progress':0})
                        time.sleep(5)
                    else:
                        break
                    retry += 1
                if status == "2": 
                    logging.exception('thread_functions.py - ECMWFDataDownloadThread - run - Exception ' + message)
                    self.download_failed.emit(message)
                elif status == "1": 
                    text = 'The processing of the query is finished and the file is ready to be downloaded.<br>'
                    self.download_update.emit({'browser_text':text,
                                                'bar_text':'Ready to download...',
                                                'progress':0})
                    if '.zip' in download_url:
                        self.out_filename += '.zip'
                    elif '.nc' in download_url:
                        self.out_filename += '.nc'
                    final_res = requests.get(download_url, headers=self.headers, stream=True)
                    status_code = final_res.status_code
                    logging.debug('thread_functions.py - ECMWFDataDownloadThread - run - downloading - headers ' + str(final_res.headers))
                    with open(self.out_folder + self.out_filename, 'wb') as f:
                        start = time.time()
                        total_length = int(final_res.headers.get('content-length'))
                        downloaded = 0
                        self.download_update.emit({'browser_text':'Downloading...',
                                                           'bar_text':'Downloading...',
                                                           'progress':0})
                        self.download_update.emit({'browser_text':'Total size of the file: ' + self._set_size(total_length),
                                                           'bar_text':'Downloading...',
                                                           'progress':0})
                        self.downloading = True
                        download_start = datetime.now()
                        for chunk in final_res.iter_content(chunk_size=1024):
                            if self.cancel:
                                break
                            downloaded += len(chunk)
                            f.write(chunk)
                            try:
                                download_speed = self._set_size(downloaded / (time.time() - start)) + '/s'
                            except ZeroDivisionError:
                                download_speed = '0 KB/s'   
                            progress = round(downloaded * 100 / total_length)
                            bar_text = 'Downloading at ' + download_speed
                            self.download_update.emit({'browser_text':'',
                                                        'bar_text':bar_text,
                                                        'progress':progress})
                    f.close()
                    if self.cancel:
                        self.download_cancel.emit()
                        try:
                            os.remove(self.out_folder + self.out_filename)
                        except Exception:
                            logging.exception('thread_functions.py - ECMWFDataDownloadThread - run - Trying to remove aborted file')
                    else:
                        average_speed = self._set_size(total_length / (time.time() - start)) + '/s'
                        download_time = datetime.now() - download_start
                        final_dict = {'average_speed': average_speed,
                                      'file_path': self.out_folder + self.out_filename,
                                      'download_time': download_time}
                        self.download_done.emit(final_dict)
        except Exception:
            logging.exception('thread_functions.py - ECMWFDataDownloadThread - run - Exception')
            self.download_failed.emit('An exception occured during the processing and/or the download of the query. Please check the log to find '
                                      + 'more information about the exception.')
    
    def _set_size(self, bytes):
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        i = 0
        while bytes >= 1024 and i < len(suffixes)-1:
            bytes /= 1024.
            i += 1
        f = ('%.2f' % bytes).rstrip('0').rstrip('.')
        return '%s %s' % (f, suffixes[i])
    
    def _prepare_url_and_variables(self):
        self.auth_url = self.motu_url + '?'
        for key, value in self.query.items():
            if isinstance(value, list):
                for val in value:
                    self.auth_url += key + '=' + val + '&'
            else:
                self.auth_url += key + '=' + value + '&'
        self.auth_url = self.auth_url[:-1]
    
    def _auth_connexion(self, url):
        first_res = requests.get(url, headers=self.headers)
        cas_url = re.search('(.*)/login.*', first_res.url).group(1) + '/v1/tickets'
        payload = 'username=' + urllib.parse.quote(self.user, safe='') + '&password=' + urllib.parse.quote(self.password, safe='')
        auth_res = requests.post(cas_url, headers=self.headers, data=payload)
        if auth_res.status_code >= 400:
            if 'error.authentication.credentials.bad' in auth_res.text:
                logging.exception('thread_functions.py - ECMWFDataDownloadThread - _auth_connexion - Exception occured during authentication: '
                                  + 'wrong username and/or password.')
                self.download_failed.emit('Exception occured during authentication: wrong username and/or password.')
            else:
                logging.exception('thread_functions.py - ECMWFDataDownloadThread - _auth_connexion - Exception occured during authentication.')
                self.download_failed.emit('Exception occured during authentication.')
            raise Exception
        tgt_url = BeautifulSoup(auth_res.text, "html.parser").form['action']
        ticket_url = cas_url + '/' + tgt_url[tgt_url.rfind('/')+1:]
        redirect_service_url = urllib.parse.parse_qs(urllib.parse.urlparse(first_res.url).query, keep_blank_values=False)['service'][0]
        payload = 'service=' + urllib.parse.quote(redirect_service_url, safe='')
        ticket_res = requests.post(ticket_url, headers=self.headers, data=payload)
        return redirect_service_url + '&ticket=' + ticket_res.text
    
    def cancel_download(self):
        logging.debug('thread_functions.py - ECMWFDataDownloadThread - cancel_download')
        self.cancel = True
    
    def stop(self):
        logging.debug('thread_functions.py - ECMWFDataDownloadThread - stop')
        self.terminate()

