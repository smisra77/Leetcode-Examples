#Given a String that contains words separated by single space, reverse the words
#in the String. You can assume that no leading or trailing spaces are there. 
#// For example: "Man bites dog" => "dog bites Man”

sent = "Man bites dog"

def revstr(s):
    lenofs = len(s)
    s = s.split()
    x = " ".join(reversed(s))
    print("Reversed String: %s" % x)
    
revstr(sent)
    
