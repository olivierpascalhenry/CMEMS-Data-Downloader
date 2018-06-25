import logging
from PyQt5 import QtWidgets


def object_init(self):
    logging.debug('material_functions.py - object_init')
    self.modified = False
    


def info_button_text(self):
    logging.debug('material_functions.py - info_button_text')
    self.info_button_text_dict = {}


def dataset_data_information(self):
    logging.debug('material_functions.py - dataset_data_information')
    
    
    
    self.dataset_database = {'Global':{'Physics':{'Model':'',
                                                  'Insitu':'',
                                                  'Satellite':{'Near real time':'',
                                                               'Delayed delivery':['SEALEVEL_GLO_PHY_L3_REP_OBSERVATIONS_008_045',
                                                                                   'SEALEVEL_GLO_PHY_L4_REP_OBSERVATIONS_008_047',
                                                                                   'SST_GLO_SST_L4_REP_OBSERVATIONS_010_011',
                                                                                   'SST_GLO_SST_L4_REP_OBSERVATIONS_010_024',
                                                                                   'SEAICE_GLO_SEAICE_L4_REP_OBSERVATIONS_011_009',
                                                                                   'WIND_GLO_WIND_L4_REP_OBSERVATIONS_012_003',
                                                                                   'WIND_GLO_WIND_L3_REP_OBSERVATIONS_012_005']},
                                                  'Satellite / Insitu':''},
                                       'Biogeochemistry':'',
                                       'Waves':''},
                             'Arctic Ocean':'',
                             'Baltic Sea':'',
                             'Mediterranean Sea':'',
                             'Black Sea':''
                             }
    
    
    self.product_database = {'SEALEVEL_GLO_PHY_L3_REP_OBSERVATIONS_008_045':{'information':{'short_description':('Altimeter satellite along-track sea surface heights anomalies (SLA) computed with respect to a twenty-year 2012 mean. All the missions are homogenized with respect to a reference mission (see QUID document or http://duacs.cls.fr pages for processing details). The product gives additional variables (e.g. Absolute Dynamic Topography, ADT) that can be used to change the physical content for specific needs.'),
                                                                                            'description':('Short description: Altimeter satellite along-track sea surface heights anomalies (SLA) computed with respect '
                                                                    + 'to a twenty-year 2012 mean. All the missions are homogenized with respect to a reference '
                                                                    + 'mission (see QUID document or http://duacs.cls.fr pages for processing details). The product'
                                                                    + ' gives additional variables (e.g. Absolute Dynamic Topography, ADT) that can be used to '
                                                                    + 'change the physical content for specific needs. Detailed description: This product is processed by the DUACS '
                                                                    + 'multimission altimeter data processing system. It serves in near-real time the main '
                                                                    + 'operational oceanography and climate forecasting centers in Europe and worldwide. It '
                                                                    + 'processes data from all altimeter missions: Jason-3, Sentinel-3A, HY-2A, Saral/AltiKa,'
                                                                    + ' Cryosat-2, Jason-2, Jason-1, T/P, ENVISAT, GFO, ERS1/2. It provides a consistent and '
                                                                    + 'homogeneous catalogue of products for varied applications, both for near real time '
                                                                    + 'applications and offline studies. Processing information: To produce SLA in delayed-time (REPROCESSED), the system'
                                                                    + ' uses the Geophysical Data Records which are computed from a Precise Orbit Ephemeris (POE)'
                                                                    + ' and are delivered within 3 months depending on the mission. Reanalysis products are more '
                                                                    + 'precise than NRT products. The system acquires and then synchronizes altimeter data and '
                                                                    + 'auxiliary data; each mission is homogenized using the same models and corrections. The Input'
                                                                    + ' Data Quality Control checks that the system uses the best altimeter data. The multi-mission'
                                                                    + ' cross-calibration process removes any residual orbit error, or long wavelength error (LWE),'
                                                                    + ' as well as large scale biases and discrepancies between various data flows; all altimeter'
                                                                    + ' fields are interpolated at crossover locations and dates. After a repeat-track analysis, a'
                                                                    + ' mean profile, which is peculiar to each mission, or a Mean Sea Surface (MSS) (when the orbit'
                                                                    + ' is non repetitive) is subtracted to compute sea level anomaly. The MSS is available via the'
                                                                    + ' Aviso+ dissemination (http://www.aviso.altimetry.fr/en/data/products/auxiliary-products/mss'
                                                                    + '.html). Data are then cross validated, filtered from residual noise and small scale'
                                                                    + ' signals (sla_filtered variable). The ADT (Absolute Dynamic Topography, adt_filtered variable)'
                                                                    + ' is then computed as follows: adt_filtered=sla_filtered+MDT where MDT is the Mean Dynamic'
                                                                    + ' Topography distributed by Aviso+ (http://www.aviso.altimetry.fr/en/data/products/auxiliar'
                                                                    + 'y-products/mdt.html).'),
                                                                     'resolution':'7km x 7km',
                                                                     'temporal_resolution':'instantaneous',
                                                                     'level':'L3',
                                                                     'type':'swath',
                                                                     'vertical':'surface',
                                                                     'temporal':'from 1993-01-01T00:00:00Z to 2017-05-15T00:00:00Z',
                                                                     'production':'SL-CLS-TOULOUSE-FR',
                                                                     'image':'SEALEVEL_GLO_PHY_L3_REP_OBSERVATIONS_008_045.png'},
                                                     'variables':None,
                                                     'subset':None,
                                                     'swath':['dataset-duacs-rep-global-alg-phy-l3',
                                                              'dataset-duacs-rep-global-alg-phy-unfiltered-l3',
                                                              'dataset-duacs-rep-global-al-phy-l3',
                                                              'dataset-duacs-rep-global-al-phy-unfiltered-l3',
                                                              'dataset-duacs-rep-global-c2-phy-l3',
                                                              'dataset-duacs-rep-global-c2-phy-unfiltered-l3',
                                                              'dataset-duacs-rep-global-e1-phy-l3',
                                                              'dataset-duacs-rep-global-e1-phy-unfiltered-l3',
                                                              'dataset-duacs-rep-global-e2-phy-l3',
                                                              'dataset-duacs-rep-global-e2-phy-unfiltered-l3',
                                                              'dataset-duacs-rep-global-enn-phy-l3',
                                                              'dataset-duacs-rep-global-enn-phy-unfiltered-l3',
                                                              'dataset-duacs-rep-global-en-phy-l3',
                                                              'dataset-duacs-rep-global-en-phy-unfiltered-l3',
                                                              'dataset-duacs-rep-global-g2-phy-l3',
                                                              'dataset-duacs-rep-global-g2-phy-unfiltered-l3',
                                                              'dataset-duacs-rep-global-h2g-phy-l3',
                                                              'dataset-duacs-rep-global-h2g-phy-unfiltered-l3',
                                                              'dataset-duacs-rep-global-h2-phy-l3',
                                                              'dataset-duacs-rep-global-h2-phy-unfiltered-l3',
                                                              'dataset-duacs-rep-global-j1g-phy-l3',
                                                              'dataset-duacs-rep-global-j1g-phy-unfiltered-l3',
                                                              'dataset-duacs-rep-global-j1n-phy-l3',
                                                              'dataset-duacs-rep-global-j1n-phy-unfiltered-l3',
                                                              'dataset-duacs-rep-global-j1-phy-l3',
                                                              'dataset-duacs-rep-global-j1-phy-unfiltered-l3',
                                                              'dataset-duacs-rep-global-j2n-phy-l3',
                                                              'dataset-duacs-rep-global-j2n-phy-unfiltered-l3',
                                                              'dataset-duacs-rep-global-j2-phy-l3',
                                                              'dataset-duacs-rep-global-j2-phy-unfiltered-l3',
                                                              'dataset-duacs-rep-global-j3-phy-l3',
                                                              'dataset-duacs-rep-global-j3-phy-unfiltered-l3',
                                                              'dataset-duacs-rep-global-tpn-phy-l3',
                                                              'dataset-duacs-rep-global-tpn-phy-unfiltered-l3',
                                                              'dataset-duacs-rep-global-tp-phy-l3',
                                                              'dataset-duacs-rep-global-tp-phy-unfiltered-l3',
                                                              'dataset-duacs-rep-global-sa3-phy-l3',
                                                              'dataset-duacs-rep-global-sa3-phy-unfiltered-l3'],
                                                     'suffixe':'-DGF'},
    'SEALEVEL_GLO_PHY_L4_REP_OBSERVATIONS_008_047':{'information':{'short_description':('For the Global Ocean - Multimission altimeter satellite gridded sea surface'
                                                                                  + ' heights and derived variables computed with respect to a twenty-year mean.'
                                                                                  + ' Previously distributed by Aviso+, no change in the scientific content. All'
                                                                                  + ' the missions are homogenized with respect to a reference mission which is'
                                                                                  + ' currently OSTM/Jason-2. The sla is computed with an optimal and centered '
                                                                                  + 'computation time window (6 weeks before and after the date). Two kinds of '
                                                                                  + 'datasets are proposed: filtered (nominal dataset) and unfiltered.'),
                                                                   'description':('Short description: For the Global Ocean - Multimission altimeter satellite gridded sea surface'
                                                                                  + ' heights and derived variables computed with respect to a twenty-year mean.'
                                                                                  + ' Previously distributed by Aviso+, no change in the scientific content. All'
                                                                                  + ' the missions are homogenized with respect to a reference mission which is'
                                                                                  + ' currently OSTM/Jason-2. The sla is computed with an optimal and centered '
                                                                                  + 'computation time window (6 weeks before and after the date). Two kinds of '
                                                                                  + 'datasets are proposed: filtered (nominal dataset) and unfiltered. Detailed description: This pro'
                                                                                  + 'duct is processed by the SL-TAC multimission altimeter data processing syst'
                                                                                  + 'em. It processes data from all altimeter missions: Jason-3, Sentinel-3A, HY'
                                                                                  + '-2A, Saral/AltiKa, Cryosat-2, Jason-2, Jason-1, T/P, ENVISAT, GFO, ERS1/2. '
                                                                                  + 'It provides a consistent and homogeneous catalogue of products for varied '
                                                                                  + 'applications, both for near real time applications and offline studies. Two '
                                                                                  + 'resolutions are proposed (appears in the file name): *vfec* : for validated, '
                                                                                  + 'filtered, sub-sampled and LWE-corrected data *vxxc* (named unfiltered) : for '
                                                                                  + 'validated, NON-filtered, NON-sub-sampled and LWE-corrected data. Processing information: To produce '
                                                                                  + 'SLA in delayed-time (REPROCESSED), the system uses the Geophysical Data '
                                                                                  + 'Records which are computed from a Precise Orbit Ephemeris (POE) and are '
                                                                                  + 'delivered within 2 months depending on the mission. Reanalysis products are '
                                                                                  + 'more precise than NRT products. The system acquires and then synchronizes '
                                                                                  + 'altimeter data and auxiliary data; each mission is homogenized using the same '
                                                                                  + 'models and corrections. The Input Data Quality Control checks that the system '
                                                                                  + 'uses the best altimeter data. The multi-mission cross-calibration process '
                                                                                  + 'removes any residual orbit error, or long wavelength error (LWE), as well as '
                                                                                  + 'large scale biases and discrepancies between various data flows; all '
                                                                                  + 'altimeter fields are interpolated at crossover locations and dates. After a '
                                                                                  + 'repeat-track analysis, a mean profile, which is peculiar to each mission, or '
                                                                                  + 'a Mean Sea Surface (MSS) (when the orbit is non repetitive) is subtracted to '
                                                                                  + 'compute sea level anomaly. The MSS is available via the Aviso+ dissemination '
                                                                                  + '(http://www.aviso.altimetry.fr/en/data/products/auxiliary-products/mss.html). '
                                                                                  + 'Data are then cross validated, filtered from residual noise and small scale '
                                                                                  + 'signals, and finally sub-sampled (sla variable). Finally an Optimal '
                                                                                  + 'Interpolation is made merging all the flying satellites in order to compute '
                                                                                  + 'gridded SLA. The ADT (Absolute Dynamic Topography, adt variable) is then '
                                                                                  + 'computed as follows: adt =sla +MDT where MDT is the Mean Dynamic Topography '
                                                                                  + 'distributed by Aviso+ (http://www.aviso.altimetry.fr/en/data/products/auxili'
                                                                                  + 'ary-products/mdt.html). The geostrophic currents are derived from sla '
                                                                                  + '(geostrophic velocities anomalies, ugosa and vgosa variables) . Note that '
                                                                                  + 'the gridded products can be visualized on the LAS (Live Access Data) Aviso+ '
                                                                                  + 'web page http://www.aviso.altimetry.fr/en/data/data-access/las-live-access-'
                                                                                  + 'server.html)'),
                                                                    'resolution':'0.25degree x 0.25degree',
                                                                    'temporal_resolution':'irregular',
                                                                    'level':'L4',
                                                                    'type':'grid',
                                                                    'vertical':'surface',
                                                                    'temporal':'from 1993-01-01T00:00:00Z to 2017-05-15T00:00:00Z',
                                                                    'production':'SL-CLS-TOULOUSE-FR',
                                                                    'image':'SEALEVEL_GLO_PHY_L4_REP_OBSERVATIONS_008_047.png'},
                                                    'variables':['sla','adt','ugos','vgos','ugosa','vgosa','err'],
                                                    'subset':'geographical',
                                                    'swath':'dataset-duacs-rep-global-merged-allsat-phy-l4',
                                                    'suffixe':'-TDS'},
    'SST_GLO_SST_L4_REP_OBSERVATIONS_010_011':{'information':{'short_description':('For the Global Ocean- The OSTIA global Sea Surface Temperature '
                                                                             + 'Reanalysis product provides daily gap-free maps of: Foundation sea surface '
                                                                             + 'temperature (referred to as an L4 product) at 0.05deg.x 0.05deg. horizontal '
                                                                             + 'resolution, using in-situ and satellite data from infra-red radiometers. Sea '
                                                                             + 'Surface Temperature anomaly from the Pathfinder climatology at 0.25degree x 0.25degree '
                                                                             + 'horizontal resolution. This product provides the foundation Sea Surface '
                                                                             + 'Temperature, which is the temperature free of diurnal variability. Monthly and '
                                                                             + 'seasonal means of the daily Sea Surface Temperature product at 0.25degree x 0.25degree '
                                                                             + 'horizontal resolution are also available.'),
                                                              'description':('Short description: For the Global Ocean- The OSTIA global Sea Surface Temperature '
                                                                             + 'Reanalysis product provides daily gap-free maps of: Foundation sea surface '
                                                                             + 'temperature (referred to as an L4 product) at 0.05deg.x 0.05deg. horizontal '
                                                                             + 'resolution, using in-situ and satellite data from infra-red radiometers. Sea '
                                                                             + 'Surface Temperature anomaly from the Pathfinder climatology at 0.25degree x 0.25degree '
                                                                             + 'horizontal resolution. This product provides the foundation Sea Surface '
                                                                             + 'Temperature, which is the temperature free of diurnal variability. Monthly and '
                                                                             + 'seasonal means of the daily Sea Surface Temperature product at 0.25degree x 0.25degree '
                                                                             + 'horizontal resolution are also available. Detailed description: The Operational '
                                                                             + 'Sea Surface Temperature and Sea Ice Analysis (OSTIA) system is run by the UK Met '
                                                                             + 'Office and produces a high resolution (1/20deg. - approx. 5km) daily analysis of '
                                                                             + 'the sea surface temperature (SST) for the global ocean. The OSTIA reanalysis uses '
                                                                             + 'satellite data provided by the Pathfinder AVHRR project and reprocessed (A)ATSR '
                                                                             + 'data together with in-situ observations from the ICOADS data-set, to determine '
                                                                             + 'the sea surface temperature. It also uses reprocessed sea-ice concentration data '
                                                                             + 'from the EUMETSAT OSI-SAF. Processing information: The OSTIA output is a daily '
                                                                             + 'global coverage combined SST and sea-ice concentration product on a 1/20deg. '
                                                                             + 'grid, based on measurements from several satellite and in situ SST data sets. '
                                                                             + 'OSTIA uses SST data in the common format developed by GHRSST and makes use of the '
                                                                             + 'uncertainty estimates and auxiliary fields as part of the quality control and '
                                                                             + 'analysis procedure. Satellite derived sea ice products from the EUMETSAT Ocean '
                                                                             + 'and Sea Ice Satellite application Facility (OSI-SAF) provide sea-ice '
                                                                             + 'concentration and edge data to the analysis system. After quality control of the '
                                                                             + 'SST observations, a bias correction is performed using ATSR-2/AATSR data as a '
                                                                             + 'key component. To provide the final SST analysis, a multi-scale optimal '
                                                                             + 'interpolation (OI) is performed using the previous analysis as the basis for a '
                                                                             + 'first guess field. Monthly and seasonal means and standard deviations of the '
                                                                             + 'daily analysis are produced but on a lower resolution (0.25degree x 0.25degree) grid. (The '
                                                                             + 'monthly files also contain the monthly mean and standard deviation of the daily '
                                                                             + 'sea ice concentration fields.) The anomaly of the OSTIA SST is also calculated '
                                                                             + 'from the daily Pathfinder V5.2 climatology at 0.25degree x 0.25degree horizontal resolution.'),
                                                              'spatial_resolution':'0.05degree x 0.05degree',
                                                              'temporal_resolution':'daily-mean, monthly-mean, seasonal-mean',
                                                              'level':'L4',
                                                              'type':'grid',
                                                              'vertical':'surface',
                                                              'temporal':'from 1985-04-15T00:00:00Z to 2007-12-31T00:00:00Z',
                                                              'production':'SST-METOFFICE-EXETER-UK',
                                                              'image':'SST_GLO_SST_L4_REP_OBSERVATIONS_010_011.png'},
                                               'variables':[['analysed_sst','sea_ice_fraction','sst_anomaly'],
                                                            ['analysed_sst','sea_ice_fraction','analysis_error','mask'],
                                                            ['analysed_sst','standard_deviation_ice','sea_ice_fraction','mask','standard_deviation_sst'],
                                                            ['analysed_sst','standard_deviation_sst']],
                                               'subset':'geographical',
                                               'swath':['METOFFICE-GLO-SST-L4-RAN-OBS-ANOM',
                                                        'METOFFICE-GLO-SST-L4-RAN-OBS-SST',
                                                        'METOFFICE-GLO-SST-L4-RAN-OBS-SST-MON',
                                                        'METOFFICE-GLO-SST-L4-RAN-OBS-SST-SEAS'],
                                               'suffixe':'-TDS'}
    }
    
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
    
    ''''SEALEVEL_GLO_PHY_L4_REP_OBSERVATIONS_008_047':{'information':{'description':'',
                                                                    'resolution':'',
                                                                    'level':'',
                                                                    'type':'',
                                                                    'vertical':'',
                                                                    'temporal':'',
                                                                    'production':'',
                                                                    'image':''},
                                                    'variables':None,
                                                    'swath':None,
                                                    'suffixe':''}'''
    
    
    ['http://marine.copernicus.eu/services-portfolio/access-to-products/?option=com_csw&view=details&product_id=SEALEVEL_GLO_PHY_L3_REP_OBSERVATIONS_008_045',
     'http://marine.copernicus.eu/services-portfolio/access-to-products/?option=com_csw&view=details&product_id=SEALEVEL_GLO_PHY_L4_REP_OBSERVATIONS_008_047',
     'http://marine.copernicus.eu/services-portfolio/access-to-products/?option=com_csw&view=details&product_id=SST_GLO_SST_L4_REP_OBSERVATIONS_010_011',
     'http://marine.copernicus.eu/services-portfolio/access-to-products/?option=com_csw&view=details&product_id=SST_GLO_SST_L4_REP_OBSERVATIONS_010_024',
     'http://marine.copernicus.eu/services-portfolio/access-to-products/?option=com_csw&view=details&product_id=SEAICE_GLO_SEAICE_L4_REP_OBSERVATIONS_011_009',
     'http://marine.copernicus.eu/services-portfolio/access-to-products/?option=com_csw&view=details&product_id=WIND_GLO_WIND_L4_REP_OBSERVATIONS_012_003',
     'http://marine.copernicus.eu/services-portfolio/access-to-products/?option=com_csw&view=details&product_id=WIND_GLO_WIND_L3_REP_OBSERVATIONS_012_005']
    
    
    '''
    
    '''
    
    
    