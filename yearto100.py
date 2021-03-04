#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

from datetime import datetime

age = int(input("Enter your age: "))
name = input("Enter your name: ")
current_year = int(datetime.now().year)

def year(age, name):
    diff = 100 - age
    yearto100 = current_year + diff
    return yearto100

x = year(age, name)
print("%s, year you will turn to 100 is %d" % (name, x))
    
