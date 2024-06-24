"""
program that asks user to enter an integer and prints "Fizz" if the number is divisible by 3,
prints "Buzz" if the number is divisible by 5,
and prints FizzBuzz if the number is divisible by both 3 and 5.
Ex:
number 15
Output:
FizzBuzz
"""

number = int(input('Enter number: '))
if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print('Not divisible by 3 or 5')

