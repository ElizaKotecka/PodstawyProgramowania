# Returns True if at least 3 people were in the room at the same time,
# or False otherwise.

def f(detector):
    current_count = 0
    max_count = 0

    for char in detector:
        if char == '+':
            current_count += 1
        elif char == '-':
            current_count -= 1

        max_count = max(max_count, current_count)

    # Return True if max_count is 3 or more
    return max_count >= 3

if __name__ == '__main__':
    print(f("+-+++-+---"))  # True
    print(f("+-+-+-+-"))    # False
    print(f("+-++-+--"))    # False
    print(f("+-++-++-+---")) # True


