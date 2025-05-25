def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32

def main():
    while True:
        try:
            # Get temperature value from the user
            temp_value = float(input("Input a number to convert for temperature: "))
            
            # Get the unit of the input temperature
            from_unit = input("What unit will the temperature be? (Celsius, Fahrenheit, Kelvin) ").capitalize()
            
            # Get the unit to convert to
            print("What unit should the temperature be converted to:")
            print("1. Fahrenheit")
            print("2. Celsius")
            print("3. Kelvin")
            choice = input()
            
            if choice == '1':
                to_unit = "Fahrenheit"
            elif choice == '2':
                to_unit = "Celsius"
            elif choice == '3':
                to_unit = "Kelvin"
            else:
                print("Invalid choice. Please try again.")
                continue
            
            # Convert the temperature
            converted_temp = convert_temperature(temp_value, from_unit, to_unit)
            
            # Print the result
            print(f"{temp_value} {from_unit} will be converted to {converted_temp:.2f} {to_unit}.")
            
            # Ask the user if they want to convert another
            print("Would you like to convert another?")
            print("1. Convert Another")
            print("2. Exit Program")
            choice = input()
            
            if choice == '2':
                print("Exiting program.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()