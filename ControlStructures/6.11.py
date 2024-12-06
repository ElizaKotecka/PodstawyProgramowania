# A computer program analyses the price of a product in an online store.
# If the product price decreases by at least 10%, the program prints a purchase recommendation.

current_price = 140.00
previous_price = 200.00

# Calculate percentage change
price_reduction = ((previous_price - current_price) / previous_price) * 100

if price_reduction >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {price_reduction:.0f}%")
else:
    print("No price reduction.")