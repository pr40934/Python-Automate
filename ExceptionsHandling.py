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
 
# 20 - 01 - 2024

# 21 - 01 - 2024

# Practice Projects

# The Collatz Sequence

# Write a function named collatz() that has one parameter named number. If
# number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.
# Then write a program that lets the user type in an integer and that keeps
# calling collatz() on that number until the function returns the value 1.
# (Amazingly enough, this sequence actually works for any integer—sooner
# or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t
# sure why. Your program is exploring what’s called the Collatz sequence, some-
# times called “the simplest impossible math problem.”)
# Remember to convert the return value from input() to an integer with
# the int() function; otherwise, it will be a string value.
# Hint: An integer number is even if number % 2 == 0, and it’s odd if
# number % 2 == 1.

def userInput():
    try:

        userValue = int(input('Enter Number :: '))
        calculateFunction(userValue)

    except:
        print('Exception in Input')


def calculateFunction(userValue):

    if userValue % 2 == 0:
        finallValue = userValue // 2
        print("finallValue : ",finallValue)
        
    else:
        finallValue = 3 * userValue + 1

        print("finallValue : ",finallValue)

    if finallValue != 1:
            userInput()
    
userInput()