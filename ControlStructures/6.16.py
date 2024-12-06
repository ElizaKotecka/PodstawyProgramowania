# Write a program that calculates and prints the total washing time.

total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')

if program == 'j':
    total_washing_time += 40 
elif program == 'u':
    total_washing_time += 70
elif program == 's':
    total_washing_time += 20

extra_rinse = input('Extra rinse? (y/n): ')
if extra_rinse == 'y':
    total_washing_time += 15

extra_spin = input('Extra spin? (y/n): ')
if extra_spin == 'y':
    total_washing_time += 9

print(f'Total washing time: {total_washing_time} minutes.')