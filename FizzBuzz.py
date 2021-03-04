#FizzBuzz: Program that prints the numbers from 1 to 20.
#But for multiples of three print �Fizz� instead of the number and
#for the multiples of five print �Buzz�.
#For numbers which are multiples of both three and five print �FizzBuzz�.

def fizzbuzz():
    for n in range(1, 21):
        if n%3 == 0 and n%5 == 0:
            print ('FizzBuzz')
        elif n%3 == 0:
            print('Fizz')
        elif n%5 == 0:
            print('Buzz')
        else: print(n)

fizzbuzz()
