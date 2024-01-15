# 1. What are the two values of the Boolean data type? How do you
# write them?

True and False

# 2. What are the three Boolean operators?

'or' 'and' 'not'

# 3. Write out the truth tables of each Boolean operator (that is, every
# possible combination of Boolean values for the operator and what
# they evaluate to).

"and"

True and True == True

True and False == False

False and True == False

False and False == False

"or"

True or False == True

False or True == True

True or True == True

False or False == False

"not"

not True == False

not False == True

# 4. What do the following expressions evaluate to?
(5 > 4) and (3 == 5)                  #False
not (5 > 4)                           # False
(5 > 4) or (3 == 5)                   # True
not ((5 > 4) or (3 == 5))             # False
(True and True) and (True == False)   # False
(not False) or (not True)             # True

# 5. what are six Comparsion Operators ?

"==" ">=" "<=" ">" "<" "!="

# 6. What is the difference between the equal to operator and the assign-
# ment operator?

assign = 'giving a Value'

'Comparing' == 'comparing'

# 7. Explain what a condition is and where you would use one.
# age rescrition for voiting

enterAge = input('Enter you age :: ')

if enterAge != "":

    userAge = int(enterAge)

    if userAge   >= 21:

        print('You are eligibile to Voite')

    else:
        requiredAge = 21

        yearToWait = requiredAge - userAge 

        print('i have to wait for '+str(yearToWait)," Year")

else:
    print("Please Enter Your Age to Check you Eligibility")

# 8. Identify the three blocks in this code
    
spam = 0
if spam == 10:   # first
    print('eggs')
    if spam > 5: # second
        print('bacon')
    else:        # third
        print('ham')
    print('spam')
print('spam')

# 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is
# stored in spam, and prints Greetings! if anything else is stored in spam.

user = 1

if user == 1:
    print('Hello')
elif user == 2:
    print('Howdy')
else:
    print('Greetings!')

# 10. What can you press if your program is stuck in an infinite loop?
    
"Ctrl + c"

# 11. What is the difference between break and continue ?

# break # strops the code excution 

for i in range(5):
    if i == 3:
        break
    print(i)

# In this example, the loop will print values 0, 1, and 2,
# but when i becomes 3, the break statement will terminate the loop.


# continue # starts code excution from start

for i in range(5):
    if i == 2:
        continue
    print(i)

# In this example, the loop will print values 0, 1, 3, and 4. When i is 2, the continue 
# statement skips the print(i) statement for that iteration.
    
# 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1)
# in a for loop?
    
    range(10) # it start from 0 to 9.

    range(0,10) # it start from 0 to 9

    range(0, 10, 1) # it start from 0 to 9

# 13. Write a short program that prints the numbers 1 to 10 using a for loop.
# Then write an equivalent program that prints the numbers 1 to 10 using
# a while loop. 

for lop in range(1,11):
    print('lop',lop)

looper = 1
while looper <= 10:
    print('looper',looper)
    looper += 1

# 14. If you had a function named bacon() inside a module named spam, how
# would you call it after importing spam?

# import spam

# spam.bacon()
