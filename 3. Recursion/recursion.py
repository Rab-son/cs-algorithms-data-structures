# Using recursion to implement power and factorial functions


def power(num, pwr):
    # breaking condition: if we reach zero, return 1
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)


def factorial(num):
    if (num == 0):
        return 1
    else:
        return num * factorial(num-1)