from slackclient import SlackClient
import json
import neighbourGen
import sqlListing

class SlackPoster(object):
    def __init__(self):
        self.dataBase = sqlListing.SqlListingHelper()
        self.prepareArgs("slackauth.json")

    def prepareArgs(self, jsonfile):
        with open(jsonfile) as data_file:
            slackdata = json.load(data_file)
        self.SLACK_TOKEN = slackdata["token"]
        self.SLACK_CHANNEL = "#scraped-listings"
    
    def performPost(self, results):
        region = neighbourGen.Region()
        
        sc = SlackClient(self.SLACK_TOKEN)
        for result in results:
            if (not self.isDuplicate(result)):
                result["area"] = region.findArea(result["geotag"])
                desc = "{0} | {1} | {2} | <{3}>".format(result["area"], result["price"], result["name"], result["url"])
                print(desc)
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