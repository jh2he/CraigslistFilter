# from craigslist import CraigslistHousing

# cl = CraigslistHousing(site='toronto', area='tor', category='apa', filters={'max_price': 2000, 'min_price': 1000})
                       
# results = cl.get_results(sort_by='newest', geotagged=True, limit=20)


for result in results:
    geotag = result["geotag"]
    area_found = False
    area = ""
    for aname, acoord in neighbourhoods.items():
        


