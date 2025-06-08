# temp_conversion_tool.py
# Oughlane

FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0
FREEZING_POINT_FAHRENHEIT = 32.0

# Conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - FREEZING_POINT_FAHRENHEIT) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_FAHRENHEIT

# interaction
def main():
    try:
        temp = float(input("Enter the temperature value: "))
        unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

        if unit == "F":
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result:.2f}°C")
        elif unit == "C":
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result:.2f}°F")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid input. Please enter a numeric temperature.")


if __name__ == "__main__":
    main()
