# In one of the online stores, a 25% discount is charged for each product purchased over two.
# Write a program that calculates the amount to be paid. 

numb_products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

total_price = numb_products * product_price

if numb_products > 2:
    discount = 0.25 * (numb_products - 2) * product_price
    total_price -= discount

print(f"Amount to pay: {total_price:.2f}")