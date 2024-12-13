###
# Checks the correctness of username and password
# username is at least 6 characters long
# username contains only lowercase letters
# password is at least 8 characters long
# password contains only letters (lowercase and uppercase), numbers, and the underscore character

import re

# read username and password from keyboard
username = input('Enter username: ')
password = input('Enter password: ')

# pattern (criteria) for username and password
username_pattern = '^[a-z]{6,}$'
password_pattern = '^\w{8,}$'

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern,password)

# print results
if username_match and password_match:
   print('Password and username meet requirements.')
else:
   print('Password or username not meet requirements.')
   