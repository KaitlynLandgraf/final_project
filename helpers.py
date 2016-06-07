from operator import itemgetter
import csv
FACILITIES_FNAME = './static/data/geocoded_facilities.csv'

def get_facilities():
    with open(FACILITIES_FNAME, 'r') as f:
        newrows = []
        for row in csv.DictReader(f):
            if row['latitude'] and row['longitude']:
                newrows.append(row)
        return newrows

def filter_by_city(city, datarows):
    matches = []
    for c in datarows:
        if city.upper() == c['Facility City']:
                matches.append(c)
    return matches

def filter_by_county(county, datarows):
    matches = []
    for c in datarows:
        if county.upper() == c['County Name']:
                matches.append(c)
    return matches

def sort_by_status(status, datarows):
    matches = []
    if status == 'licensed':
        for c in datarows:
            if c['Facility Status'] == 'LICENSED':
                matches.append(c)
    elif status == 'closed':
        for c in datarows:
            if c['Facility Status'] == 'CLOSED':
                matches.append(c)
    elif status == 'pending':
        for c in datarows:
            if c['Facility Status'] == 'PENDING':
                matches.append(c)
    else:
        # i.e. 'alpha' or any value...just sort by last name, first name
        rows = sorted(datarows, key=itemgetter('Facility Name'))
    return matches
