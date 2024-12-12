# Returns a number specifying the number of dice rolled the most times in a row.

def f(dice):
    prev_number = dice[0] # Remember previous number
    counter = 1
    max_len_of_sequence = 1 
    num_in_max_len = dice[0] # Number in longest sequence
    for x in dice[1:]:
        if x == prev_number:
            counter += 1
        else:
            if max_len_of_sequence < counter:
                max_len_of_sequence = counter
                num_in_max_len = prev_number
                counter = 1
        prev_number = x
    if max_len_of_sequence < counter: # If the longest sequence at the end
        max_len_of_sequence = counter
        num_in_max_len = prev_number
    return num_in_max_len


# Test cases
print(f("5233165554211"))  # Expected output: 5
print(f("2133"))  # Expected output: 3