"""
program that asks user to enter the grade level number, determine and print which school type the person is in
grade level and types are:
1-5: Elementary school
6-8: Middle school
9-12: High school
13-16: College
17-18: Grad School
Assume that the given number is 1 ~ 18
"""

grade_level_number = int(input('Enter grade level number: '))
grade_level_type = None
if 1 <= grade_level_number <= 5:
    print('Elementary school')
elif 6 <= grade_level_number <= 8:
    print('Middle school')
elif 9 <= grade_level_number <= 12:
    print('High school')
elif 13 <= grade_level_number <= 16:
    print('College')
elif 17 <= grade_level_number <= 18:
    print('Grad School')
else:
    print('Invalid grade level number')
