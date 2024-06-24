
if True:
    print('Python Programming')

print('Java Programming')

print('==========SINGLE IF=============')
score = 70
if score >= 60:
    print('Congrats! You passed the exam')      # this block with condition MUST be filled or can use keyword 'pass'

if score >= 60:
    pass                                        # can use keyword 'pass' to move on and be back to it later

s = 'Hello World'
if 'H' and 'W' in s:
    print(s, ' has', ' H and W')

print('===========IF ELSE==============')

if score >= 60:
    print('Pass')
else:
    print('Fail')

print('===========TERNARY==============')
# in ternary you have to assign one of the results/returns to the result variable (usually whatever is True)
age = 26
result = 'Eligible' if age >= 21 else 'Not Eligible'
print(result)

num = -200
result2 = 'Positive' if num >= 0 else 'Negative'
print(result2)

print('========MULTI BRANCH IF=========')
# for 3 and more alternatives
# only one condition block gets executed, all others are terminated
num = 100
result = None
if num > 0:
    result = 'Positive'
elif num < 0:
    result = 'Negative'
else:
    result = 'Zero'
print(result)

print('===========NESTED IF============')
# if condition depends on another condition (pre-condition)
score = -300
if 0 <= score <= 100:       # range of values
    if score >= 60:
        print('Pass')
    else:
        print('Fail')
else:
    print('Invalid score')

score2 = 81
if 0 <= score2 <= 100:
    if score2 >= 90:
        print('A')
    elif score2 >= 80:
        print('B')
    elif score2 >= 70:
        print('C')
    elif score2 >= 60:
        print('D')
    else:
        print('F')
else:
    print('Invalid score')
