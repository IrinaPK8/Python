import numbers

class Employee:
    is_human = True     # STATIC variable, can be called outside class by CLASSNAME.VARIABLENAME
                        # to make variable static - it should be created without 'self' keyword

    planet = 'Earth'

# initialize method
# each class has CONSTRUCTOR
    def __init__(self, name: str = 'Unknown', job_title: str = 'Janitor', salary: numbers = 0):     # set type (:) and default values (=) for arguments
        self.name = name                # every single variable must initialized/defined/contain data
        self.job_title = job_title      # whatever is created using 'SELF' - INSTANCE variable
        self.salary = salary

# METHOD
# inside method in order to use instant variable - use 'self' keyword
    def work(self):                     # every method has 'self' keyword to be able to access instant variables
        print(f'{self.name} is working')

# to String method - returns String
    def __str__(self):
        # return f'name: {self.name}, job title: {self.job_title}'  # name: Unknown, job title: Janitor
# {self.__dict__}  returns in json format (key-value)
        return f'Employee {self.__dict__}'                          # Employee {'name': 'Daniel', 'job_title': 'Janitor', 'salary': 0}
# {type(self).__name__}  returns name of the class
        # return f'{type(self).__name__}{self.__dict__}'            # Employee {'name': 'Unknown', 'job_title': 'Janitor', 'salary': 0}

employee1 = Employee()
print(employee1.name)               # Unknown   --> as set in default
print(employee1.job_title)          # Janitor   --> as set in default
print(employee1.salary)             # 0         --> as set in default

employee2 = Employee('Daniel')      # setting default values for Employee object
print(employee2.name)               # Daniel   --> we set name when created employee2 variable
print(employee2.job_title)          # Janitor   --> as set in default
print(employee2.salary)             # 0         --> as set in default

employee3 = Employee('John', 'CEO')     # in Python arguments are option. If some are missing - default value will be used
print(employee3.name)               # John      --> we set name when created employee3 variable
print(employee3.job_title)          # CEO       --> we set job_title when created employee3 variable
print(employee3.salary)             # 0         --> as set in default

employee4 = Employee('Brianna', 'SDET', 150000)     # setting default values for Employee object
print(employee4.name)               # Brianna   --> we set name when created employee3 variable
print(employee4.job_title)          # SDET      --> we set job_title when created employee3 variable
print(employee4.salary)             # 150000    --> we set salary when created employee3 variable

print(Employee.is_human)            # True   --> as set by default in class Employee
print(Employee.planet)              # Earth   --> as set by default in class Employee

# can access method only through the object objectName.methodName
employee1.work()                # Unknown is working
employee2.work()                # Daniel is working
employee3.work()                # John is working
employee4.work()                # Brianna is working

print(employee1)                # name: Unknown, job title: Janitor
print(employee2)                # name: Daniel, job title: Janitor
print(employee3)                # name: John, job title: CEO
print(employee4)                # name: Brianna, job title: SDET