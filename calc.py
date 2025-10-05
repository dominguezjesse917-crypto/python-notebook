"""
Tiny 2-number calculator for + - * /.
Run: python simple_calculator.py
"""
a = float(input("Enter first number: "))
sym = input("Operator (+, -, *, /): ").strip()
b = float(input("Enter Second number: "))

if sym == "+":
    print(a + b)
elif sym == "-":
    print(a - b)
elif sym == "*":
    print(a * b)
elif sym == "/":
    if b == 0:
        print("Error: division by zero")
    else:
        print(a / b)
else:
    print("Unknown operator.")
