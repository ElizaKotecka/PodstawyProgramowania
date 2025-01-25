avg_speed= lambda distance, hours, minutes : distance/ (hours + minutes/60)

distance = int(input('Enter distance in km:'))
hours = int(input('Enter number of travel hours:'))
minutes = int(input("Enter number of travel minutes:"))

print(f'Average speed: {avg_speed(distance, hours, minutes):.1f} km/h')