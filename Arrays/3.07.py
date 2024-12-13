# Create a program that prints the longest name 
# (consisting of the largest number of characters). Sample result:

# Names: Genowefa Onufry Celestyna Alojzy Pankracy
# Longest name: Celestyna

names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest_name = ''
for name in names:
    if len(name) > len(longest_name):
        longest_name = name
        
print(f"Names: {' '.join(names)}")
print(f"Longest name: {longest_name}")
