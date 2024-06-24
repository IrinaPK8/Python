"""
Given a number of people on the ship, determine how many need to be crew members and how many can be passengers.
Print how many of each type there should be.
Total: 50  ====> 20 crew, 30 passengers
Total: 75  ====> 25 crew, 50 passengers
Total: 100 ====> 30 crew, 70 passengers
Any other number of people on the ship is not valid
NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT  ??????????
"""

num_of_people_on_ship = int(input('Number of people on ship: '))

if num_of_people_on_ship == 50:
    print('20 crew, 30 passengers')
elif num_of_people_on_ship == 75:
    print('25 crew, 50 passengers')
elif num_of_people_on_ship == 100:
    print('30 crew, 70 passengers')
else:
    print('Not a valid number')
