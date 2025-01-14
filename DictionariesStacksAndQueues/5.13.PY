import queue

def calculate_rpn():
    stack = queue.LifoQueue()
    operator = ['+', '-', '*', '/']

    while True:
        value = input("Enter a number, operator (+, -, *, /), or '=' to calculate: ")
        
        if value.isdigit():
            stack.put(int(value))
        elif value in operator:
            if stack.qsize() < 2:
                    return "Error: Not enough operands."

            
            last = stack.get()
            second_last = stack.get()
            
            if value == "+":
                result = second_last + last
            elif value == "-":
                result = second_last - last
            elif value == "*":
                result = second_last * last
            elif value == "/":
                if last == 0:
                    return "Error: Division by zero is not allowed."

                result = second_last / last
            
            stack.put(result)

        elif value == "=":
                if stack.empty():
                    return "Error: No result to display."
                elif stack.qsize() > 1:
                    return "Error: Too many operands. Check your expression."
                else:
                    return f"Result: {stack.get()}"
        else:
            return "Invalid input. Please enter a number, an operator, or '='."

if __name__=='__main__':
    print("Calculate RPN expressions:")
    print("Example inputs: 2, 3, +, =")
    print(calculate_rpn())

# 2 3 + =
# 2 4 1 + * =
# 2 3 + 4 5 + * =
# 8 3 1 + / 3 2 - 4 + * =