#1
###
# Printing student's personal data
#
name = "Adam"
height = 170
age = 27
print(f"My name is {name}.")
print(f"I am {age} years old, and my height is {height} cm.")
print(f"In 6 years I will be {age+6} years old.")

#2
###
# Write a program that calculates and prints
# the income of a family per person. To print the results
# in a readable form, use f-strings.
#
father_income = 5450
mother_income = 4920
family_members = 5
total_income = father_income + mother_income
income_per_person = total_income/5
print(f'Total family income is {total_income}, and income per person is {income_per_person}')

#3
###
# Program that prints the following expression containing the values of these variables and the value of the expression.
a = 3
b = 5
print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a+b}')
print(f'{a}/{b}={a/b}')