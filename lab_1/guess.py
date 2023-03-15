# Zan's answer to Guess the Number game.

from random import randint


secret_num = randint(1, 10)

print("I am thinking of a number between 1 and 10.")
guess = input("What is the number?")

print(f'The number was {secret_num}.')
print(f'You guessed {guess}')