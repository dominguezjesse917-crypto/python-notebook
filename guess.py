"""
02_guess_the_number.py — capped at 5 guesses, range 1..15
Run: python 02_guess_the_number.py
"""
import random

MAX_GUESSES = 5
LOW, HIGH = 1, 15

def ask_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a whole number.")

def play_once(low=LOW, high=HIGH, max_guesses=MAX_GUESSES) -> int:
    secret = random.randint(low, high)
    print(f"I'm thinking of a number between {low} and {high}. You have {max_guesses} tries.")
    for n in range(1, max_guesses + 1):
        guess = ask_int(f"Guess {n}/{max_guesses}: ")
        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Correct! It was {secret}. You needed {n} guesses.")
            return n
    print(f"Out of guesses! The number was {secret}.")
    return max_guesses

def main():
    print("=== Guess the Number (1–15, 5 tries) ===")
    while True:
        play_once()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
