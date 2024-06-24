name = 'Python'

# get/returns total number of chars in String - len(stringName)
print(len(name))                    # 6

# access chars in the String - stringName [indexNumber]
print(name[0])                      # P
print(name[len(name)-6])            # P    # as option to easier way to access char
print(name[-1])                     # n
print(name[-2])                     # o
# print(name[10])                   # IndexError: string index out of range

# SLICING STRING
s = 'Java Programming language'

# use range on indexes to indicate where to start and where to end the slicing - [ start : end ]
# the ending index/last index char is NOT included in the string
s2 = s[5:-9]    # can also do [5:16]
print(s2)                           # Programming

# need to slice from the beginning - indicate the ending index only
# by default the slicing will start at index 0
s3 = s[:4]                          # Java
print(s3)

# need to slice the end only - can also provide last index as negative -1
s4 = s[:-1]                         # Java Programming languag
print(s4)

# slice and REVERSE string use :: and the last index as negative -1 to start with
s5 = s[::-1]                        # egaugnal gnimmargorP avaJ
print(s5)

# REVERSE WITHOUT SLICING - USE CONSTRUCTOR                   ??????????????????????????????????
# s6 = str(reversed(s))               # return is Object, not the String - cast into str to have return as String
# #    print('reversed ' + i)

# slice from any index to end including last char - provide index where to start slicing only
s7 = s[7:]                          # ogramming language
print(s7)

print('--------------------------------------------------')
# get all METHODS OF STRING CLASS
# print(help(str))

print('--------------------------------------------------')
# capitalize() - takes no argument, capitalizes first char of string only
s = 'python programming language'
s = s.capitalize()
print(s)                                    # Python programming language

# title() - takes no argument, capitalizes each first letter in each word in string
s = s.title()
print(s)                                    # Python Programming Language

# strip() - takes no argument, remove all white spaces before/after string
# lstrip() - remove white space on left
# rstrip() - remove white space on right
s = '            Python             '
s = s.strip()
print(s)                                    # Python

# index() - looks for and returns index of char starting from index 0
# rindex() - looks for and returns index of char starting from last char
s = 'JAVA ABA'
print(s.index('A'))                         # 1
print(s.rindex('A'))                        # 7

# replace() - takes old value, new value and argument 'count'
# 'count' is optional - if you do not specify how many words to be replaced - all will be replaced - 'Java Java' > 'Python Python
# if you specify how many words to be replaced - only this amount will be replaced - 'Java Java' > 'Python Java'
s = 'Java Java'
s = s.replace('Java', 'Python', 1)
print(s)                                    # Python Java

# if need to replace char in the middle of string - add some unique char (e.g., space after/before this word which exists in string)
s = 'C# C# Python'
s = s.replace(' C#', ' Java')   # if certain char need to be replace from a string - use additional char to specify (here space before C#)
print(s)                                    # C# Java Python

# count() - find frequency in string, accepts argument (what to count)
s = 'Java JaVa javA Python Python'
# to ignore case - assign to lower() and count all javas in lower case in String
count_java = s.lower().count('java')
count_python = s.count('Python')
print(count_java)                           # 3
print(count_python)                         # 2

# to compare contents of objects - use equal operator ==
# == does not ignore the case
# need to use lower() to ignore case to get True
s1 = 'java'
s2 = 'Java'
print(s1.lower() == s2.lower())             # True

# islower()     isupper() - check if char(s) in string a lower or upper case, checks all chars in string
# to check some certain char - use index [] of this char
s = 'Java'
print(s[0].isupper())                       # True
print(s[2].islower())                       # True

# isalpha()     isdigit() - verify if string is letter or numerical
s = 'a'
print(s.isalpha())                          # True
print(s.isdigit())                          # False

# istitle() - checks if each word in string starts with capital letter
s = 'Java Programming'
print(s.istitle())                          # True
