from craigslist import CraigslistHousing
import shapefile

#Comparator to determine location in the neighbourhood box
#geotag = [latitude, longitude]
#coords = [bottomleft-long, lat, topright-long, lat]
def inArea(geotag, coords):
    if (coords[0] < geotag[1] < coords[2] and 
        coords[1] < geotag[0] < coords[3]):
        return True
    return False

shpf = shapefile.Reader("TorNeighbour.shp")

records = shpf.iterShapeRecords()
neighbourhoods = {}
for record in records:
    name = record.record
    bbox = record.shape.bbox
    neighbourhoods[name[1]] = [coord for coord in bbox]

#cl = CraigslistHousing(site='toronto', area='tor', category='apa',
                       # filters={'max_price': 2000, 'min_price': 1000})

cl = CraigslistHousing(site='toronto', area='tor', category='apa', filters={'max_price': 2000, 'min_price': 1000})
                       
results = cl.get_results(sort_by='newest', geotagged=True, limit=20)

for result in results:
    geotag = result["geotag"]
    area_found = False
    area = ""
    for aname, acoord in neighbourhoods.items():
        try:
            if (inArea(geotag, acoord)):
                area = aname
                area_found = True
                print("Found in " + area)
                print(result)
                printI("\n")
        except:
            print("Location not found")
            print(result)
            printI("\n")
            
