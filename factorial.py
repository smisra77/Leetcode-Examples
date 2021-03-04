#Write a iterative Python function to print the factorial of a number n (ie, returns n!).

num = input("Enter a number: ")

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(num))
