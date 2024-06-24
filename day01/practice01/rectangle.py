"""program that can calculate the area & perimeter of any given Rectangle
Hint: width and length need to be given to calculate the area and perimeter of rectangle
Ex:
Given Data:
length = 5
width = 2

output:
Area of the rectangle is equal to 10
Perimeter of rectangle is equal to 20
"""

length = int(input('Length is\n'))
width = int(input('Width is\n'))

print('Area of the rectangle is equal to {}'.format(length * width))
print('Perimeter of rectangle is equal to {}'.format((length + width) * 2))
