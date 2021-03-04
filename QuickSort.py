#Quicksort Algorithm
#sys.setrecursionlimit(1500)

numbers = [52, 43, 123, 4, 47, 32, 100, 47, 65, 23, 44]

def QuickSort(arr):
    less = []
    equal = []
    high = []

    lenarr = len(arr)

    if lenarr > 1:
        pivot = arr[0]
#        pivot = (lenarr//2) # failing
#        print('Pivot: ', pivot)
                
        for x in arr:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                high.append(x)

        low = QuickSort(less)
        more = QuickSort(high)
        return low+equal+more
    else:
        return arr

output = QuickSort(numbers)
print('Sorted List: ', output)
