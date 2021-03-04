#sort: [5,2,0,3,0,1,6,0] -> [1,2,3,5,6,0,0,0]

arr = [5,2,0,3,0,1,6,0,20,4,34,23]
sorted_list = []

def sorting(a):
    sorted_list = sorted(a) #do with proper sorting not via function
    print('Original List: ', sorted_list)
    for x in sorted_list:
        if sorted_list[0] == 0:
            sorted_list += [sorted_list.pop(0)] #index to be removed and added to end
    return sorted_list

s = sorting(arr)
print("Partial Sorted: ", s)
