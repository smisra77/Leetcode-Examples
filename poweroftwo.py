#Power of two

n = input("Enter a number: ")

def powerof(num):
    return num>0 and (num & (num-1))
#If num & num-1 == 0: powerof2. Eg: 16&15 = 0, 10&9 = 8
#& Binary AND: Operator copies a bit to the result if it exists in both operands

x = powerof(n)
if x==0:
    print('%d is power of two' %n)
else:
    print('%d is not power of 2' %n)
                    
