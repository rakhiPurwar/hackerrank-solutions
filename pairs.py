def pairs(k, arr):
    c = 0
    i = 0
    j = 1
    arr.sort()
    while i<len(arr) and j<len(arr):
        if i!=j and arr[j]-arr[i] == k:
            c+=1
            print(arr[j],arr[i])
            i+=1
        elif arr[j]-arr[i]<k:
            j+=1   
        else:
            i+=1

    return c
