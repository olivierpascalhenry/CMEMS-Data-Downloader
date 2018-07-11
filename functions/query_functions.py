import logging
import calendar
from PyQt5 import QtCore


def check_product_dataset(self):
    logging.debug('query_functions.py - check_product_dataset')
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
    logging.debug('query_functions.py - prepare_query')
    
    '''user = self.config_dict['CREDENTIALS'].get('user')
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
        '''
    
    
    
    
    query = {}
    
    user, password, motu_url, service, product = None, None, None, None, None
    lon_min, lon_max, lat_min, lat_max, date_min, date_max, depth_min, depth_max = None, None, None, None, None, None, None, None
    var, folder, filename, output = None, None, None, None
    
    ### service
    service = str(self.main_cb_5.currentText()) + self.product_database[self.main_cb_5.currentText()]['suffixe']
    
    ### product
    product = str(self.main_cb_6.currentText())
    
    ### password, user and url
    user = self.config_dict['CREDENTIALS'].get('user')
    password = self.config_dict['CREDENTIALS'].get('password')
    motu_url = self.config_dict['CREDENTIALS'].get('url')
    
    
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
    '''depth_text = self.main_cb_7.currentText()
    if depth_text != 'Make a choice...' and depth_text != 'No depth...' and depth_text != 'surface':
        depth_max = str(self.main_cb_7.currentText())'''
    
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
                var_tmp.append(var_names[cb.text()])
    if var_tmp:
        if len(self.variables_cb) != checked_count:
            var = var_tmp
    
    
    parameter_list = [service, product, lon_min, lon_max, lat_min, lat_max, 
                      date_min, date_max, depth_min, depth_max, var, output]
    name_list = ['service', 'product', 'x_lo', 'x_hi', 'y_lo', 'y_hi', 
                      't_lo', 't_hi','z_lo', 'z_hi', 'variable', 'output']
    
    for index, parameter in enumerate(parameter_list):
        if parameter != None:
            query[name_list[index]] = parameter
    
    
    ### si tous les champs Area sont vides , et si toutes les variables ont été sélectionnées, et si la profondeur n'a pas été modifiée, alors on télécharge
    ### un fichier .zip avec des fichiers netcdf correspondant aux dates
    ### si on demande une variable particulière, ou une zone particulière, ou une profondeur particulière, alors on télécharge un fichier netcdf.
    
    
    query['scriptVersion'] = '1.5.00'
    query['mode'] = 'status'
    query['action'] = 'productdownload'
    
    logging.debug('query_functions.py - prepare_query - query ready: ' + str(query))
    return query, motu_url, user, password, folder, filename

    