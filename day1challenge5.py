'''
challenge 5

Write a Python program to guess a number betwen 1 and 9.
(user is to guess what the computer is 'thinking')

'''
import random

wrongGuess=True
guess=str(random.randint(1,9))

while wrongGuess:
    if input("Guess a number ") == guess:
        wrongGuess=False
        print("You guessed it!")
        break
    else:
        print("Try again.")
        continue