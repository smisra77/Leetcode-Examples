#Given an array and a number, add it in such a way where array is [0,0,1]
#and number is 4 output will be [0,0,5]

#Example 2 : array is [1] and number is 9 output will be [1,0]

arry = [1]

def addvalue(a, n):
    for i in range(len(a) - 1, -1, -1):
        n += a[i]
        a[i] = n%10
        n /= 10

    if n > 0:
        a = [n] + a
    return a

print addvalue(arry, 9)
