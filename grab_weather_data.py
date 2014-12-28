import urllib2
import sys
import json
from kelvin_to_fahrenheit import *

def grabWeatherData(city="Escondido", country="us"):
	data = urllib2.urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country)
	return data.read()

weather =  grabWeatherData()
print weather

weather = json.loads(weather)
print "Temp (F): " + str(calculateF(float(weather["main"]["temp"])))
