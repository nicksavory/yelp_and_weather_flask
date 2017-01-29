import forecastio
from geopy.geocoders import Nominatim
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

address = 'Dallax, TX'

def get_weather(address):

	api_key = os.environ['API_KEY']
	# Init geo
	geolocator = Nominatim()

	# Address
	location = geolocator.geocode(address)

	# Shorten
	latitude = location.latitude
	longitude = location.longitude

	# Init API
	forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()

	# Return weather
	return "{} and {}°F".format(forecast.summary, forecast.temperature)