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

# 7. 