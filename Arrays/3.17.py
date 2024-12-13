# Write a program that counts the number of occurrences 
# of any value from a tuple. Sample result:

# Tuple: 50,20,40,50,30,50
# Value: 50
# Number of occurrences: 3

t = (50, 20, 40, 50, 30, 50)
val = 50
count = 0
t_list = []

for i in t:
    if i == val:
        count += 1

for i in t:
    t_list.append(str(i))

        

print(f"Tuple: {','.join(t_list)}")
print(f"Value: {val}")
print(f"Number of occurrences: {count}")