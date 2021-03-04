#Write a function that takes a string as input and returns the string reversed.
#Example: Given s = "hello", return "olleh".

data = input("Enter a string: ")
#revstring = []
lenofdata = len(data)

if lenofdata == 0:
    print("Empty string!!!")
    quit()

#data[::-1]
def reversedstring(d):
    output = "".join(reversed(d))
    return output

revstring = reversedstring(data)

if revstring == data:
    print("Palindrome")
    print('Reversed String:', revstring)
else:
    print("Not Palindrome")
    print('Reversed String:', revstring)