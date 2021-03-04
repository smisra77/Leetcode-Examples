#search in sorted reverse array

#Find integer in rotated array

arr = [4,5,6,10,1,2]
num = input("Enter number to be searched: ")

def find(a, n):
    first = 0
    last = len(a) - 1
    found = False
#    a = sorted(a)
#    print('0', a)

    while first <= last and not found:
        mid = (first + last)//2
        print('1', mid)
       # print('2', n)
        if a[mid] == n:
            print('5', a[mid])
            found = True
        else:
            if mid < last and a[mid+1] < a[mid]:
                if a[first] <= a[mid]:
                    first = mid + 1
                print('2', first)
            else:
                last = mid - 1
                print('3', last)
    return found

print(find(arr,num))
