def equalizeArray(arr):
    c = Counter(arr)
    print(c)  
    maximum = max(c, key=c.get)
    return len(arr)-c[maximum]
