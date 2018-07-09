import logging
import xml.dom.minidom
import datetime
from PyQt5 import QtGui, QtCore

NAMESPACE_URI = 'CMEMSDataDownloader'

def save_xml_query(self, out_file_name):
    logging.info('xml_functions.py - save_xml_query - starting ...')
    doc = xml.dom.minidom.Document()
    doc_root = add_element(doc, "DownloaderQuery", doc)
    doc_root.setAttribute("xmlns:downloader", NAMESPACE_URI)
    add_element(doc, "CreationDate", doc_root, datetime.date.isoformat(datetime.date.today()))
    
    
    ############################
    # product and dataset
    ############################
    product_dataset = add_element(doc, "ProductDataset", doc_root)
    product, dataset = '', ''
    if self.main_cb_5.currentText() != 'Make a choice...' and self.main_cb_5.currentText() != 'No product available...':
        product = self.main_cb_5.currentText()
    if self.main_cb_6.currentText() != 'Make a choice...' and self.main_cb_6.currentText() != 'No product selected...':
        dataset = self.main_cb_6.currentText()
    add_element(doc, "Product", product_dataset, product)
    add_element(doc, "Dataset", product_dataset, dataset)
    
    
    ############################
    # variables
    ############################
    variables = add_element(doc, "Variables", doc_root)
    for cb in self.variables_cb:
        if cb.isChecked():
            add_element(doc, "Variable", variables, cb.text())
    
    
    ############################
    # time period
    ############################
    time_period = add_element(doc, "TimePeriod", doc_root)
    add_element(doc, "From", time_period, self.main_de_1.date().toString(QtCore.Qt.ISODate))
    add_element(doc, "To", time_period, self.main_de_2.date().toString(QtCore.Qt.ISODate))
    
    
    ############################
    # depth
    ############################
    depth = add_element(doc, "Depth", doc_root)
    if self.main_cb_7.currentText() != 'Make a choice...' and self.main_cb_7.currentText() != 'No depth...':
        add_element(doc, "DepthMin", depth, '')
        add_element(doc, "DepthMax", depth, self.main_cb_7.currentText())
    
    
    ############################
    # area
    ############################
    area = add_element(doc, "Area", doc_root)
    if self.space_ln_north.isEnabled():
        add_element(doc, "LatMax", area, self.space_ln_north.text())
        add_element(doc, "LatMin", area, self.space_ln_south.text())
        add_element(doc, "LonMin", area, self.space_ln_west.text())
        add_element(doc, "LonMax", area, self.space_ln_east.text())
    
    
    ############################
    # filename
    ############################
    add_element(doc, "FileName", doc_root, self.main_ln_1.text())   
    
    
    ############################
    # File Creation
    ############################
    logging.debug('xml_functions.py - save_xml_query - file creation ...')
    f = open(out_file_name, 'w')
    f.write(doc.toprettyxml())
    f.close()
    self.modified = False
    self.make_window_title()
    logging.info('xml_functions.py - save_xml_query - xml file successfully created')
    
    
def open_xml_query(self, file_name):
    logging.info('xml_functions.py - open_xml_query - starting ...')
    f = open(file_name, 'r')
    doc = xml.dom.minidom.parse(f)
    
    
    ############################
    # product and dataset
    ############################
    main_index = self.tabWidget.currentIndex()
    self.tabWidget.setCurrentIndex(0)
    product_dataset = get_element(doc, "ProductDataset")
    product = get_element_value(product_dataset, 'Product')
    dataset = get_element_value(product_dataset, 'Dataset')
    tree = self.product_database[product]['tree']
    self.main_cb_1.setCurrentIndex(self.main_cb_1.findText(tree[0]))
    self.main_cb_2.setCurrentIndex(self.main_cb_2.findText(tree[1]))
    self.main_cb_3.setCurrentIndex(self.main_cb_3.findText(tree[2]))
    self.main_cb_4.setCurrentIndex(self.main_cb_4.findText(tree[3]))
    self.main_cb_5.setCurrentIndex(self.main_cb_5.findText(product))
    self.main_cb_6.setCurrentIndex(self.main_cb_6.findText(dataset))
    self.tabWidget.setCurrentIndex(main_index)
    
    
    ############################
    # variables
    ############################
    self.tabWidget.setCurrentIndex(1)
    variables = get_element_values(get_element(doc, "Variables"), 'Variable')
    for widget in self.variables_cb:
        if widget.text() in variables:
            widget.setChecked(True)
    self.tabWidget.setCurrentIndex(main_index)
    
    
    ############################
    # time period
    ############################
    period_from = get_element_value(get_element(doc, "TimePeriod"), 'From')
    period_to = get_element_value(get_element(doc, "TimePeriod"), 'To')
    self.main_de_1.setDate(QtCore.QDate.fromString(period_from, QtCore.Qt.ISODate))
    self.main_de_2.setDate(QtCore.QDate.fromString(period_to, QtCore.Qt.ISODate))
    
    
    ############################
    # depth
    ############################
    depth_max = get_element_value(get_element(doc, "Depth"), "DepthMax")
    if self.main_cb_7.isEnabled() and depth_max:
        self.main_cb_7.setCurrentIndex(self.main_cb_7.findText(depth_max))
        
    
    ############################
    # area
    ############################
    if self.space_ln_north.isEnabled():
        self.space_ln_north.setText(get_element_value(get_element(doc, "Area"), "LatMax"))
        self.space_ln_south.setText(get_element_value(get_element(doc, "Area"), "LatMin"))
        self.space_ln_west.setText(get_element_value(get_element(doc, "Area"), "LonMin"))
        self.space_ln_east.setText(get_element_value(get_element(doc, "Area"), "LonMax"))
    
    
    ############################
    # filename
    ############################
    self.main_ln_1.setText(get_element_value(doc, "FileName"))
    
    
    self.modified = False
    self.make_window_title()
    logging.info('xml_functions.py - open_xml_query - xml file successfully parsed')

    
def add_element(doc, element_name, parent, value=None):
    logging.debug('xml_functions.py - add_element')
    new_element = doc.createElementNS(NAMESPACE_URI, 'downloader:' + element_name)
    if value:
        new_text = doc.createTextNode(value)
        new_element.appendChild(new_text)
    parent.appendChild(new_element)
    return new_element


def get_element(parent, element_name):
    logging.debug('xml_functions.py - get_element')
    return parent.getElementsByTagNameNS(NAMESPACE_URI, element_name)[0]


def get_element_value(parent, element_name):
    logging.debug('xml_functions.py - get_element_value')
    elements = parent.getElementsByTagNameNS(NAMESPACE_URI, element_name)
    if elements:
        element = elements[0]
        nodes = element.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                return node.data.strip()


def get_check_value(parent, element_name):
    logging.debug('xml_functions.py - get_check_value')
    elements = parent.getElementsByTagNameNS(NAMESPACE_URI, element_name)
    return elements[0].childNodes[0].data.strip()


def get_element_values(parent, element_name):
    logging.debug('xml_functions.py - get_element_values')
    value_list = []
    elements = parent.getElementsByTagNameNS(NAMESPACE_URI, element_name)
    for element in elements:
        value_list.append(element.childNodes[0].data.strip())
    return value_list
