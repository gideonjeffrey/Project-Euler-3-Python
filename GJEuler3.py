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


def next_prime_factor(number, known_factor):
    if is_prime(number):
        return number
    number = number / known_factor
    for i in range(known_factor, int(ceil(sqrt(number))) + 1):
        if number % i == 0 and is_prime(i):
            return i
    return known_factor
    

def highest_prime_factor(number):
    while number > 1:
        x = next_prime_factor(number, 1)
        number = number / x
    return x

print(highest_prime_factor(600851475143))
