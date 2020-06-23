def kaprekarNumbers(p,q):
    found = False
    if(p<9):
        p = 9
        print(1,end = " ")
    for i in range(p,q+1):
        n = i*i
        s = str(n)
        d = len(s)//2
        r = s[d:]
        l = s[0:d]
        if((int(r)+int(l)== i)):
           found = True
           print(i,end = " ")
          
    if (not found):
       print("INVALID RANGE")
