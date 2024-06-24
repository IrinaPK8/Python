"""
Ask the user to enter the following info, and display the user entered info:
name (String)
age (integer)
gender (String)
company (String)
job title (String)
salary (float)

Ex:
Given Data:
name = "Daniel"
age = 28
gender = 'Male'
company_name = 'Google Inc'
job_title = "Scrum Master"
salary = 90000

Output:
Daniel is 28 years old, gender is Male
Daniel works at Google Inc as a Scrum Master
Daniel makes $ 90000 per year
"""

name = input('Name: ')
age = int(input('Age: '))
gender = input('Gender: ')
company = input('Company: ')
job_title = input('Job title: ')
salary = float(input('Salary: '))

print(f'{name} is {age} years old, gender is {gender}\n{name} works at {company} as a {job_title}\n{name} makes $ {salary} per year')
