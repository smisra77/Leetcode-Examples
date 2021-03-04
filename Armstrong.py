#Armstrong number

number = raw_input("Enter a number: ")
temp = int(number)
Sum = 0

while(temp>0):
    rem = int(temp%10)
    temp=temp/10
    Sum += (rem*rem*rem)
if(int(Sum) == int(number)):
    print("Number is Armstrong")
else:
    print("Not Armstrong")

