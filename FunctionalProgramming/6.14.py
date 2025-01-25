bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]

capacity = 500
tolerance = 0.02


lower_limit = capacity * (1 - tolerance)
upper_limit = capacity * (1 + tolerance)

incorrect_bottles = list(filter(lambda x: x < lower_limit or x > upper_limit, bottles))
incorrect_count = len(incorrect_bottles)
total_bottles = len(bottles)
incorrect_percentage = (incorrect_count / total_bottles) * 100


print(f"Bottle capacity:    {capacity} ml")
print(f"Filling tolerance:  {tolerance * 100} %")
print(f"Filled bottles:     {', '.join(map(str, bottles))}")
print(f"Incorrectly filled: {incorrect_percentage:.0f}%")