def avg_speed(distance,hours,minutes):
    time = hours + minutes/60
    return distance/time

distance = int(input('Enter distance in km:'))
hours = int(input('Enter number of travel hours:'))
minutes = int(input("Enter number of travel minutes:"))

print(f'Average speed: {avg_speed(distance, hours, minutes):.1f} km/h')
