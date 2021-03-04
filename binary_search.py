#Binary Search Algorithm

arr = [23, 4, 23, 54, 112, 54, 89, 8]
target = input('Enter number to be searched: ')
target = int(target)

def binarysearch(a, t):
    low = 0
    high = len(a)
    while True:
        if low == high:
            return -1
        
        mid = (low + high) // 2

        if a[mid] < t:
            low = mid + 1
        elif a[mid] > t:
            high = mid
        elif a[mid] == t:
            return mid
    
    
arr = sorted(arr)
print('Sorted Array: ', arr)
result = binarysearch(arr, target)
print('Position: ', result)
