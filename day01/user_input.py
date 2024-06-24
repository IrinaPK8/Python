print('==========USER INPUT============')
# print(help(input))

# can assign method to variable or use without assignment
name = input('Enter your name:\n')       # can type prompt
age = int(input('Enter your age:\n'))    # can cast into in right here OR like this when printing - print(int(age) + 10)
gpa = float(input('Enter your GPA:\n'))
boolean_value = bool(input('Enter T or F:\n'))

print(name)
print(age + 10)                         # can treat return as integer (- or + smth) because casting was done when declaring variable
print(gpa)
print(boolean_value)

print(type(name))                       # check what data type the input is
print(type(age))
print(type(gpa))
print(type(boolean_value))


