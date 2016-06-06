from helpers import get_facilities
from helpers import filter_by_city, filter_by_county, sort_by_status

facilities = get_facilities()

def just_do_it(city="", county="", sortby="alpha"):
	matched_rows = []
	datarows = facilities
	if city:
		filteredrows = filter_by_city(city, facilities)
	else:
		filteredrows = filter_by_county(county, facilities)
	return sort_by_status(sortby, filteredrows)

def print_record_count():
	print("there are", len(facilities), 'residential care facilities')