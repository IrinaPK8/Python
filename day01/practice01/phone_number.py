"""declare the following variables:
countryCode, areaCode, localNumber
use string concatenation to display the phone number
ex:
country_code = 1
area_code = 703
localNumber = 4512625
output:
Your phone number is +1(703)-4512625
"""

countryCode = input('Enter country code:\n')
areaCode = input('Enter area code code:\n')
localNumber = input('Enter local number code:\n')
print(f'Your phone number is +{countryCode}({areaCode})-{localNumber}')

