import re

# Function to perform the arithmetic operations
def calculate(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"Error: {str(e)}"

# Function to validate the input expression
def is_valid_expression(expression):
    # Check for valid characters in the expression
    if not re.match(r'^[0-9+\-*/().\s]*$', expression):
        return False

    # Check for balanced parentheses
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

print("Welcome to the Simple Command-Line Calculator!")
print("Enter mathematical expressions, and I will calculate the result.")
print("Type 'q' to quit.")

# infinite while loop that allows the user
#  to enter expressions until they type 'q' to quit.
while True:
    user_input = input("Enter an expression: ")
    
    if user_input.lower() == 'q':
        print("Goodbye! Thanks for using the calculator.")
        break
    
    if is_valid_expression(user_input):
        result = calculate(user_input)
        print("Result:", result)
    else:
        print("Invalid input. Please enter a valid expression.")
