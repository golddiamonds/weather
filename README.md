weather
=======

Python Weather Grabber

No special modules are needed at the moment. Currently downloads weather for Escondido, CA, USA. But it's setup to grab weather for whatever city/country you'd like.

There are two functions that are useful:

- calculateF(kelvin)
This will change whichever kelvin value (make sure it's a float) to a fahrenheit value. A Celsius function would be even easier to make.

- grabWeatherData(city, country)
This function will grab weather information from the OpenWeatherMap Rest API.

