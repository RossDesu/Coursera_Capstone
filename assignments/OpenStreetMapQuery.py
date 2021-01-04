'''Using the openstreetmap nominatim service, find json data for a given query'''
import requests
from urllib.parse import urlencode
def open_street_map_data(**kwargs):
    '''
    Uses the nomatim service ( https://nominatim.org/ ) to return OpenStreetMap data
    
    Returns:
        json
    
    possible named argumentss:
        (All optional and strings)
        q  = freeform query 
        street = street name
        city = city name
        county = county name
        country = country name
        postalcode = postal code
        format = type of format to retrieve ( can be xml|json|jsonv2|geojson|geocodejson)
        
        NOTE: per the nomatim.org docs, do not use q with other parameters:
        https://nominatim.org/release-docs/develop/api/Search/
    '''
    base_url = 'https://nominatim.openstreetmap.org/search?'
    url = base_url + urlencode(kwargs)
    print(url)
    return requests.get(url)