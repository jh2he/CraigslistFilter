import googlemaps
from datetime import datetime
import json

class direction(object):
    def __init__(self):
        with open('auth.json') as data_file:    
            self.auth = json.load(data_file)
        GOOGLE_KEY=self.auth['google_key']
        self.googleMaps = googlemaps.Client(key=GOOGLE_KEY)
    
    def getDirections(self, geotagOrig, geotagDest):
        now = datetime.now()
        dirResult = self.googleMaps.directions(
            geotagOrig,
            geotagDest,
            mode='transit',
            departure_time=now
        )
        return dirResult
        
    def parseDirections(self, route):
        transit = {'duration':'', 'distance':''}
        transit['duration'] = route[0]['legs'][0]['duration']['text']
        transit['distance'] = route[0]['legs'][0]['distance']['text']
        return transit
    

if __name__ == "__main__":  
    dir = direction()

    lat = 43.7370860
    lng = -79.3421320
    orig = {'lat': lat, 'lng': lng} # Accepts Tuples as Latitude and Longitude

    lat2 = 43.645275
    lng2 = -79.380559
    dest = {'lat': lat2, 'lng': lng2}

    route = dir.getDirections(orig, dest)

    print(dir.parseDirections(route))