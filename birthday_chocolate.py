def birthday(s, d, m):
    sm=0
    count=0
    for i in range(0,m):
        sm+=s[i]
    if sm == d :
        count+=1
    print(sm)
    for end in range(m,len(s)):
        sm=sm + s[end] - s[end-m]
        print(sm)
        if sm == d:
            count+=1
        else:
            count+=0
    return count
