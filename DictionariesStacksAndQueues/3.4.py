import queue

def decimal_to_binary(number):
    stack = queue.LifoQueue()
    original_number = number 

    while number > 0:
        remainder = number % 2
        stack.put(remainder)
        number = number // 2
        
    binary_number = ""
    while not stack.empty():
        binary_number += str(stack.get())

    print(f"Natural number: {original_number}")
    print(f"Binary number: {binary_number}")

decimal_to_binary(18)
