import requests
API_KEY = open('mapzenkey.txt').read().strip()

BASE_URL = 'https://search.mapzen.com/v1/search'
BOUNDING_BOX = {
    'boundary.rect.min_lat': 32.53,
    'boundary.rect.max_lat': 42.01,
    'boundary.rect.min_lon': -124.42,
    'boundary.rect.max_lon': -114.13
}


def geocode(address, city):
    lat = None
    lng = None
    address_text = address + ', ' + city + ', CA'
    myparams = {'api_key': API_KEY, 'size': 1,
               'text': address_text}
    myparams.update(BOUNDING_BOX)

    try:
        resp = requests.get(BASE_URL, params = myparams)
        data = resp.json()
        features = data['features']
        if features:
            lng, lat = features[0]['geometry']['coordinates']
        return {'longitude': lng, 'latitude': lat}
    except Exception as err:
        print("Oops error", err)
        return {'longitude': None, 'latitude': None}
