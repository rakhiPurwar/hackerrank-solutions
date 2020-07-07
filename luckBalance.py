def luckBalance(k, lst):
    p = []
    rest = [lst[i][0] for i in range(0, len(lst))]
    res = [lst[i][0] for i in range(0, len(lst)) if lst[i][1] == 1]
    res.sort()
    for j in range(0,len(res)-k):
        p.append(res[j])
    s = sum(rest)
    t = sum(p)
    return s-2*t
   
