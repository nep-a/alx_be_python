FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    
def convert_to_fahrenheit(celsius) :
    return (celsius + 32) * CELSIUS_TO_FAHRENHEIT_FACTOR

def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input)
        unit =input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        if unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f'{temperature}C is {converted}F')
        elif unit == "F":
            converted = convert_to_fahrenheit(temperature)
            print(f'{temperature}F is {converted}C')
        else:
            raise ValueError("Invalid option")
    except ValueError as e:
        print(f"Error: {e}")
        print("Invalid temperature. Please enter a numeric value.")
if __name__== "__main__":
    main()