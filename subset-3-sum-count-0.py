#Given a list of integers, output all subsets of size three, which sum to zero.


def subsetofthree(ar, loa, t):
    subset = []
    if loa < 3:
        print('Incorrect input!!!')
        exit
    else:
        for i in range(0, loa-2):
            for j in range(i+1, loa-1):
                for k in range(j+1, loa):
                    if(ar[i]+ar[j]+ar[k] == t):
                        newtup = (ar[i],ar[j],ar[k])
                        subset.append(newtup)
    return subset
            

#a = [-1, 0]
a = [-1, 0, 1, 2, -1, -4]
lenofa = len(a)
total = 0

output = subsetofthree(a, lenofa, total)
print('Subset with desired sum: ', output)
