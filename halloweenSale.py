def howManyGames(p, d, m, s):
    w = 0
    c =0
    while w<=s:
        if p>m:
           w+=p
           c+=1
           p-=d
        else:
            w+=m
            p=m
            c+=1
    if w>s:
        return c-1
    else:
        return c       
