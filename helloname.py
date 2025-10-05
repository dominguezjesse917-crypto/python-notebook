"""
Ask for a name and say hello.
Run: python hello_name.py
"""
name = input("What's your name? ").strip()
if name:
    print(f"Hello, {name}!")
else:
    print("Hello there!")
