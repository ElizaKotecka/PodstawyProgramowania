# Write a program that counts the number of occurrences 
# of any value from a tuple. Sample result:

# Tuple: 50,20,40,50,30,50
# Value: 50
# Number of occurrences: 3

T = (50, 20, 40, 50, 30, 50)
val = 50
count = 0
for i in T:
    if i == val:
        count += 1

print(f"Tuple: {T}")
print(f"Value: {val}")
print(f"Number of occurrences: {count}")