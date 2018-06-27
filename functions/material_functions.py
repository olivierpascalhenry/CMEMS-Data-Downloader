import logging
from PyQt5 import QtWidgets


def object_init(self):
    logging.debug('material_functions.py - object_init')
    self.modified = False
    self.product_database = {}
    self.dataset_database = {}
    self.variables_cb = []


def info_button_text(self):
    logging.debug('material_functions.py - info_button_text')
    self.info_button_text_dict = {}


def dataset_data_information(self):
    logging.debug('material_functions.py - dataset_data_information')
    self.variables_name = {'sla':'Sea level anomaly',
                           'adt':'Absolute dynamic topography',
                           'ugos':'Absolute geostrophic velocity: zonal component',  
                           'vgos':'Absolute geostrophic velocity: meridian component',   
                           'ugosa':'Geostrophic velocity anomalies: zonal component',  
                           'vgosa':'Geostrophic velocity anomalies: meridian component',  
                           'err':'Formal mapping error',
                           'analysed_sst':'Analysed sea surface temperature',
                           'sea_ice_fraction':'Sea ice fraction',
                           'sst_anomaly':'Sea surface temperature anomaly from pathfinder climatology',
                           'analysis_error':'Estimated error standard deviation of analysed sea surface temperature',
                           'mask':'Sea/Land/Lake/Ice field composite mask',
                           'standard_deviation_ice':'Standard deviation of sea ice fraction',
                           'standard_deviation_sst':'Standard deviation of analysed sea surface temperature',
                           }
    
