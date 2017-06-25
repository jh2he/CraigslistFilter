#UNUSED -- FOR NEAREST BUS LOCATION WITHIN THE INDICATED RADIUS

from googleplaces import GooglePlaces, types, lang
from datetime import datetime
import json

class busLocation(object):
    def __init__(self):
        with open('auth.json') as data_file:    
            self.auth = json.load(data_file)
        GOOGLE_KEY=self.auth['google_key']
        print(GOOGLE_KEY)
        self.googlePlaces = GooglePlaces(GOOGLE_KEY)
    
    def searchForBus(self, geotag):
        busResult = self.googlePlaces.nearby_search(
            types= [types.TYPE_BUS_STATION],
            lat_lng= geotag,
            radius= 500
        )
        return busResult

busLoc = busLocation()

lat = 43.7370860
lng = -79.3421320
origin = {'lat': lat, 'lng': lng} # Accepts Tuples as Latitude and Longitude

nearbyBus = busLoc.searchForBus(origin)

print(type(nearbyBus))
print(nearbyBus)

for station in nearbyBus.places:
    print(station)