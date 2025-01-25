names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']


print('Sorted list:')
sorted_names = sorted(names, key=lambda name: len(name))
for name in sorted_names:
    print(name)