def beautifulBinaryString(b):
    c = 0
    for i in range(len(b)):
        p=b.find("010")
        if(p!=-1):
            b = b[p+3:]
            print(b)
            c+=1
    return c
