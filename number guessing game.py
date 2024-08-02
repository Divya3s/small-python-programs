import random
import math

def number_guessing_game():
  lower_bound = 1
  upper_bound = 100
  secret_number = random.randint(lower_bound, upper_bound)
  attempts = 0

  print("Welcome to the Number Guessing Game!")
  print(f"Guess a number between {lower_bound} and {upper_bound}")

  while True:
    try:
      guess = int(input("Enter your guess: "))
      attempts += 1

      if guess < secret_number:
        print("Too low! Try again.")
      elif guess > secret_number:
        print("Too high! Try again.")
      else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break

    except ValueError:
      print("Invalid input. Please enter a number.")

number_guessing_game()