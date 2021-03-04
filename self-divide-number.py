# A self-dividing number is a number that is divisible by every digit it contains.
#
# For example, 128 is a self-dividing number because 128 % 1 == 0,
# 128 % 2 == 0, and 128 % 8 == 0.
#
# Also, a self-dividing number is not allowed to contain the digit zero.
#
# Given a lower and upper number bound, output a list of every possible self dividing number,
# including the bounds if possible.
#
# Example 1:
# Input: 
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
#
# Note:
# - The boundaries of each input argument are 1 <= left <= right <= 10000.


def selfdivide(n):
    num = n
    while num > 0:
#        print('1')
        if(num%10) == 0 or (n%(num%10)) != 0:
            return False
        num /= 10
        return True

result = []
left = 1
right = 22
for n in xrange(left, right+1):
#    print('2')
    if selfdivide(n):
        result.append(n)
print result
