# 11
"""
Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma
separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
sequence = input("Provide sequence: ")
numbers = [number for number in sequence.split(',')]
for number in numbers:
    intp = int(number, 2)
    if not intp % 5:
        print(number)

from typing import List


def fib():
    current, next = 0, 1
    while True:
        current, next = next, current + next
        yield current


result = fib()
for n in result:
    print(n, end=', ')
    if n > 10000:
        break

if __name__ == '__main__':
    print(fib)
