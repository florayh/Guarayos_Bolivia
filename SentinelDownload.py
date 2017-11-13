import os
os.chdir("/Users/Flora/Desktop/Sentinel_Python")
import sys
sys.path.append("/Users/Flora/Desktop/Sentinel_Python")
import sentinel_api_noPB as api


# use username and password for ESA DATA Hub authentication
username = ''
password = ''

# please also specify the Hub URL:
# All Sentinel-1 and -2 scenes beginning from 15th Nov. 2015: https://scihub.copernicus.eu/apihub/
# All historic Sentinel-1 scenes: https://scihub.copernicus.eu/dhus/
s2 = api.SentinelDownloader(username, password, api_url='https://scihub.copernicus.eu/apihub/')

# set directory for
# - filter scenes list with existing files
# - set directory path for data download
s2.set_download_dir('./download')

# load geometries from shapefile
s2.load_sites('TCO_GUARAYOS1prjwgs.shp')

# search for scenes with some restrictions (minimum overlap: 1%)
s2.search('S2A*', start_date="2017-05-15", end_date = "2017-06-01", min_overlap=0.5, cloudcoverpercentage = '[0 TO 1]')

s2.print_scenes()



