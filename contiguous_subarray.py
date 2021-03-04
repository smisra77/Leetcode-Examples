#Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#For example, given the array [-2,1,-3,4,-1,2,1,-5,4] ,
#the contiguous subarray [4,-1,2,1] has the largest sum = 6 .
import sys
arr = [-2,1,-3,4,-1,2,1,-5,4]
loa = len(arr)

def findmaxubarray(arr):
    if arr == []:
        return 0
    if loa == 1:
        return arr[0]
    if loa == 2:
        return max(arr[0], arr[1], arr[0] + arr[1])
    else:
        allneg = True
        for x in arr:
            if x >= 0:
                allneg = False
        if allneg == False:
            currsum = 0
            maxsum = - sys.maxsize - 1
            for i in range(loa):
                currsum = currsum + arr[i]
                if currsum < 0:
                    currsum = 0
                if currsum > maxsum:
                    maxsum = currsum
            return maxsum
        else:
            return max(arr)

print(findmaxubarray(arr))