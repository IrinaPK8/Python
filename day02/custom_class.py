import numbers

class Employee:
    is_human = True     # STATIC variable, can be called outside class by callsName.variableName
                        # to make variable static - it should be created without 'self' keyword

    planet = 'Earth'

# initialize method
    def __init__(self, name: str = 'Unknown', job_title: str = 'Janitor', salary: numbers = 0):     # set type (:) and default values (=) for arguments
        self.name = name                # every single variable must initialized/defined/contain data
        self.job_title = job_title      # whatever is created using 'self' - INSTANCE variable
        self.salary = salary

# METHOD
    def work(self):                     # every method has 'self' keyword to be able to access instant variables
        print(f'{self.name} is working')

# to String method - returns String
    def __str__(self):
        return f'name: {self.name}, job title: {self.job_title}'

employee1 = Employee()
print(employee1.name)
print(employee1.job_title)
print(employee1.salary)

employee2 = Employee('Daniel')     # setting default values for Employee object
print(employee2.name)
print(employee2.job_title)
print(employee2.salary)

employee3 = Employee('John', 'CEO')     # in Python arguments are option. If some are missing - default value will be used
print(employee3.name)
print(employee3.job_title)
print(employee3.salary)

employee4 = Employee('Brianna', 'SDET', 150000)     # setting default values for Employee object
print(employee4.name)
print(employee4.job_title)
print(employee4.salary)

print(Employee.is_human)
print(Employee.planet)

# can access method only through the object objectName.methodName
employee1.work()
employee2.work()
employee3.work()
employee4.work()

print(employee1)
print(employee2)
print(employee3)
print(employee4)