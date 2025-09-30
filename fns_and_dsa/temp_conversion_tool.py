FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
	return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
	return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def userPrompt():
	value = input("Enter the temperature to convert: ")
	try:
		value = float(value)
	except ValueError:
		return print("Invalid temperature. Please enter a numeric value.")
	temp = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
	if temp.lower() != "c" and temp.lower() != "f":
		print("Temperature must be in celsius or fahrenheit (c or f)")
		return
	match temp.lower():
		case "c":
			return print(f"{value}°C is {convert_to_fahrenheit(value)}°F")
		case "f":
			return print(f"{value}°F is {convert_to_celsius(value)}°C")

userPrompt()
