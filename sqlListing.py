from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import sessionmaker
import re
from dateutil.parser import parse

class SqlListingHelper(object):
    engine = create_engine("sqlite:///listings.db", echo=False)
    Base = declarative_base()
    
    class Listing(Base):
        __tablename__ = "scrapedListings"
        
        id = Column(Integer, primary_key=True)
        link = Column(String, unique=True)
        name = Column(String)
        created = Column(DateTime)
        geotag = Column(String)
        lat = Column(Float)
        lon = Column(Float)
        price = Column(Float)
        location = Column(String)
        cl_id = Column(Integer, unique=True)
        area = Column(String)
    
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    
        
    def __init__(self):
        self.session = SqlListingHelper.Session()
        #regex for removing non-decimal characters
        self.regexNonDec=re.compile(r'[^\d.]+')
    
    def isDuplicate(self, clid):
        listing = self.session.query(SqlListingHelper.Listing).filter_by(cl_id=clid).first()
        if listing is None:
            return False
        else:
            return True
    
    def addListing(self, result):
        lat = 0
        lon = 0
        if result["geotag"] is not None:
            lat = result["geotag"][0]
            lon = result["geotag"][1]
        
        price = 0
        try:
            price = float(self.regexNonDec.sub('', result["price"]))
        except:
            pass
        
        listing = SqlListingHelper.Listing(
            link=result["url"],
            name=result["name"],
            created=parse(result["datetime"]),
            geotag=str(result["geotag"]),
            lat=lat,
            lon=lon,
            price=price,
            location=result["where"],
            cl_id=result["id"],
            area=result["area"],
        )
        
        self.session.add(listing)
        self.session.commit()