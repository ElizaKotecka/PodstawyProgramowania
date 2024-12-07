# time_string(15, 38, '24') returns '15:38'
# time_string(8, 3, '24') returns '08:03'
# time_string(0, 5 '24') returns '00:05'
# time_string(11, 15, '12') returns '11:15am'
# time_string(0, 7, '12') returns '12:07am'
# time_string(7, 30, '12') returns '7:30am'
# time_string(12, 46, '12') returns '12:46pm'
# time_string(13, 10, '12') returns '1:10pm'
# time_string(19, 2, '12') returns '7:02pm'


def time_string(hours, minutes, time_format):

    if time_format == '12':
        if hours == 0:
            if minutes <= 9:
                return f'12:0{minutes}am'
            else:
                return f'12:{minutes}am'
        
        elif hours == 12:
            if minutes <= 9:
                return f'12:0{minutes}am'
            else:
                return f'12:{minutes}pm'
        elif hours > 12:
            hours -= 12
            if minutes <= 9:
                return f'{hours}:0{minutes}pm'
            else:
                return f'{hours}:{minutes}pm'
        elif hours <= 12:
            if minutes <= 9:
                return f'{hours}:0{minutes}am'
            else:
                return f'{hours}:{minutes}am'

            
    if time_format == '24':
        if hours <= 9:
            if minutes <= 9:
                return f'0{hours}:0{minutes}'
            else:
                return f'0{hours}:{minutes}'
        else:
            if minutes <=9:
                return f'{hours}:0{minutes}'
            else:
                return f'{hours}:{minutes}'


print(time_string(15, 38, '24'))
print(time_string(8, 3, '24'))
print(time_string(0, 5, '24'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12'))

