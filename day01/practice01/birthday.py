"""
create the following variable
name, birthDay, birthMonth, birthYear
use concatenation to display the birthday of the person
name = "John"
birth_day = 25
birth_month = "April"
birth_year = 1995;
output:
John was born on April/25/1995.
"""

name = input('Name:\n')
birthDay = input('Date:\n')
birthMonth = input('Month:\n')
birthYear = input('Year"\n')
print(f'{name} was born on {birthMonth}/{birthDay}/{birthYear}.')
