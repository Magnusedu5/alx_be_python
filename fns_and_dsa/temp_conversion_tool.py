FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    temp_in_F = temperature
    temp_in_C = (temp_in_F - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{temp_in_F}°F is {temp_in_C}°C")

def convert_to_fahrenheit(celsius):
    temp_in_C = temperature
    temp_in_F = (temp_in_C * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{temp_in_C}°C is {temp_in_F}°F")

temperature = float(input("Enter the temperature to convert: "))
temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if temp_unit == 'C':
    convert_to_fahrenheit(celsius=temperature)
elif temp_unit == 'F':
    convert_to_celsius(fahrenheit=temperature)
else:
    print("Value Error")


