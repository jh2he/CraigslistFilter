import shapefile

class Region(object):
    def __init__(self):
        self.neighbourhoods = {}
        self.SHAPEFILE="TorNeighbour.shp"
        self.initShapeFile()

    #Comparator to determine location in the neighbourhood box
    #geotag = [latitude, longitude]
    #coords = [bottomleft-long, lat, topright-long, lat]
    def inAreaApprox(self, geotag, coords):
        if (coords[0] < geotag[1] < coords[2] and 
            coords[1] < geotag[0] < coords[3]):
            return True
        return False

    def initShapeFile(self):
        shpf = shapefile.Reader(self.SHAPEFILE)

        records = shpf.iterShapeRecords()
        for record in records:
            name = record.record
            bbox = record.shape.bbox
            self.neighbourhoods[name[1]] = [coord for coord in bbox]
            
    def findArea(self, geotag):
        for a, coord in self.neighbourhoods.items():
            if (self.inAreaApprox(geotag, coord)):
                return a
        return "none"