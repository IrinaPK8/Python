"""
write a program that asks user to enter their age and define the age groups of the user
age groups are:
Teenager (< 21)
Adult   (>=21 && <55 )
Senior  ( > 55 )
if age is negative or greater than 150, print invalid

NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT
"""

age = int(input('Enter age: '))
group = None
if 0 < age < 150:
    if age < 21:
        group = 'Teenager'
    elif 21 <= age <= 55:
        group = 'Adult'
    elif age > 55:
        group = 'Senior'
else:
    group = "Invalid"
print(group)
