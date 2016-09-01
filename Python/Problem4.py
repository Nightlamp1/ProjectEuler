'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

palindromes = []

for i in range(100,1000):
    for t in range(100,1000):
        number = i * t
        if str(number) == str(number)[::-1]:
            palindromes.append(number)

palindromes = sorted(palindromes)
pal_largest = len(palindromes)-1
print(palindromes[pal_largest])
