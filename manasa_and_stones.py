def stones(n, a, b):
    lis = []
    ls =[]
    for i in range(0,n):
        ls.append((n - i -1)*a+(i*b))
    s=list(set(ls))
    s.sort()
    return s
