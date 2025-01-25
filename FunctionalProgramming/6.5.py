
numbers = list(range(1, 21))

divisible_numbers = list(filter(lambda x: x % 6 == 0, numbers))

print("Numbers divisible by 2 and 3:", divisible_numbers)
