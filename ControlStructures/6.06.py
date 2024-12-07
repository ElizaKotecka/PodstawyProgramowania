# The parking meter calculates the parking fee based on the number of hours the car was parked according to the following rules:

# 1-2 hours: 5 PLN
# 3-6 hours: 15 PLN
# Over 6 hours: 20 PLN

hours_parked = float(input("Enter the number of hours parked: "))

# Calculate parking fee
if 1 <= hours_parked <= 2:
    fee = 5
elif 3 <= hours_parked <= 6:
    fee = 15
elif hours_parked > 6:
    fee = 20
else:
    fee = 0

# Print the parking fee
if fee > 0:
    print(f"The parking fee is: {fee} PLN")
else:
    print("Invalid number of hours.")