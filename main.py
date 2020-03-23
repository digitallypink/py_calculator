"""
 Extend a simple calculator. Add and Subtract has been included for you.
 Your mission. If you choose to accept it, is to add the following functionality to this program.
   1. Division
   2. Multiplication

 To run this program (I am assuming you have python installed on a windows machine.)
   1. Open the command line terminal.
       The quickest way is to enter WINDOWS KEY + R.
       When the Run dialog is open type cmd then Enter.
   2. Navigate to your project folder in the terminal. `cd <Location of this file on your system>`
   3. type `python3 main.py` and Enter.

 Ask all questions on digitallypink.slack.com
"""

# Math Operations

# Add two numbers
def add(x, y):
    return x + y


# Subtract two numbers
def subtract(x, y):
    return x - y


# Add other functions here that perform math operations.

# Take operation input from user. The 'input' function is used to receive input from the user.
operation = input("Enter operation (e.g. + or -): ")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

# Using if statements to perform the desired operation
if operation == '+':
    print(x, operation, y, "=", add(x, y))
elif operation == '-':
    print(x, operation, y, "=", subtract(x, y))
# Add other conditions following the examples above
# The else below happens when no condition has been met
else:
    print("Invalid Input.", "Cannot perform: ", x, operation, y)
