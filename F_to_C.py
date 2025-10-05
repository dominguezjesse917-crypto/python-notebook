"""
Convert between Celsius and Fahrenheit.
Run: python temp_converter_simple.py
"""
choice = input("Type 'C' to convert to Celsius or 'F' to Fahrenheit: ").strip().upper()
value = float(input("Enter the temperature value: "))

if choice == "F":
    # C -> F
    result = value * 9/5 + 32
    print(f"{value} °C = {result:.2f} °F")
elif choice == "C":
    # F -> C
    result = (value - 32) * 5/9
    print(f"{value} °F = {result:.2f} °C")
else:
    print("Please choose 'C' or 'F'.")
