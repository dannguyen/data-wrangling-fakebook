
"""fetch-basic.py -- Fetch plaintext data files from NASA Climate site and serialize as CSV

Fetches the plaintext data file behind the presentations of this landing page:

    https://climate.nasa.gov/vital-signs/global-temperature/

Direct link to data file:

    https://climate.nasa.gov/system/internal_resources/details/original/647_Global_Temperature_Data_File.txt

Simply saves data file to:

    datastash/originals/647_Global_Temperature_Data_File.txt

"""
import urllib.request
import os

SRC_URL = 'https://climate.nasa.gov/system/internal_resources/details/original/647_Global_Temperature_Data_File.txt'
DATA_DIR = 'datastash' + '/' + 'originals'
DEST_PATH = DATA_DIR  + '/' + SRC_URL.split('/')[-1]

# make the subdir
os.makedirs(DATA_DIR, exist_ok=True)

# download from URL
u = urllib.request.urlopen(SRC_URL)
content = u.read()
u.close()

# write to file
o = open(DEST_PATH, 'wb')
o.write(content)
o.close()
