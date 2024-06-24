print('=============ARITHMETIC OPERATORS===============')
# ARITHMETIC:  + - / * %
print(10-2)         # 8
print(10+2)         # 12
print(10*3)         # 30

print(10/3)         # in Java int / by int returns int, in Python returns float 3.333 unless cast division result to int
print(10/2)         # 5.0
print(int(10/2))    # 5   - cast into int to get return in int

print(10 % 3)         # returns remainder 1


print('=============SHORTHAND OPERATORS===============')
# SHORTHAND ASSIGNMENT OPERATORS: = += -= *= /= %=
a = 100
print(a)

a += 100
print(a)

a -= 50
print(a)

a /= 3
print(a)

a %= 3
print(a)

print('=============RELATIONAL OPERATORS===============')
# RELATIONAL OPERATORS:  >  >=  <  <=  ==  !=
a = 10
b = 55
print(bool(a >= b))     # False

b = 10
print(bool(a == b))     # True

a = 100
print(bool(a != b))     # True

print('=============LOGICAL OPERATORS===============')
# LOGICAL OPERATORS: and  or  not
# can use operators not only with boolean (like in Java)
s = 'Hello World'
# verify if both H and W  are in the string
print('H' and 'W' in s)         # True

# verify either H or W are in the string
print('W' or 'H' in s)          # W - returns whatever first is True in string

m = 'Java Python C# C++'
print('Ruby' or 'Java' in m)        # Ruby
print('Ruby' and 'Java' in m)       # True
print('Java' and 'Ruby' in m)       # False
print('Java' or 'Ruby' in m)        # Java

age = 26
citizen = 'USA'
is_eligible = age >= 18 and citizen == 'USA'
print(is_eligible)              # True

print('=============MEMBERSHIP OPERATORS===============')
# MEMBERSHIP OPERATORS: in   not in
has_java = 'Java' in m
print(has_java)

print('Java' not in m)          # False
print('Ruby' not in m)          # True

print('=============IDENTITY OPERATORS===============')
# IDENTITY OPERATORS: is, is not
# Java - verify if variables are referencing to the same object
# Python - compares the value or equality of two objects
s = 'Java'
s2 = 'Java'
print(s is s2)                  # True
print(s is not s2)              # False
