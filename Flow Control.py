# 14 - 01 - 2024

# Flow Control Conditions

# Comparison Operators

print("Pratap" == "Pratap") # same as Both

print("Pratap" != "Pratap") # Not equal TO

print(9 < 10) # less than

print(8 <= 8) # less than Equal to

print(8 >= 8 ) # Greater than Equal to

# Conditions 

if True:
    print('Make If True')
else:
    print('else')


if False:
    print('Falsed')

elif True:
    print('no else ')


while True:
    print('Hello While')
    
    if True:
        print('Loop Breaked')
        
        break
x = 2

import time
print("time :: ",time.ctime())
# time.sleep(5)
if x == 2:

    print('IFFF')

    print('time :: ',time.ctime())

elif x == 2: # this elif not going to print Or excuite

    print('EEEEELIF')


looper = 10

import sys

for lop in range(0,looper):

    looper += 20
    print('lop',looper)

    sys.exit()

    
