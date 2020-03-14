from googlemaps import Client as GoogleMaps

def ReqCoordenates(request, address):
    api_key = "AIzaSyDspZ6IEQmnOhK87N6a9hYjbFfnzSjhm-M"
    gmaps = GoogleMaps(api_key)
    lat, lng = gmaps.address_to_latlng(address)
    return lat, lng