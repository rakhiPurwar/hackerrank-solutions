def beautifulTriplets(d, arr):
    c = 0
    n = len(arr)
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            if arr[j]- arr[i]==d:
                for k in range(j+1,n):
                    if arr[k]-arr[j] == d:
                        c+=1
                        break
    return c
