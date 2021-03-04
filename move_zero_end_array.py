#Given an array of integers. Modify the array by moving all the zeros to the end (right side).
#The order of the other elements doesn't matter.

#O(n^2)

#[3, 2, 3, 1, 12, -1, 23, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0]

arry = [0,3,2,0,0,3,0,1,0,12,0,-1,0,23,5,0,6]

def move_zero(a):
    # Traverse the array. If element
    # encountered is non-zero, then
    # replace the element at index
    # 'count' with this element

    l = len(a)
    print(l)
    count = 0
    for i in range(l):
        if a[i] != 0:
            a[count] = a[i]
            count += 1

    # Now all non-zero elements have been
    # shifted to front and 'count' is set
    # as index of first 0. Make all
    # elements 0 from count to end. 

    while count < l:
        a[count] = 0
        count += 1

    return a

x = move_zero(arry)
print('Final: ', x)
