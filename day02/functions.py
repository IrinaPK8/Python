"""
Java methods:
    public static void method (parameter) {
    ...... }

Python methods:
    - public access modifier is used by default (no need to type it) - if there are no underscores
                                                before function name > it's public access modifier
    - private - add two underscores before function name __functionName
    - protected - add one underscore before function name _functionName

    - in Python function you do not specify any return type - it can be used as void or return value
"""
import numbers

# VOID FUNCTION
def display_message():
    print('Hello Cydeo')                # Hello Cydeo
    print('Hello World')                # Hello World
display_message()       # calling function


# RETURN FUNCTION
# do not need to specify return type - can return anything - Sting, Integer...
# if it's return function, you are able to assign it to variable or call it in print() statement   !!!!!!!!!!
def value():
    return 'Python Programming'
print(value())                          # Python Programming


# CAN MAKE IT MANDATORY TO RETURN A VALUE - GENERIC FUNCTION - user arrow token -> returnType:
def return_int() -> int:
    return 8
print(return_int())                     # 8


# FUNCTION WITH PARAMETERS - in order to provide additional info to pass the test
def square(num: int):               # it's better to specify/restrict which type only to take as argument 'parameter: type'
    return num * num                # if other var type is used - getting warning since Python uses Interpreter instead of Compiler
print(square(10))                       # 100


def divide(num1, num2):
    return num1 / num2
print (divide(48, 6))       # 8.0


def compare(str1, str2):                # can take any arguments
    return str1 == str2
print(compare('java', 'java'))      # True


def concatenate(num):
    return num + num
print(concatenate('Java'))              # JavaJava


# if not sure what type of number variable to accept > import numbers (at very top of function)
# it will return type of given arguments
def add(num1: numbers, num2: numbers):
    return num1 + num2
print (add(5.5, 6.0))       #11.5
print(add(12, 8))           #20


print('-------------CALCULATOR----------------')
def calculate(num1: numbers, num2: numbers, operator: str) -> numbers:
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Invalid operator')
        return 0
print(calculate(10, 5, '+'))
print(calculate(10, 5, '-'))
print(calculate(10, 5, '*'))
print(calculate(10, 5, '/'))


print('-------------------------------------------')
# DEFAULT ARGUMENT FUNCTION CAN BE TREATED AS METHOD OVERLOADING IN JAVA
# if not all params are must > assign default values = 0 to non-mandatory params
# whatever param gets default value first - all following params should also get default values
def sum(n1: numbers, n2: numbers, n3: numbers = 0, n4: numbers = 0) -> numbers:
    return n1 +n2 +n3 +n4

# default value will be assigned if only user does not provide value
print(sum(10, 20))                      #30
print(sum(10, 20, 30))              #60
print(sum(10, 20, 30, 40))      #100

print('---------CONCAT STR WITH OTHER DATA-----------')
# create concatenate function - str with any other datas (up to five data)
# set other values to default - empty String in this case
def concat (a: str, b, c = '', d = '', e = ''):
    print(f'{a} {b} {c} {d} {e}'.strip())       # add .strip() method to remove spaces if necessary
concat('Cydeo', 'school')                           # Cydeo school
concat('Python', 3, 2.5)                         # Python 3 2.5
concat('Python', 3, '2.5', True, False)    # Python 3 2.5 True False

"""
STEPS:
1. declare
2. parameters
3. restrict params data type
4. set default value to parameters
5. restrict return type      : type   OR   -> type

*** Dynamic Typing - any data can be assigned to param variables ***
"""
