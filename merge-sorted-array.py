#Merge two sorted arrays list

a1 = [1, 3, 4, 5]
a2 = [2, 4, 6, 8]

def mergearray(x, y):
    l = []
    while x and y:
        if x[0] < y[0]:
            l.append(x.pop(0))
            #Remove the item at the given position in the list, and return it. 
        else:
            l.append(y.pop(0))
    return l + x + y

print(mergearray(a1, a2))
