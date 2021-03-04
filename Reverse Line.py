#Program to reverse the words in file

filen = input("Enter filename: ")
fh = open(filen)

for line in fh:
    line = line.rstrip()
    words = line.split()
    # reverse list of words
    # suppose we have list of elements list = [1,2,3,4],
    # list[0]=1, list[1]=2 and index -1 represents
    # the last element list[-1]=4 ( equivalent to list[3]=4 )
    # So, inputWords[-1::-1] here we have three arguments
    # first is -1 that means start from last element
    # second argument is empty that means move to end of list
    # third arguments is difference of steps
    words = words[-1::-1]
    output = " ".join(words)

print('Reveresed line: ', output)

finaloutput = "".join(reversed(output))

print("Final output: ", finaloutput)