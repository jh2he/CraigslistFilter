from slackclient import SlackClient
import json
import neighbourGen
import sqlListing

class SlackPoster(object):
    def __init__(self):
        self.proccedResults = [{'area_found': False, 'price': u'$1700', 'datetime': u'2017-05-20 16:12', 'has_map': True, 'id': u'6140474228', 'name': u'Apt close to Uoft avail July 1st (incl Utilities)', 'area': 'none', 'url': u'http://toronto.craigslist.org/tor/apa/6140474228.html', 'geotag': (43.656893, -79.399849), 'has_image': False, 'where': u'Spadina/College'},
            {'area_found': False, 'price': u'$1899', 'datetime': u'2017-05-20 15:59', 'has_map': True, 'id': u'6134095162', 'name': u'Looking for Comport & Luxury? self Furnished Condo is perfect for you!', 'area': 'none', 'url': u'http://toronto.craigslist.org/tor/apa/6134095162.html', 'geotag': (43.63738, -79.53651), 'has_image': True, 'where': u'Bloor/Kipling'},
            {'area_found': False, 'price': u'$1799', 'datetime': u'2017-05-20 15:57', 'has_map': True, 'id': u'6131118123', 'name': u'FULLY FURNISHED Large Studio Condo with Phone, Internet, TV & Cable', 'area': 'none', 'url': u'http://toronto.craigslist.org/tor/apa/6131118123.html', 'geotag': (43.654382, -79.37901), 'has_image': True, 'where': u'Yonge/Dundas'},
            {'area_found': False, 'price': u'$1645', 'datetime': u'2017-05-20 15:46', 'has_map': True, 'id': u'6130901968', 'name': u'Avail. now Must see  1 bedroom Toronto Yonge Eglinton Apartments - Or', 'area': 'none', 'url': u'http://toronto.craigslist.org/tor/apa/6130901968.html', 'geotag': (43.708146, -79.399009), 'has_image': True, 'where': u'Toronto'}]
        self.dataBase = sqlListing.SqlListingHelper()
        
        self.prepareArgs("slackauth.json")
        self.performPost()

    def prepareArgs(self, jsonfile):
        with open(jsonfile) as data_file:
            slackdata = json.load(data_file)
        self.SLACK_TOKEN = slackdata["token"]
        self.SLACK_CHANNEL = "#scraped-listings"
    
    def performPost(self):
        region = neighbourGen.Region()

        sc = SlackClient(self.SLACK_TOKEN)
        for result in self.proccedResults:
            if (not self.isDuplicate(result)):
                result["area"] = region.findArea(result["geotag"])
                desc = "{0} | {1} | {2} | <{3}>".format(result["area"], result["price"], result["name"], result["url"])
                sc.api_call(
                    "chat.postMessage", channel=self.SLACK_CHANNEL, text=desc, username='pybot',
                    icon_emoji=':robot_face:'
                )
                self.addToDatabase(result)
            
    def isDuplicate(self, result):
        return (self.dataBase.isDuplicate(result["id"]))
    
    def addToDatabase(self, result):
        self.dataBase.addListing(result)
        
sp = SlackPoster()