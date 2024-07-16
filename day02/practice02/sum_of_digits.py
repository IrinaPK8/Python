"""
Write a program that can return the sum of digits from a  string
Ex:
input: A1B2C3
output: 6
"""

def sum_of_digits(phrase: str):
    total_sum =  0

    for i in phrase:
        if i.isalpha():
            continue
        else:
            total_sum += int(i)

    return total_sum

print(sum_of_digits('A1B2C3'))
