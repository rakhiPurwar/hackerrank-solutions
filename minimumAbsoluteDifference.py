def minimumAbsoluteDifference(arr):
    p = []
    arr.sort()
    for i in range(0,len(arr)-1):
        p.append(abs(arr[i] - arr[i+1]))

    return min(p)
