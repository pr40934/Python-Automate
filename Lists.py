# LISTS

# The List Data Type

x = ['car','bus','bike',1,5,None,True,False]

name = ['pratap','raju']

print('slicing',name[0:])

# list Length

print(len(x))

# Concatenation

print(x + name)

print(x)

# Delete Iteam in a List

# we can delete index to index [1:-1]

del x[1:-2] # del work's with postion of data , with index numbers

x.remove(1) # we have to pass actucal data and only one argument

print('Removed and Deleted x :: ',x)

# In Operator in List

print('Check :: ','car' not in x ,x.index('car')) 

print('cal',0-1)

import random
messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']
guss_number = random.randint(0, len(messages) - 1) # len gives total count but -1 makes from 0
print(guss_number ,'::',messages[guss_number])

# 29 - 01 - 2024

user_name = 'pratap'

print(user_name[0])

# 30 - 01 - 2024


user_name = 'pratap'
# user_name[0] = 'Z'  it doesn't work because string is a immutable we can't change data in that user_name varibale

print('user_name ::',user_name)

# Tuples

# tuples are immutables we can't change values in a tuple

new_user_name = ("pratap","age 22")
# new_user_name[0] = 'Pratap Raju'
print('new_user_name ::',new_user_name)

first = [1,2,3,4,5]

third = first

print(id(first),id(third))

first[0] = 'nochange'

print('first',first)

print('third',third)

import copy

# copy list  with out changing an data from both lists

first_list = [1,2,3,4,5]

second_list = copy.copy(first_list)

second_list[0] = 'hello'

print('first_List :: ',first_list)

print('second_list :: ',second_list)