#Find Longest Increasing Subsequence
#The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order.
# #For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.

arr = [50, 3, 10, 7, 40, 80]
len_of_arr = len(arr)
longest = None
data = list()
count = 0

for x in range(0, len_of_arr-1):
    print('x', arr[x])
    for y in range(x+1, len_of_arr):
        print('y', arr[y])
        if(arr[x] < arr[y]):
            data.append(arr[x])
            l = len(data)
            if longest is None or longest < l:
                longest = l

print('size', count)
print('LIS: ', l)
print(data)
