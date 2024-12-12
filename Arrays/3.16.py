
# Prints values:
# “Seven”
# 30

t = ("Seven", [10, 20, 30], (5, 15, 25))

print(t[0])

counter = 1
for elem in t[1]:
    if counter == 3:
        print(elem)
    counter += 1

if elem in t[1] == 30:
    print(elem)


