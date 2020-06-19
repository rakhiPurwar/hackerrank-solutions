def encryption(s):
    ls = []
    p = []
    ans = ""
    s  = s.replace(" ","")
    l = len(s)
    print(s)
    r = math.floor(math.sqrt(l))
    c = math.ceil(math.sqrt(l))
    print(r,c)
    if r*c<l:
       r=r+1
    s+=" "*(r*c-l)
    ls = list(s)
    print(ls)
    for i in range(0,c):
       j = i
       temp = ""
       while j<r*c:
         temp+=ls[j]
         j+=c
       p.append(temp)
    for e in p:
        e = e.rstrip(" ")
        ans+=e
        ans+=" "
    return ans
   
