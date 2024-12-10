from range import check_range

number = 7
x = 9
y = 15

print(f"A number: {number}.")
print(f"Number {number} in range <{x},{y}>: {'yes' if check_range(number, x, y) else 'no'}")