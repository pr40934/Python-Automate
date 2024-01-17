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