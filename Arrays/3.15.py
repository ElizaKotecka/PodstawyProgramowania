# Write a program that prints the tuple (10,20,30,40,50) 
# in reverse order. Sample result:

t = (10,20,30,40,50)

print('Tuple: ', end="")
for elem in t:
 print(elem, end=' ')
      
print()

print('Reverse order: ', end="")
for elem in t[::-1]:
    print(elem, end= " ")
# Tuple: 10,20,30,40,50
# Reverse order: 50,40,30,20,10