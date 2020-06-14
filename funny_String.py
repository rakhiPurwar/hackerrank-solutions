def funnyString(s):
    p=s[::-1]
    print(p)
    r = []
    q = []
    for i in range(0,len(p)-1):
        r.append(abs(ord(p[i+1])-ord(p[i])))
    for i in range(0,len(s)-1):
        q.append(abs(ord(s[i+1])-ord(s[i])))
    if q == r:
        return "Funny"
    return "Not Funny"   
