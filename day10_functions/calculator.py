"""
calculator.py

A simple calculator module for performing basic arithmetic operations.
Functions may include addition, subtraction, multiplication, and division.

Author: [Your Name]
Date: 2025-09-22
"""
def add(x, y):
    """Return the sum of x and y."""
    return x + y

def substract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):

    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y. Raises ValueError on division by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

#operations = ["add", "substract", "multiply", "divide"]

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


num1 = float(input("What is the first number? "))
should_continue = True
while should_continue:

    for symbol in operations:
        print(symbol)

    operation_symbol = input("What is the operation? type the symbol: " )
    num2 = float(input("What is the second number? "))

    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if choice == 'y':
        num1 = answer
    else:  
        should_continue = False


