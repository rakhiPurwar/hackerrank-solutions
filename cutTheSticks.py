def cutTheSticks(arr):
    ls = []
    while max(arr)!=0:
        print(max(arr))
        m = min(j for j in arr if j > 0)
        c = 0
        for i in range(0,len(arr)):
            if arr[i]!=0:
                arr[i] = arr[i]-m
                c+=1
        ls.append(c)
    return ls
