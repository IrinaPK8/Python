
name = 'James'
age = 26

# both values on left and right from + should be String
print('My name is ' + name)
print(name + ' is ' + str(age))
print(str(name) + ' is ' + str(age))        # if not sure what type of var you have - can cast again str(name)


# concatenation of different data types using {} placeholder
print('My age is {}'.format(age))
print('My name is ' + name + ' and my age is {}'.format(age))
print('My name is {} and I am {} years old'.format(name, age))
print(f'My name is {name} and I am {age} years old')

# use comma to append another data type, will append to the end of the String only
print('Python', 3, 'is awesome:', True)
