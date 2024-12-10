# An expression contains operators for adding and subtracting single-digit numbers.
# Define a function f(expression) that returns the value of the expression. 

def f(expression):
    return eval(expression)

# def f(expression):
#     result = 0 
#     current_number = 0   
#     current_operator = '+'

#     for char in expression + '+': 
#         if char.isdigit():
#             current_number = int(char)  
#         elif char in '+-':
#             if current_operator == '+':
#                 result += current_number 
#             elif current_operator == '-':
#                 result -= current_number 

#             current_operator = char

#     return result

if __name__ == '__main__':
    print(f("2+3"))
    print(f("3+8+1"))
    print(f("2+3-4+5-0"))