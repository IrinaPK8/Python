"""program that can convert gallon (int) to litter (double)
Hints: 1 gallon = 3.79 litters
Ex:
Given Data:
gallon = 10
output:
10 gallon is equal to 37.9 liters
"""

gallons = int(input('Enter gallons:\n'))
liters = gallons * 3.79
print(f'{gallons} gallon is equal to {liters} liters')
