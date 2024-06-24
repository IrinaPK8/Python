"""
1.1 Create a function that can check if a person is eligible to vote
Ex: eligibleToVote(19, "USA");
output: You are not eligible to vote!
1.2 Create a function that can calculate the grade of the student based on the score
1.3 Create a function that can check if the given integer is positive, negative or zero
1.4 Create a function that can check if a string is palindrome, the function
 should return true if the given string is palindrome.
"""

"""1.1 Create a function that can check if a person is eligible to vote
Ex: eligibleToVote(19, "USA");
output: You are not eligible to vote!
"""
def eligible_to_vote (age: int = 0, country = ''):
    if age >= 19 and country == 'USA':
        return 'You are eligible to vote!'
    elif age >= 19 and country != 'USA':
        return 'You are not eligible to vote!'
    elif age <= 19 and country == 'USA':
        return 'You are not eligible to vote!'
    else:
        return 'You are not eligible to vote!'

print (eligible_to_vote(20, 'USA'))
print (eligible_to_vote(5, 'USA'))
print (eligible_to_vote(20, 'UK'))
print (eligible_to_vote(10, 'Canada'))

"""
1.2 Create a function that can calculate the grade of the student based on the score
"""
# A 90-100 B 80-90 C 70-80 D 60-70 E fail
def grade (score: int):
    if score <= 100 and score >= 90:
        return 'A'
    elif score < 90 and score >= 80:
        return 'B'
    elif score < 80 and score >= 70:
        return 'C'
    elif score < 70 and score >= 60:
        return 'D'
    else:
        return 'Fail'

print(grade(99))
print(grade(0))
print(grade(65))
print(grade(80))
print(grade(70))


"""1.3 Create a function that can check if the given integer is positive, negative or zero"""
def number (num: int):
    if num < 0:
        return 'negative'
    elif num > 0:
        return 'positive'
    else:
        return 'zero'

print(number(0))
print(number(-1258))
print(number(456))

"""1.4 Create a function that can check if a string is palindrome, the function
 should return true if the given string is palindrome."""

def palindrome_string (word = ''):
    reverse = word[:: -1]
    if word.lower() == reverse.lower():
        return True
    else:
        return False

print(palindrome_string('Anna'))
##

