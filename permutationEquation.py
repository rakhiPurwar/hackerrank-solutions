def permutationEquation(p):
    ls = []
    for i in range(1,len(p)+1):
        r = p.index(i)
        q = p.index(r+1)
        ls.append(q+1)
    return ls
