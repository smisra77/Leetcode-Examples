#nth element in fibanocii series
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#https://jineshpaloor.wordpress.com/2011/07/09/optimized-program-to-find-the-n-th-fibonacci-number-using-python/

def fib(n):
    if n<2: return n
    elif not n in fib_dict:
        fib_dict[n] = fib(n-1) + fib(n-2)
    return fib_dict[n]

#fib_dict stores fibanocii values

fib_dict = {}
result = fib(6)
print result
