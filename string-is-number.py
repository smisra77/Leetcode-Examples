#Create a function that validates whether you a given string is a number

# -*- coding: utf-8 -*-
#num = input("Enter a string: ")

def check_number(n):
    try:
#        n.encode('utf-8')
        float(n)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(n)
        return True
    except (TypeError, ValueError):
        pass
    return False    

print(check_number('@'))
