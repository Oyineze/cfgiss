import requests
import json
from datetime import datetime

def get_iss_location():
    endpoint = 'http://api.open-notify.org/iss-now.json'
    response= requests.get(endpoint)
    return response.json()
print(get_iss_location())

    # Return in json format {"iss_position": {"latitude": "-49.4665", "longitude": "-51.0737"}, "message": "success", "timestamp": 1552249236}

def get_iss_pass_time(lat, lon):
    endpoint = 'http://api.open-notify.org/iss-pass.json'
    coordinates = {
        'lat': lat,
        'lon': lon
    }
    response = requests.get(endpoint, params=coordinates)
    date_list = response.json().get('response')
    pass_time_unix = int(date_list[0].get('risetime'))

    return datetime.utcfromtimestamp(pass_time_unix).strftime('%Y-%m-%d %H:%M:%S')

print(get_iss_pass_time('-52.0','10.0'))


    # Return in following format 2019-03-10 23:56:31
def get_iss_pass_time_from_postcode(postcode):
    endpoint = f'http://api.postcodes.io/postcodes/{postcode}'
    response = requests.get(endpoint).json()
    lat = response.get('result').get('latitude')
    lon = response.get('result').get('longitude')
    return get_iss_pass_time( lat, lon )

print( get_iss_pass_time_from_postcode('E145GL'))

    # Return in following format 2019-03-10 23:56:31
