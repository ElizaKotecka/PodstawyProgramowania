# Write a program that generates and prints a random number between 1 and 6,
# similar to rolling a dice.

from random import randrange

for _ in range(10):
    print(randrange(1,7))