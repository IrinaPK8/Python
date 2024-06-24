# whatever is in the 'utility' module can be accessed here
# when importing other module - everything from that module will be printed when Run
# import utility > result = utility.sum / utility.concat / utility.calculate
# to import module from different package > import day01.utility

# 'from' keyword allows us to import only parts of python files properties
from utility import sum, calculate

result = sum(10, 20)
print(result)                           # 30

result = calculate(10, 20, '+')
print(result)                           # 30

# import statement can be placed anywhere in the module
import utility

utility.concat('Java', 'Python')
utility.sum(10, 20)
utility.calculate(10, 30, '*')

print('---------------------------------------')
# 'as' keyword to define alias name
import utility as u

u.concat('Java', 'Python')
u.sum(3, 1, 2)
u.calculate(30, 30, '/')

print('---------------------------------------')
# 'as' keyword - can use alias name for functions too
from utility import sum as s, calculate as c
print(s(10, 20))
print(c(20, 20, '/'))

