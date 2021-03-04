#If you are given 2 infinitely large integers in the form of strings,
#given the length of the string, find the product of the two integers.

#x = length of 1st num
#y = length of 2nd num
#a = 1st num
#b = 2nd num

num1 = '654154154151454545415415454'
num2 = '63516561563156316545145146514654'

def multiply_large(a,b):
    lenofa = len(a)
    lenofb = len(b)
    result = 0

    for x in xrange(lenofa-1, -1, -1): #(last-element, last-element, difference)["start", "stop" and "step"]
        for y in xrange(lenofb-1,-1,-1):
            result += (int(a[x])*int(b[y]))* 10 ** (lenofb - (y+1) + lenofa - (x+1))
    return result

print(multiply_large(num1,num2))

#While adding, we put i-th multiplication shifted.
