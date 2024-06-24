# FOR LOOP
# 1. need to have a sequence (String is also a sequence)
s = 'Python'

# 2. apply For Loop to sequence
# during each loop operation 'each' represents each element in the sequence
for each in s:
    print(each)                 # prints chars P y t h o n


print('-------------------------------------')
# print range of numbers (specified in (from, to (excluded)))
for i in range(5, 10):
    print(i)

print('-------------------------------------')
# get index numbers from sequence - range()
# len() - function to include on last char -1
for i in range(0, len(s)):
    print(i)                    # get each index number
    print(s[i])                 # get each char under certain index number

print('-------------------------------------')
# get reverse index numbers from sequence
for i in range(-len(s), 0):
    print(i)
    print(s[i])

# reversed() - function to print reversed String
for i in reversed(range(0, len(s))):
    print(i)
    print(s[i])

# use slicing to reverse String from last to first - FASTEST WAY TO REVERSE STRING
result = ''                         # defining variable to store result in
for x in s[:: -1]:
    result += x
print(result)

print('-----------WHILE LOOP---------------')
# WHILE LOOP

num = int(input('Enter positive number:\n'))
while num <= 0:
    num = int(input('Enter positive number:\n'))

print(f'You have entered {num}')

print('-------------------------------------')
answer = input('Enter yes or no:\n')
while not (answer.lower() == 'yes' or answer.lower() == 'no'):
    answer = input('Enter yes or no:\n')

print(f'You have entered {answer}')

