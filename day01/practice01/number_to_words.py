"""
Write a program that can convert user entered number (from 0~9) to words.
NOTE: MUST use ternary
"""

number = int(input('Enter a number 0-9:\n'))

word_result = "Zero" if number == 0 else "One" if number == 1 else "Two" if number == 2 else "Three" if number == 3 \
else "Four" if number == 4 else "Five" if number == 5 else "Six" if number == 6 else "Seven" if number == 7 \
else "Eight" if number == 8 else "Nine" if number == 9 else "Invalid number"

print(word_result)
