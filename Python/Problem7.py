'''
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''


def primes(n):
    primes = [2]
    current_number = 3
    while len(primes) < n:
        if all(current_number % prime != 0 for prime in primes):
            primes.append(current_number)
        current_number += 2
    return primes[-1]

if __name__ == '__main__':
    print(primes(10001))
