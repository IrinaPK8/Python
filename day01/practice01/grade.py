"""
variable named grade is given. write a program to print the following messages:
'A': excellent
'B': great job
'C': good
'D': passed
'F': failed
otherwise: invalid
NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT
"""

grade = input('Enter grade: ')
message = None
if grade == 'A':
    message = 'excellent'
elif grade == 'B':
    message = 'great job'
elif grade == 'C':
    message = 'good'
elif grade == 'D':
    message = 'passed'
elif grade == 'F':
    message = 'failed'
else:
    message = 'Invalid'
print(message)
