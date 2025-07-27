CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def celsius_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def main():
    try:
        value = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            result = celsius_to_fahrenheit(value)
            print(f"{value}°C is {result:.2f}°F")
        elif unit == 'F':
            result = fahrenheit_to_celsius(value)
            print(f"{value}°F is {result:.2f}°C")
        else:
            print("Invalid unit. Please enter C or F.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
