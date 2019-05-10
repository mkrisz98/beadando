from itertools import count


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False;

    return True


def get_primes(n):
    primes = []
    for number in count():
        if is_prime(number):
            primes.append(number)
        if len(primes) == n:
            return primes


print(get_primes(10000))