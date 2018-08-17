import logging
from PyQt5 import QtWidgets


def object_init(self):
    logging.debug('material_functions.py - object_init')
    self.modified = False
    self.variables_cb = []


def info_button_text(self):
    logging.debug('material_functions.py - info_button_text')
    self.info_button_list = [self.info_bt_1,self.info_bt_2,self.info_bt_3,self.info_bt_4,self.info_bt_5,self.info_bt_6,self.info_bt_7]
    self.info_button_text_dict = {'info_bt_1':('All products are read when the software starts to create a database and are classified based '
                                               + 'on a domain, a type, a source and a mode. First, select a domain, then a type, and so on. '
                                               + 'Once it is done, available products are displayed in the last combobox in the right part '
                                               + 'of the GUI. Select one of them to populate all other tabs.'),
                                  'info_bt_2':('All datasets available in a product are listed here once a product is selected. If each dataset '
                                               + 'involves a different temporal/spatial/vertical coverage and/or variables, the GUI will be '
                                               + 'updated based on information found in the database. Select a dataset to display a list of '
                                               + 'variables available in the dataset.'),
                                  'info_bt_3':('The following section is dedicated to all variables included in a product and linked to a part'
                                               + 'icular dataset. For few products and datasets, there is no possibility to select variables. '
                                               + 'In that case, a warning message is displayed. If no variable is selected by the user, all '
                                               + 'variables in the dataset will be downloaded.'),
                                  'info_bt_4':('The user has the possibility to select a temporal coverage for its query. Based on the temporal '
                                               + 'coverage of the selected product, the following section can be modified according to the '
                                               + 'temporal coverage of the selected dataset if it exists.'),
                                  'info_bt_5':('The vertical coverage depends on a dataset. It can cover surface, a whole water column, or '
                                               + 'different depths. For products/datasets with depths, if no depths are selected, the software '
                                               + 'will download the whole vertical coverage.'),
                                  'info_bt_6':('If a product/dataset is subsetable, the following section is activated and it is possible to select '
                                               + 'an area by entering max and min longitude/latitude. This section doesn\'t take into account '
                                               + 'min and max longitude/latitude registered in the product/dataset webpage yet.'),
                                  'info_bt_7':('The user has the possibility to give a name to the file donwloaded by the software.'),
                                  'ow_infoButton_1':('The user can change here the verbose level of the logging system. If an issue is '
                                                     + 'noticed, it is a good idea to change the level to DEBUG and send the log '
                                                     + 'file to the developer.'),
                                  'ow_infoButton_2':('The path where to save the log file, for those who appreciate to keep all '
                                                     + 'their logs at the same place. A reboot of the software is necessary if the '
                                                     + 'location of the log file is changed.'),
                                  'ow_infoButton_3':('A personal account on CMEMS website is necessary to use the software and the CMEMS '
                                                     + 'MOTU api. Once the account is created, the username has to be entered here. For '
                                                     + 'those who don\'t want to store their credentials, it is possible to enter them in '
                                                     + 'a dedicated window just before submitting a query, and leaving the username and '
                                                     + 'password fields empty.'),
                                  'ow_infoButton_4':('A personal account on CMEMS website is necessary to use the software and the CMEMS '
                                                     + 'MOTU api. Once the account is created, the password has to be entered here. For '
                                                     + 'those who don\'t want to store their credentials, it is possible to enter them in '
                                                     + 'a dedicated window just before submitting a query, and leaving the username and '
                                                     + 'password fields empty.'),
                                  'ow_infoButton_5':'A folder where to save the file/data downloaded on ECMWF server.',
                                  'ow_infoButton_6':('If checked, CMEMS Data Downloader displays information about the CMEMS MOTU API '
                                                     + 'at startup.'),
                                  'ow_infoButton_7':'Activate this option to allow CMEMS Data Downloader to check for an update online.',
                                  'ow_infoButton_8':'Activate this option to allow CMEMS Data Downloader to check for the product database updates.',
                                  }


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
                           'sea_ice_fraction_error':'Sea ice area fraction error estimate',
                           'sst_anomaly':'Sea surface temperature anomaly from pathfinder climatology',
                           'analysis_error':'Estimated error standard deviation of analysed sea surface temperature',
                           'mask':'Sea/Land/Lake/Ice field composite mask',
                           'standard_deviation_ice':'Standard deviation of sea ice fraction',
                           'standard_deviation_sst':'Standard deviation of analysed sea surface temperature',
                           'ice_conc':'Concentration of sea ice',
                           'status_flag':'Status flag for sea ice concentration retrieval',
                           'standard_error':'Total uncertainty of concentration of sea ice',
                           'Lambert_Azimuthal_Grid':'Lambert_Azimuthal_Grid',
                           'Polar_Stereographic_Grid':'Polar_Stereographic_Grid',
                           'lon':'Longitude',
                           'time_bnds':'Seconds since 1978-01-01 00:00:00 (time_bnds)',
                           'algorithm_standard_error':'Algorithm uncertainty of concentration of sea ice',
                           'smearing_standard_error':'Smearing uncertainty of concentration of sea ice',
                           'lat':'Latitude',
                           'eastward_wind':'Eastward wind speed',
                           'northward_wind':'Northward wind speed',
                           'surface_downward_eastward_stress':'Eastward wind stress',
                           'surface_downward_northward_stress':'Northward wind stress',
                           'wind_speed':'Wind speed',
                           'surface_downward_northward_stress_rms':'Northward wind stress root mean square',
                           'wind_stress':'Wind stress',
                           'land_ice_mask':'Land ice mask',
                           'wind_stress_std':'Wind stress standard deviation',
                           'sampling_length':'Sampling length',
                           'wind_stress_rms':'Wind stress root mean square',
                           'eastward_wind_std':'Eastward wind speed standard deviation',
                           'wind_speed_rms':'Wind speed root mean square',
                           'surface_downward_eastward_stress_rms':'Eastward wind stress root mean square',
                           'eastward_wind_rms':'Eastward wind speed root mean square',
                           'surface_downward_northward_stress_std':'Northward wind stress standard deviation',
                           'northward_wind_std':'Northward wind speed standard deviation',
                           'surface_downward_eastward_stress_std':'Eastward wind stress standard deviation',
                           'wind_speed_std':'Wind speed standard deviation',
                           'northward_wind_rms':'Northward wind speed root mean square',
                           'air_density':'Air density at 10 m',
                           'wind_curl':'Rotation of stress equivalent wind at 10m',
                           'stress_divergence':'Divergence of ocean surface stress',
                           'wind_divergence':'Divergence of stress equivalent wind at 10m',
                           'eastward_wind':'Stress equivalent wind u component at 10 m',
                           'wind_stress_magnitude':'Wind stress',
                           'northward_wind':'Stress equivalent wind v component at 10 m',
                           'eastward_stress':'Wind stress u component',
                           'northward_stress':'Wind stress v component',
                           'stress_curl':'Rotation of ocean surface stress',
                           'wind_speed':'Stress equivalent wind speed at 10 m',
                           'wind_to_dir':'Wind direction at 10 m',
                           'model_stress_curl':'Model rotation of ocean surface stress',
                           'model_stress_divergence':'Model divergence of ocean surface stress',
                           'se_northward_model_wind':'Stress equivalent model wind v component at 10 m',
                           'se_model_wind_curl':'Model rotation of stress equivalent wind at 10m',
                           'model_wind_to_dir':'Model wind direction at 10 m',
                           'eastward_model_stress':'Model stress u component',
                           'se_eastward_model_wind':'Stress equivalent model wind u component at 10 m',
                           'se_model_wind_divergence':'Model divergence of stress equivalent wind at 10m',
                           'wvc_quality_flag':'Wind vector cell quality',
                           'se_model_speed':'Stress equivalent model wind speed at 10 m',
                           'measurement_time':'Measurement acquisition time',
                           'bs_distance':'Backscatter distance',
                           'wvc_index':'Cross track wind vector cell number',
                           'northward_model_stress':'Model stress v component',
                           'model_stress_magnitude':'Model stress',
                           'bottomT':'Sea water potential temperature at sea bed',
                           'uo':'Eastward current velocity in the water column',
                           'vo':'Northward current velocity in the water column',
                           'siconc':'Sea ice area fraction',
                           'sithick':'Sea ice thickness',
                           'usi':'Eastward sea ice velocity',
                           'vsi':'Northward sea ice velocity',
                           'mlotst':'Kara Mixed Layer Depth',
                           'so':'Sea water salinity',
                           'zos':'Sea surface height above geoid',
                           'thetao':'Sea water potential temperature',
                           'temperature':'Temperature',
                           'salinity':'Salinity',
                           'ssh':'Sea surface height',
                           'u':'Eastward velocity',
                           'v':'Northward velocity',
                           'mlp':'Density ocean mixed layer thickness',
                           'fice':'Ice concentration',
                           'hice':'Sea ice thickness',
                           'uice':'Sea ice eastward velocity',
                           'vice':'Sea ice northward velocity',
                           'TEMP':'Sea water temperature',
                           'PSAL':'Sea water salinity',
                           'PSAL_PCTVAR':'Error on sea water salinity',
                           'TEMP_PCTVAR':'Error on sea water temperature',
                           'sea_water_temperature':'Sea water temperature',
                           'sea_water_practical_salinity':'Sea water practical salinity',
                           'sea_surface_wave_significant_height':'Sea surface wave significant height',
                           'sea_surface_wave_mean_period':'Sea surface wave mean period',
                           'mole_concentration_of_dissolved_molecular_oxygen_in_sea_water':'Mole concentration of dissolved molecular oxygen in sea water',
                           'sea_surface_height_above_sea_level':'Sea surface height above sea level',
                           'mass_concentration_of_chlorophyll_in_sea_water':'Mass concentration of chlorophyll in sea water',
                           'CHL':'Mass Concentration of Chlorophyll in Sea Water',
                           'PHYC':'Mole Concentration of Phytoplankton expressed as carbon in sea water',
                           'O2':'Mole Concentration of Dissolved Oxygen in Sea Water',
                           'NO3':'Mole Concentration of Nitrate in Sea Water',
                           'PO4':'Mole Concentration of Phosphate in Sea Water',
                           'Si':'Mole Concentration of Silicate in Sea Water',
                           'Fe':'Mole Concentration of Dissolved iron in Sea Water',
                           'PP':'Net Primary Productivity of Carbon Per Unit Volume',
                           'RRS412':'Sea surface reflectance defined as the ratio of water-leaving radiance to surface irradiance at 412 nm',
                           'RRS443':'Sea surface reflectance defined as the ratio of water-leaving radiance to surface irradiance at 443 nm',
                           'RRS490':'Sea surface reflectance defined as the ratio of water-leaving radiance to surface irradiance at 490 nm',
                           'RRS510':'Sea surface reflectance defined as the ratio of water-leaving radiance to surface irradiance at 510 nm',
                           'RRS555':'Sea surface reflectance defined as the ratio of water-leaving radiance to surface irradiance at 555 nm',
                           'RRS670':'Sea surface reflectance defined as the ratio of water-leaving radiance to surface irradiance at 670 nm',
                           'thetao_cglo':'C-GLORS Potential Temperature',
                           'thetao_foam':'FOAM/GloSea Potential Temperature',
                           'thetao_glor':'GLORYS2V4 Potential Temperature',
                           'thetao_mean':'Mean of Input Analyses Potential Temperatures',
                           'thetao_oras':'ORAS5 Potential Temperature',
                           'thetao_std':'Standard Deviation of Input Analyses Potential Temperatures',
                           'so_cglo':'C-GLORS Salinity',
                           'so_foam':'FOAM/GloSea Salinity',
                           'so_glor':'GLORYS2V4 Salinity',
                           'so_mean':'Mean of Input Analyses Salinities',
                           'so_oras':'ORAS5 Salinity',
                           'so_std':'Standard Deviation of Input Analyses Salinities',
                           'uo_cglo':'C-GLORS Eastward Velocity',
                           'uo_foam':'FOAM/GloSea Eastward Velocity',
                           'uo_glor':'GLORYS2V4 Eastward Velocity',
                           'uo_mean':'Mean of Input Analyses Eastward Velocities',
                           'uo_oras':'ORAS5 Eastward Velocity',
                           'uo_std':'Standard Deviation of Input Analyses Eastward Velocities',
                           'vo_cglo':'C-GLORS Northward Velocity',
                           'vo_foam':'FOAM/GloSea Northward Velocity',
                           'vo_glor':'GLORYS2V4 Northward Velocity',
                           'vo_mean':'Mean of Input Analyses Northward Velocities',
                           'vo_oras':'ORAS5 Northward Velocity',
                           'vo_std':'Standard Deviation of Input Analyses Northward Velocities'
                           }





    self.temporal_step_name = {'dm':'daily-mean',
                               'mm':'monthly-mean',
                               'sm':'seasonal-mean',
                               'ir':'irregular',
                               'hi':'hourly-instantaneous',
                               'in':'instantaneous',
                               'di':'daily-instantaneous',
                               'hm':'hourly-mean'
                               }