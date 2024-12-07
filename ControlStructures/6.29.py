# A natural number greater than 1
# is called a prime if it has exactly 2 natural factors
# with the values 1 and this number.
# Write a program that finds N leading prime numbers.

N = int(input("Enter the number of prime numbers you want to find: "))
number = 2
count = 0

while count < N:
    is_prime = True
    for x in range (2, number):
        if number % x  == 0:
            is_prime = False
            continue
    if is_prime:
        print(number)
        count += 1
    number += 1