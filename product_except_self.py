#Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#Input:  [1,2,3,4]
#Output: [24,12,8,6]

arr = [1,2,3,4]
len_of_arr = len(arr)

L = [0]*len_of_arr
R = [0]*len_of_arr
Result = [0]*len_of_arr

L[0] = 1
for i in range(1, len_of_arr):
    L[i] = arr[i-1] * L[i-1]

R[len_of_arr-1] = 1
for i in reversed(range(len_of_arr-1)):
    R[i] = R[i+1] * arr[i+1]

for i in range(len_of_arr):
    Result[i] = R[i] * L[i]

print('Result: ', Result)
