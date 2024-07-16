"""
Write a program for grade calculator:
8.1. Ask the user "Enter your score"
If user enters invalid score, terminate the program after displaying the error message "Invalid Entry"

8.2 Display the grade of the student.
90 ~ 100 ==> A
80 ~ 89 ==> B
70 ~ 79 ==> C
60 ~ 69 ==> D
0 ~ 59 ==> F

8.3 Ask the user would you like to continue
If "yes" --> repeat the previous steps
If "no" --> print "Thank you for using Cydeo Grade Calculator APP"

If user enters an invalid entry, ask the user to re-enter until user provides a valid entry
"""

def grade_calculator(score: int):
    if score >=0 and score <=  100:
        if score >= 90 and score <= 100:
            return('A')
        elif score >= 80 and score < 90:
            return('B')
        elif score >= 70 and score < 80:
            return('C')
        elif score >= 60 and score < 70:
            return('D')
        elif score < 59:
            return('F')
    else:
        return('Invalid Entry')

print(grade_calculator(89))

def cont (question: str):
    if question.islower() == 'Yes':
        return (grade_calculator())     #### ?????????????????????????
    elif question.islower() == 'No':
        return ('Thank you for using Cydeo Grade Calculator APP')
    else:
        return ('Invalid input')

print(cont('No'))
