#If a=1, b=2, c=3,....z=26. Given a string, find all possible codes that string can generate.
#Give a count as well as print the strings.


def extend(current,i,string,result):
    l = len(string)
    if i == l:
        result.append(current)
        return
    numinstr = [int(string[i])]

    if i+1 < len(string):
        numinstr.append(int(string[i] + string[i+1]))
    # if use on digit, d is 1, else 2
    d = 1
    for n in numinstr:
        if 1 <= n and n <= 26:
            c = chr(ord('a') + n-1)
            extend(current + c, i+d, string, result)
        d += 1
 

def decode(string):
    result = []
    extend("",0,string,result)
    return result

print(decode('1123'))
