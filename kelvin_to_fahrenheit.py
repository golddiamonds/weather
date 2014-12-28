import sys

k = 288.88 #test value

def calculateF( k ):
	return (((k - 273.15) * 1.8000) + 32.00)


if __name__ == "__main__":
	if len(sys.argv) == 1:
		print 'testing...k at ' + str(k) + ' is f =>'
		print calculateF(k)
	elif len(sys.argv) == 2:
		print calculateF(float(sys.argv[1]))
	else:
		print 'error. use the following:'
		print 'python kelvin_to_fahrenheit.py kelvin_temp'

