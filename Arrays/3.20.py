# Write a program to separate even and odd numbers of a given array of integers. 
# Put all even numbers first, and then odd numbers.

# Sample result:

# arr = [7,9,2,4,5,6]
# ...
# ...
# arr = [2,4,6,7,9,5]


arr = [7,9,2,4,5,6]
even = []
odd = []

for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

arr_joined = even + odd

print(f'arr = {arr_joined}')
print(f'even = {even}')
print(f'odd = {odd}')
print(f'joined = {arr_joined}')
