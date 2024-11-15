#1
###
# A program that calculates the number of characters
# of your name, surname and full name
#

name = 'Eliza'
surname = 'Kotecka'
characters_in_name = len(name)
print(f'Your name "{name}" has {characters_in_name} characters.')
print(f'Your surname "{surname}" has {len(surname)} characters.')
print(f'Your full name "{name+" "+surname}" has {len(name)+len(surname)} characters.')

#2
###
# A program that prints your initials
#
name = 'Eliza'
surname = 'Kotecka'
print(f"My initials: {name[0]+surname[0]}.")

#3
###
# A program that prints a university abbreviation
#   
university = "Krakow University of Economics"
print(f"Abbrevation of my university name: {university} is {university[0]+university[7]+university[21]}.")

#4
###
# A program for printing detailed information.
#
employee = "Mr. John May, born on 1998-02-16"
print(f'Name: {employee[4:8]}')
print(f'Surname: {employee[9:12]}')
print(f'Born: {employee[22:33]}')
print(f'Initials: {employee[4]+employee[9]}')

#5
###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone= input('Enter phone number: ')
print(f'Your phone number is: {phone[:3]}-{phone[3:6]}-{phone[6:]}.')

#6
###
# A program to print numerical representations of characters.
# a, b, z, A, B, Z, 1, =, +, €
print(f"a {ord('a')}")
print(f"b {ord('b')}")
print(f"z {ord('z')}")
print(f"A {ord('A')}")
print(f"B {ord('B')}")
print(f"Z {ord('Z')}")
print(f"1 {ord('1')}")
print(f"= {ord('=')}")
print(f"+ {ord('+')}")
print(f"€ {ord('€')}")

#7
###
# A program that prints a numerical representation of each letter of your name.
#
name = 'Eliza'
print(f'The letter {name[0]} has a code {ord(name[0])}')
print(f'The letter {name[1]} has a code {ord(name[1])}')
print(f'The letter {name[2]} has a code {ord(name[2])}')
print(f'The letter {name[3]} has a code {ord(name[3])}')
print(f'The letter {name[4]} has a code {ord(name[4])}')

#8
###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
print(first_letter_code)
print(last_letter_code)
number_of_letters = max(
    first_letter_code-last_letter_code-1,   # first > last eg. first=Z, last=A result > 0
    last_letter_code-first_letter_code-1,   # first < last eg. first=A, last=Z result > 0
    0                                       # first = last
)

print(f'Between {first} and {last} is {number_of_letters} letters.')

#9
###
# Character code conversion
# 67, 111, 108, 33

print(chr(67), chr(111), chr(111), chr(108), chr(33))

#10
###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print(movie.upper())

# print title in small letters
print(movie.lower())

# print how many times the vowel "e" appears in the title
print(movie.count('e'))

# print where in the text is the word "Lord"
print(movie.find('Lord'))

# print where in the text is the word "dragon"
print(movie.find('dragon'))