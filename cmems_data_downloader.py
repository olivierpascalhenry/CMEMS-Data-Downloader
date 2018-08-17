import logging
import os
import sys
import configparser
from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from ui.mainwindow import MainWindow
from ui._version import _downloader_version



def launch_data_downloader(path):
    app = QApplication(sys.argv)
    splash_pix = QPixmap('icons\cmems_data_downloader_icon.svg')
    splash = QSplashScreen(splash_pix)
    splash.setMask(splash_pix.mask())
    splash.show()
    config_dict = configparser.ConfigParser()
    if not os.path.exists(os.path.join(path, 'cmems_downloader.ini')):
        config_dict['LOG'] = {'level': 'INFO',
                              'path': ''
                              }
        config_dict['OPTIONS'] = {'language':'english',
                                  'check_update':'False',
                                  'check_database':'False',
                                  'display_api_info':'True'
                                  }
        config_dict['CREDENTIALS'] = {'password':'',
                                      'user':'',
                                      'folder':''
                                      }
        with open(os.path.join(path, 'cmems_downloader.ini'), 'w') as configfile:
            config_dict.write(configfile)
    config_dict.read(os.path.join(path, 'cmems_downloader.ini'))
    if not config_dict['OPTIONS'].get('check_database'):
        config_dict.set('OPTIONS', 'check_database', 'False')
        with open(os.path.join(path, 'cmems_downloader.ini'), 'w') as configfile:
            config_dict.write(configfile)
    if config_dict['CREDENTIALS'].get('url'):
        config_dict.remove_option('CREDENTIALS', 'url')
        with open(os.path.join(path, 'cmems_downloader.ini'), 'w') as configfile:
            config_dict.write(configfile)
    path_exist = True
    if not config_dict.get('LOG', 'path'):
        log_filename = os.path.join(path, 'cmems_downloader_log.out')
    else:
        path_exist = os.path.isdir(config_dict.get('LOG', 'path'))
        if path_exist:
            log_filename = os.path.join(config_dict.get('LOG', 'path'),'cmems_downloader_log.out')
        else:
            log_filename = os.path.join(path, 'cmems_downloader_log.out')
    logging.getLogger('').handlers = []
    logging.basicConfig(filename = log_filename,
                        level = getattr(logging, config_dict.get('LOG', 'level')),
                        filemode = 'w',
                        format = '%(asctime)s : %(levelname)s : %(message)s')
    formatter = logging.Formatter('%(levelname)s : %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info('*****************************************')
    logging.info('CMEMS Data Downloader ' + _downloader_version + ' is starting ...')
    logging.info('*****************************************')
    if not path_exist:
        logging.exception('cmems_data_downloader.py - exception occured when CDD tried to write log file in a non-default folder. Please check '
                          + 'that the folder exists. The path option in the config file is going to be modified to the default folder.')
        config_dict.set('LOG', 'path', '')
        with open(os.path.join(path, 'cmems_downloader.ini'), 'w') as configfile:
            config_dict.write(configfile)   
    ui = MainWindow(path, config_dict)
    ui.show()
    splash.finish(ui)
    sys.exit(app.exec_())


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception


if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(__file__))
    launch_data_downloader(path)
    