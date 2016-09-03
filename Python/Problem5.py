'''
2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
'''

found = False
smallest_number = 20

while not found:
    current_number = smallest_number
    for i in range(1,21):
        if smallest_number % i != 0:
            found = False
            smallest_number += 1
        elif smallest_number == current_number and i == 20:
            found = True

print(smallest_number)
