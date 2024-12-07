###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed

import keyboard_

#Reads employee's data from keyboard
first_name = keyboard_.input_string('Enter name: ')
last_name = keyboard_.input_string('Enter last name: ')
age = keyboard_.input_integer('Enter age: ')
salary = keyboard_.input_real('Enter salary: ')
is_salary_hidden = keyboard_.input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print(f'Name: {first_name}', f'Last name: {last_name}')
print(f'Age: {age}')
if is_salary_hidden:
    print('Salary hidden.')
else:
    print(f'Salary: {salary}')