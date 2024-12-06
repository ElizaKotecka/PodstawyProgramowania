# Write a program that calculates a dog's age in dog's years.

dog_human_years = int(input("Enter the dog's age in human years: "))

if dog_human_years <= 2:
    dog_years = dog_human_years * 10.5
else:
    dog_years = 2 * 10.5 + (dog_human_years - 2) * 4

# Display the result
print(f"The dog's age in dog's years is {dog_years} years.")