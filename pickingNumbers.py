def pickingNumbers(arr):
    # Write your code here
    c = 0
    arr.sort()
    for i in range(0,len(arr)-1):
        if arr[i+1]-arr[i] <= 1:
            if arr[i] == arr[i+1]:
                p = a.count(arr[i])
            else:
                p = arr.count(arr[i])+arr.count(arr[i+1])
            if(p>c):
                c = p
        
    return c
