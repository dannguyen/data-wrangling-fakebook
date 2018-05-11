
"""fetch.py -- Fetch plaintext data files from NASA Climate site and serialize as CSV

Fetches the plaintext data file behind the presentations of this landing page:

    https://climate.nasa.gov/vital-signs/global-temperature/

Direct link to data file:

    https://climate.nasa.gov/system/internal_resources/details/original/647_Global_Temperature_Data_File.txt


Simply saves data file to:

    datastash/originals/647_Global_Temperature_Data_File.txt

"""
from pathlib import Path
from urllib.request import urlopen

SRC_URL = 'https://climate.nasa.gov/system/internal_resources/details/original/647_Global_Temperature_Data_File.txt'
DEST_PATH = Path('datastash', 'originals', Path(SRC_URL).name)
# make datastash/originals in case it doesn't exist
DEST_PATH.parent.mkdir(parents=True, exist_ok=True)

with urlopen(SRC_URL) as u:
    content = u.read()

with open(DEST_PATH, 'wb') as o:
    o.write(content)
