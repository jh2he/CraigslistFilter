import craigsListScrape
import time

def main():
    input("press the Enter key to start...")
    looper()

def looper():
    scraper = craigsListScrape.craigsListScraper()
    while True:
        scraper.performScrape()
        time.sleep(1200)
    
if __name__ == "__main__":
    main()
    
