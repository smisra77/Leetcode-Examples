#find palindrome number
#53235

n = input("Enter a number: ")

def findpalin(num):
    return int(str(num)[::-1])
# using slice notation to reverse the string and turning it back to an integer 

x = findpalin(n)
if x == n:
    print("Palin")
else:
    print("Not Palin")
