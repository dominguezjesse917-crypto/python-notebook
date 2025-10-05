"""
Roll a dice multiple times (default: 1d6).
Run: python dice_roller.py
"""
import random

sides = input("How many sides? (default 6): ").strip()
rolls = input("How many rolls? (default 1): ").strip()

sides = int(sides) if sides.isdigit() and int(sides) > 1 else 6
rolls = int(rolls) if rolls.isdigit() and int(rolls) > 0 else 1

for i in range(1, rolls + 1):
    print(f"Roll {i}: {random.randint(1, sides)}")
