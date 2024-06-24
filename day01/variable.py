"""
give variable name > set data > data type will be set automatically,
 depending on what kind of data you store in this variable

 In Java:  DataType var = Data
 In Python: var = Data
"""

# null value, object was not created and does not exist
name = None
print(name)

name = "John"
age = 25
married = False
employed = True

print(name)
print(age)
print(married)
print(employed)


# to find out data type of variable use function 'type'
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(married))    # <class 'bool'>

gpa = 3.5
print(type(gpa))        # <class 'float'>


# CASTING
s = '25'        # string now
print(s*5)      # 2525252525
s = int(s)        # cast to int
print(s*5)      # 125
