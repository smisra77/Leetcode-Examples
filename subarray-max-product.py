#Maximum subarray product

A = [6, -3, -10, 0, 2]

def maxProduct(arr):
    n = len(arr)
    max_end = 1 # max positive product ending at the current position
    min_end = 1 # min positive product ending at the current position
    maximum = 1 # Initialize maximum so far

    # Traverse throughout the array. Following values
    # are maintained after the ith iteration:
    # max_end is always 1 or some positive product
    # ending with arr[i]
    # min_end is always 1 or some negative product
    # ending with arr[i]
    for i in range(0,n):
        # If this element is positive, update max_end.
        # Update min_end only if min_end is
        # negative
        if arr[i] > 0:
            max_end = max_end*arr[i]
            min_end = min(min_end*arr[i], 1)

        # If this element is 0, then the maximum product cannot
        # end here, make both max_end and min_end 0
        # Assumption: Output is alway greater than or equal to 1.
            
        elif arr[i] == 0:
            min_end = 1
            max_end = 1

        # If element is negative. This is tricky
        # max_end can either be 1 or positive.
        # min_end can either be 1 or negative.
        # next min_end will always be prev.
        # max_end * arr[i]
        # next max_end will be 1 if prev
        # min_end is 1, otherwise
        # next max_end will be prev min_ending_here * arr[i]
        
        else:
            temp = max_end
            max_end = max(min_end*arr[i], 1)
            min_end = temp*arr[i]
        if(maximum < max_end):
            maximum = max_end
    return maximum

print(maxProduct(A))
