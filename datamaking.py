from geocoder import geocode
import csv

SOURCE_FILENAME = './static/data/AdultResidentialFacilities06052016.csv'
OUTPUT_FILENAME = 'static/data/geocoded_facilities.csv'

# Open the old data
with open(SOURCE_FILENAME, 'r') as f:
    facilities = []
    for row in csv.DictReader(f):
            facilities.append(row)

xcount = 0
# now we geocode
for f in facilities:
    xcount += 1
    address = f['Facility Address']
    city = f['Facility City']
    coordinates = geocode(address, city)
    f['latitude'] = coordinates['latitude']
    f['longitude'] = coordinates['longitude']
    print(xcount, address, city, coordinates)

print("Geocoding all done!")

the_headers = list(facilities[0].keys())

with open(OUTPUT_FILENAME, 'w') as wfile:
    c = csv.DictWriter(wfile, fieldnames=the_headers)
    c.writeheader()
    c.writerows(facilities)
