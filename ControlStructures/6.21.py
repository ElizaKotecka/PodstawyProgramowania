# Write a program showing any amount (natural number) read from the keyboard with as few coins as possible.

amount = int(input("Enter the amount in PLN: "))

original_amount = amount

coins_5 = 0
coins_2 = 0
coins_1 = 0

coins_5 = amount // 5
amount %= 5

coins_2 = amount // 2
amount %= 2

coins_1 = amount

print(f"The amount of {original_amount} PLN in coins:")
print(f"5 PLN coins: {coins_5}")
print(f"2 PLN coins: {coins_2}")
print(f"1 PLN coins: {coins_1}")