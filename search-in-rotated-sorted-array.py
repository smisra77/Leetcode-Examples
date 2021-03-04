#search-in-rotated-sorted-array

array = [21,24,45,0,2,5,7]

def search(a, n):
    first = 0
    last = len(a)-1

    while first+1 < last:
        mid = first + (last - first) // 2
        if a[mid] == n:
            return True
        if a[mid] > a[first]:
            if a[first] <= n and a[mid] > n:
                last  = mid
            else:
                first = mid
        elif a[mid] < a[first]:
            if a[mid] < n and a[last] >= n:
                first = mid
            else:
                last = mid
        else:
            first += 1

    if a[first] == n:
        return True
    if a[last] == n:
        return True
    return False


while True:
    n = int(input('Enter a numbe: '))
    result = search(array, n)
    print(result)
    x = input('Do you wish to continue?')
    if x == 'No':
        break
 
