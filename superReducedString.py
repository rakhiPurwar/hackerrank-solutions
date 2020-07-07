def superReducedString(s):
    res = []
    for i in s:
        if res and res[-1] == i:
            res.pop()  
        else:
            res.append(i)     
    res = "".join(res)
    if len(res)>0:
        return res
    else:
        return "Empty String"
