# 17 - 01 - 2024
# 08 : 24 PM

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print('ZERO :: ',spam(0))
print(spam(1))

# 18 - 01 - 2024

# 1. Why are functions advantageous to have in your programs?

# Preventing the duplicate code & re Usebullity

# 2. When does the code in a function execute: when the function is
# defined or when the function is called?

def callAFunction():
    print('Who"s that')

callAFunction()

# 3. What statement creates a function?

def statementfun():
    pass

# 4. What is the difference between a function and a function call?

def createFunc():
    print('I Created a Function')

createFunc() # Calling function to Excuite 

# 5. How many global scopes are there in a Python program? How many
# local scopes?

# one 

# 6. What happens to variables in a local scope when the function call returns?

# they are become empty

# 19 - 01 - 2024

# 7. What is a return value? Can a return value be part of an expression?

# return value is function return any data is called return value 
#  yes return value can be particpate in any expression and condition.

# 8. If a function does not have a return statement, what is the return value
# of a call to that function?

# that doesn't return any thing it just excuites

# 9. How can you force a variable in a function to refer to the global variable?

# Global variableName

global_variable = 10

def use_global_variable():
    global global_variable
    global_variable += 5
    print("Inside the function:", global_variable)

use_global_variable()

print("Outside the function:", global_variable)

# 10. What is the data type of None?

result = None
print(type(result))  # Output: <class 'NoneType'>

# 11. What does the import areallyourpetsnamederic statement do?

# use to import libary's to you code

# 12. If you had a function named bacon() in a module named spam, how
# would you call it after importing spam?

# first  Way
# import spam as sp
# sp.bacon()

# Second Way 
# import spam as sp
# sp.bacon()

# 13. How can you prevent a program from crashing when it gets an error?

def errorHandling():
    try:
        my_list = [1, 2, 3]
        print(my_list[3])

    except Exception:               
        print('error Handling Function')

errorHandling()

# 14. What goes in the try clause? What goes in the except clause?

# try clause  try to run code in a try clause block in any case it get any error it run except code block
 
