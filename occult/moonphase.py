'''
Moon Phase Attributes of the Occult Bot
'''

# Imports


# Functions

def zip_to_latlon(city, state=0, country=0 ):
    'Returns the latitude and longitude for a zipcode using geopy'
    if state != 0:
        location = geolocator.geocode(city, state)
    else:
        location = geolocator.geocode(city, country)

    return location.latitude, location.longitude

def get_moonphase():
    'Gets the Moonphases'
