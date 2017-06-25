import craigsListScrape
import time

def main():
    print("press the Enter key to start...")
    input()
    looper()
    
def looper():
    scraper = craigsListScrape.craigsListScraper()
    while True:
        scraper.performScrape()
        time.sleep(1200)
    
if __name__ == "__main__":
    main()
    
