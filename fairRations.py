def fairRations(arr):
    c = 0
    n = len(arr)
    i = n-1
    if n == 2 and arr[0]%2 == 1:
        return "NO"
    while(i>=1):
        if arr[i]%2 == 1:
            arr[i]+=1
            arr[i-1]+=1
            c+=2
        i-=1
    if arr[0]% 2 == 1:
        return "NO"
    return c
