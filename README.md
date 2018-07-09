Version
-------
CMEMS Data Downloader 0.5.0

!!! NOT SUITED FOR PRODUCTION ENVIRONMENT !!! ONLY FOR TESTING PURPOSES !!!


Project Overview:
-----------------
CMEMS Data Downloader is an open-source tool to help users to download data from the different CMEMS datasets, selecting datasets and variables from the GUI and downloading the data using the official Motu API.


Compatibility:
--------------
    - sources : linux, windows, macos
    - binaries : linux, windows


Install instructions for binaries:
---------------------------------------
Download and install the last binary file in the Release directory. Actually, the binary file is only compatible with Windows (from Windows 7 32) and Linux (from Ubuntu 14.04). The software should be installed in the Home directory for Linux, and outside the Program Files directory for Windows to avoid issues with Windows admin protections.


Install instructions for sources:
--------------------------------------
Download sources and uncompress them somewhere on your hard drive. Open a terminal in the new directory and launch CMEMS Data Downloader by typing: python cmems_data_downloader.py. Do not forget to install dependencies.


External libraries:
-------------------
* PyQt5 v5.10+
* hurry.filesize v0.9+
* requests v2.18+
