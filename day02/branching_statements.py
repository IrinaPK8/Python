print('-------------------------------------')
# BRANCHING STATEMENTS - break, continue, pass

print('---------------BREAK------------------')
for i in range (1, 6):
    print(i)
    if i == 3:
        break

print('--------------CONTINUE----------------')
for i in range(1, 6):
    if i == 3 or i == 4:
        continue
    print(i)                                    # ?????????????? why if statement is in different place than break VVVVV


print('----------------PASS------------------')
for i in range(1, 6):
    if i == 3 or i == 4:
        pass
    print(i)

# pass can be used in function, statement, class, method
def function():
    pass

if True:
    pass

class Class:

    def method(self):
        pass