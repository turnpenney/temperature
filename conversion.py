def kelvin_to_celsius(temp):
	return temp - 272.15
	""""
	convert a temp from  Celsius to F
	""""

def celsius_to_fhar(temp):
	return temp * (9/5) + 32

def kelvin_to_fhar(temp):
	temp_c = kelvin_to_celcius(temp)
	result = celcius_to_fahr(temp_c)
	return result

print('test')