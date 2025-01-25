from functools import reduce

numbers = [2, 4, 6, 3, 7, 5]

even_numbers = filter(lambda x: x % 2 == 0, numbers)
total = reduce(lambda x, y: x + y, even_numbers)
print(total)
