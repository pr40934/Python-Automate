# 16 - 01 - 2024

# functions

# 17 - 01 - 2024

def myFucntion():

    print('My Fucntion')

myFucntion() # calling My Function

def userFunctions(arug): # --> ParaMeter "arug"

    print("Hello " + arug)

userFunctions('Tim') # --> Arugments "Tim"
userFunctions('Bob') # --> Arugments "Bob"

import random
def getAnswer(answerNumber):

    print('answerNumber :: ',answerNumber)
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
    
r = random.randint(1, 9) # creating arugment
fortune = getAnswer(r)   # passing  argument
print(fortune)           # Printing OutPut


def NoneFunction():

    return None

getNone = NoneFunction()

print('getNone',getNone)

# Optional Parameters

print("pratap","Raju",sep='::') 

print('No New Line',end='....')

print('Second Line')

# Local And Gobal Scope

def spam():
    eggs = 99
    bacon()
    print("eggs :: ",eggs)

def bacon():
    eggs = 0
spam()


localvar = 100
def checkGlobal():

    print('first check :: ',localvar)
    localVar = 800
    print('Second check :: ',localvar)

checkGlobal()

def spam():
    print('first eggs :: ',eggs)

eggs = 42
spam()
print('Second eggs :: ',eggs)

# Global Statment

def makeGlobalVar(): # with out calling the Function 

    global makeGlobalVariable

    makeGlobalVariable = "Hello Every One"

makeGlobalVariable = 'Duplicate'

print('makeGlobalVariable :: ',makeGlobalVariable)

def spam(): # call the Function To create the Global Variable
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print('eggos :: ',eggs)