# Write a program that allows you to convert time in 24-hour format to 12-hour format.

time_24 = input("Enter time in 24-hour format (hh:mm): ")

hours = time_24[:2]
int_hours = int(hours)
minutes = time_24[3:5]


if int_hours >= 12:
    period = "pm"
    if int_hours > 12:
        int_hours -= 12
else:
    period = "am"
    if int_hours == 0:
        hours = 12

print(f"Time in 12-hour format: {int_hours}:{minutes} {period}.")