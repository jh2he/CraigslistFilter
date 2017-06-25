from craigslist import CraigslistHousing
import slackPoster

class craigsListScraper(object):
    def __init__(self):
        self.cl = CraigslistHousing(site='toronto', area='tor', category='apa', filters={'max_price': 2000, 'min_price': 1000})
        self.poster = slackPoster.SlackPoster()
    
    def performScrape(self):
        results = self.cl.get_results(sort_by='newest', geotagged=True, limit=5)
        self.poster.performPost(results)
