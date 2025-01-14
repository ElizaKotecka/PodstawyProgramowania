price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

print("Prices before discount:")
for product, price in price_list.items():
    print(f"{product:<10}{price:.2f}$")

total_before_discount = sum(price_list.values())
print(f"\nTotal value before discount: {total_before_discount:.2f}$")

discount = 0.10
for product in price_list:
    price_list[product] = (price_list[product] * (1 - discount))

print("\nPrices after discount:")
for product, price in price_list.items():
    print(f"{product:<10}{price:.2f}")

total_after_discount = sum(price_list.values())
print(f"\nTotal value after discount: {total_after_discount:.2f}$")