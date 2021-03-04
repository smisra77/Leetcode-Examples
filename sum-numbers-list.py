#. Given a list and a number find two numbers in the list that sums up to the number given?

from itertools import combinations

numbers = [1, 3, 5, 6, 9]

for var in combinations(numbers, 10):
    if var[0] + var[1] == 10:
        print (var[0], var[1])


