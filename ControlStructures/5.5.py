###
# Sums numbers entered by user
# arithmetic mean

total_sum = 0
mean = 0
iterator = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    iterator += 1
    total_sum += number
    mean = total_sum/iterator

print(f"The total sum of the numbers is: {total_sum} and arithmetic mean is {mean}.")