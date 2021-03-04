#You are given a string that is in roman numeral format. 
#Output the integer representation. 
#E.G. You're given XIV 
#Output 14.

roman = raw_input("Enter roman numeral :")

def romantoinetger(n):
    mapping = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    decimal = 0
    n = n[::-1]  #CM (MC = 1000-100 = 900) 
    last = None
    for x in n:
        if last and mapping[x] < last:
            decimal -= 2*mapping[x]
        decimal += mapping[x]
        last = mapping[x]
    return decimal

print(romantoinetger(roman))
