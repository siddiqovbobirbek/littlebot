from geopy.geocoders import Nominatim
def manzil(latitude, longitude):
    geolocator = Nominatim(user_agent = "Bobirbek")
    location = geolocator.reverse(f'{latitude}, {longitude}')
    return location.address