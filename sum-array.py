#Find pair in array equal to sum

ar = [0,-1,10,3,-8,40,2,9]
num = raw_input("Enter number :")


def find(a, n):
    a = list(sorted(a))
    psum = 0
    first = 0
    last = len(a) - 1
    while(first < last):
        psum = a[first] + a[last]
        if(psum > n):
            last -= 1
        elif(psum < n):
            first += 1
        else:
            print('A[first: ]', a[first, 'A[last]', a[last]])
            return a[first], a[last]
    raise ValueError('No pairs to add {}'.format(n))

x = find(ar, num)
print('Intergers::', x)
