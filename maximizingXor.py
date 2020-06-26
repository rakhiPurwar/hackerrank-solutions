def maximizingXor(l,r):
    m = 0
    i = l
    j = l+1
    while i<=r and j<=r:
        if i!=j and i^j > m:
            m = i^j
            i+=1
        elif i^j<m:
            j+=1   
        else:
            i+=1

    return m
