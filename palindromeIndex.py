def palindromeIndex(s):
    p = len(s)
    for i in range(0,int(p/2)):
        if s[i]!=s[p-1-i]:
            k= s[i+1:p-i]
            q = s[i:p-1-i]
            l =len(k)
            temp=0
            for j in range(0,int(l/2)):
                 if k[j] != k[l-1-j]:
                    temp=1
            if(temp==0):return i
            for r in range(0,int(l/2)):
                 if q[r] != q[l-1-r]:
                    temp=0
            if(temp==1):return p-i-1
    return -1
