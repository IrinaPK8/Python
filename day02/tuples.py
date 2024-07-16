
days = ('Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun', 1, 2, 3, 4, 5, True, False)

print (type(days))      # get type of variable - <class 'tuple'>
print (len(days))       # get amount of elements in tuple - 16

# cannot update existing tuple
# days[0] = 'Java'    # replace index [0] to Java
# print(days)         # TypeError: 'tuple' object does not support item assignment

# access elements in tuple - use indexes
print(days[0])          # Mon
print(days[-1])         # False

# SLICING
days1 = ('Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun')
work_days = days1[1:5]          # OR days1[1:-3]
print(work_days)                # ('Tues', 'Wed', 'Thur', 'Fri')

week_days = days1[:5]           # OR days1[:-2]
print(week_days)                # ('Mon', 'Tues', 'Wed', 'Thur', 'Fri')

weekend = days1[-3:]
print(weekend)                  # ('Fri', 'Sat', 'Sun')

# COMPARE tuples CONTENT - use ==
# see if tuple REFERENCING TO SAME OBJECT - use 'is' - use id() - id is the object's memory address
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
print(tuple1 == tuple2)             # True
print(tuple1 is tuple2)             # True - if tuples have same exact elements, only one can be allocated in memory
print(id(tuple1) is id(tuple2))     # False

# MERGE / MULTIPLY tuples using + operator (accepts duplicates)
tuple3 = tuple1 + tuple2
print(tuple3)                       # (1, 2, 3, 1, 2, 3)

tuple4 = tuple1 * 5
print(tuple4)                       # (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)

# REVERSE tuple - use slicing
tuple_reversed = days1[::-1]
print(tuple_reversed)               # ('Sun', 'Sat', 'Fri', 'Thur', 'Wed', 'Tues', 'Mon')

# reverse() function and convert to tuple - use tuple() constructor
tuple_reversed2 = tuple(reversed(days))
print(tuple_reversed2)              # (False, True, 5, 4, 3, 2, 1, 'Sun', 'Sat', 'Fri', 'Thur', 'Wed', 'Tues', 'Mon')

# tuple METHODS
# index(): returns forward index number of a specified element from tuple
print(days1.index('Wed'))            # 2

# count(): returns frequency of a specified element from tuple
nums = 10, 20, 30, 40, 50, 60, 70, 10, 50, 10, 70, 60, 10, 10, 20
print(nums.count(10))               # 5

# ITERATE through tuple elements
for x in days1:
    print (x)                       # Mon Tue Wed Thu Fri Sat Sun

# ACCESS INDEX NUMBERS in tuple - use range()
for i in range (0, len(days1)):
    print(i)                        # 1 2 3 4 5 6

# ACCESS INDEX NUMBERS in reverse order in tuple - use revered () and range()
for i in reversed (range (0, len(days1))):
    print(i)                        # 6 5 4 3 2 1
