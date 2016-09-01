'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
import math


def largest_prime(number):
    for i in range(2,round(math.sqrt(number))):
        while number % i == 0:
            number //= i
            if number==1 or number==i:
                return i


if __name__ == "__main__":
    soultion = largest_prime(600851475143)
    print(soultion)
