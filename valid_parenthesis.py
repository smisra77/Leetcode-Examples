#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

s = "{[]{()}}"
open_paren = ["(", "{", "["]

def valid_parenthesis(s):
    l = len(s)
    counter = 0
    for i in range(l):
        if s[i] in open_paren:
            counter += 1
            print('counter-1: ', counter)
        else:
            counter -= 1
            print('counter-2: ', counter)
    print('counter-final: ', counter)
    if counter == 0:
        return "Balanced"
    else:
        return "Unbalanced"

print(valid_parenthesis(s))