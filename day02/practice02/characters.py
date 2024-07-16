"""
write a program that can retrieve the digits, letters and special characters from a string
Ex:
input:
mn@#123Ab!
output:
letters: mnAb
digits: 123
special chars: @#!
"""

### ???????????????????????????????????
def characters(input_string=''):
    letters = ''
    digits = ''
    special_chars = ''

    for each in input_string:
        if each.isalpha():
            letters += each
        elif each.isdigit():
            digits += each
        else:
            special_chars += each

    return letters, digits, special_chars

letters, digits, special_chars = characters('mn@#123Ab!')

print(f'letters: {letters}')
print(f'digits: {digits}')
print(f'special_chars: {special_chars}')

