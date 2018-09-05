def kelvin_to_celsius(temp):
	return temp - 272.15

def celcius_to_fhar(temp):
	return temp * (9/5) + 32

def kelvin_to_fhar(temp):
	temp_c = kelvin_to_celcius(temp)
	result = celcius_to_fhar(temp_c)
	return result

print('test')