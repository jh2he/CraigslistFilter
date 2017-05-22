from craigslist import CraigslistHousing
import postToSlack

class ClScraper(object):
    def __init__(self):
        self.cl = CraigslistHousing(site='toronto', area='tor', category='apa', filters={'max_price': 2000, 'min_price': 1000})
        self.poster = postToSlack.SlackPoster()
    
    def performScrape(self)
        results = self.cl.get_results(sort_by='newest', geotagged=True, limit=5)

    
        


