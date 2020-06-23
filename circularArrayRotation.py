def circularArrayRotation(a, k, queries):
    
    p = []
    n = len(a)
    if k>n: 
        k = k%n 
    temp= []
    temp.append(a[n-k])
    for i in range(n-k+1,n):
        temp.append(a[i])
    for j in range(0,n-k):
        temp.append(a[j])
    for r in range(0,len(queries)):
        p.append(temp[queries[r]])
    print(p)
    return p
