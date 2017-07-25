# Project-Euler-3-Python
# Finding largest prime factor of a number

from math import sqrt, ceil

def is_prime(x):
    if type(x) != int:
        return False
    if x < 2:
        return False
    if x == 2: 
        return True
    for n in range(2, int(ceil(sqrt(x))) + 1):
        if x % n == 0:
            return False
    return True


def first_prime_factor(number):
    for i in range(1, ceil(sqrt(number)) + 1):
        if number % i == 0 and is_prime(i):
            return i
    return number
    

def highest_prime_factor(number):
    while number > 1:
        x = first_prime_factor(number)
        number = number / x
    return x

print(highest_prime_factor(600851475143))
