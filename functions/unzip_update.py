#!/usr/bin/python3

import tarfile
import sys
import time
import os
import signal
import shutil
import tempfile
import logging


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception


logging.getLogger('').handlers = []
logging.basicConfig(filename = 'cmems_updater_log.out',
                    level = getattr(logging, 'INFO'),
                    filemode = 'w',
                    format = '%(asctime)s : %(levelname)s : %(message)s')


logging.info('********************************************')
logging.info('CMEMS Data Downloader update is starting ...')
logging.info('********************************************')

zip_file = sys.argv[1]
dest_folder = sys.argv[2]
tmp_folder = tempfile.gettempdir() + '/cmems_data_downloader/'
logging.info('zip file: ' + zip_file)
logging.info('destination folder: ' + dest_folder)
logging.info('temporary folder: ' + tmp_folder)

print('')
print('--------------------------------------------------------------------')
print('--- An update is going to be installed for CMEMS Data Downloader ---')
print('------ Do not close the terminal until the end of the process ------')
print('--------------------------------------------------------------------')
print('')
print('File to unzip:\t\t' + zip_file)
print('Destination folder:\t' + dest_folder)
print('')
print('CMEMS Data Downloader is closing, waiting...')
time.sleep(3)
print('')
print('Uncompressing update...')
logging.info('uncompressing starting...')

try:
    tar = tarfile.open(zip_file, "r:gz")
    tar.extractall(path=tempfile.gettempdir())
    tar.close()
    logging.info('uncompressing finished...')
except Exception:
    logging.exception('an exception occured during uncompressing')

print('')
print('Installing update...')
logging.info('installing update...')

try:
    files = os.listdir(tmp_folder)
    for f in files:
        logging.info('---> ' + tmp_folder + f)
        shutil.move(tmp_folder + f, dest_folder + f)
    logging.info('installing finished...')
except Exception:
    logging.exception('an exception occured during installation')
    
print('')
print('Cleaning...')
logging.info('cleaning...')

try:
    shutil.rmtree(tmp_folder)
    os.remove(zip_file)
    logging.info('cleaning finished...')
except Exception:
    logging.exception('an exception occured during cleaning')

print('')
print('End of the process...')
logging.info('end of the process...')
print('Terminal will close in 5 seconds')
time.sleep(5)
logging.info('terminal closing...')
