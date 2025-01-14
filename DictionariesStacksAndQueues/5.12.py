import queue

def reverse_string_with_stack(string):
    stack = queue.LifoQueue()
    
    for char in string:
        stack.put(char)
    
    reversed_string = ""
    while not stack.empty():
        reversed_string += stack.get()
    
    return reversed_string

if __name__=='__main__':
    text = input("Enter the text to reverse: ")
    reversed_text = reverse_string_with_stack(text)
    print("Reversed text:", reversed_text)
